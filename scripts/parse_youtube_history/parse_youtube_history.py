#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repo: https://github.com/jstout-us/cli-util
"""

import argparse
import collections
import csv

from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from dateutil import parser
from dateutil import tz

from pprint import pprint as pp

__author__      = 'Justin Stout'
__copyright__   = 'Copyright 2019, {}'.format(__author__)
__credits__     = [__author__]
__license__     = 'MIT'
__version__     = '0.1.0'
__maintainer__  = __author__
__email__       = 'justin@jstout.us'
__status__      = 'Production/Stable'
__doc__         = 'Parse YouTube watch-history.html file from Google Takeout'

MONTHS_SHORT = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
TAG_FIELDS = ['channel_id', 'channel_title', 'video_id', 'video_title', 'watched']
TIMEZONES = {
    'EDT': 'US/Eastern',
    'EST': 'US/Eastern'
    }

class DeletedVideoError(Exception):
    """Exception raised for deleted videos."""
    pass


def _cli():
    """Parse cli options and return a dictionary."""
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)

    # required positional args
    parser.add_argument('history_file', help="Path to source file.")

    args = parser.parse_args()

    return vars(args)


def _parse_urls(links):
    """Extract channel id, channel title, video id, and video title."""

    channel_id = None
    channel_title = None
    video_id = None
    video_title = None

    tag_video_a = links.pop(0)
    video_id = urlparse(tag_video_a.attrs['href']).query.split('=')[-1]
    video_title = tag_video_a.contents[0]

    try:
        tag_channel_a = links.pop(0)
        channel_id = urlparse(tag_channel_a.attrs['href']).path.split('/')[-1]
        channel_title = tag_channel_a.contents[0]

    except IndexError:
        """Missing channel URL tag; aka an orphaned video."""
        pass

    return [channel_id, channel_title, video_id, video_title]


def _parse_watched(text):
    """Extract datetime from tag text and return iso formated datetime str."""

    idx_left = sorted([x for x in [text.rfind(y) for y in MONTHS_SHORT] if x > -1],
                      reverse=True)[0]
    idx_right = text.rfind(' ')

    tz_ = TIMEZONES[text[idx_right:].strip()]
    watched = parser.parse(text[idx_left:idx_right]).replace(tzinfo=tz.gettz(tz_))

    return [watched.astimezone(tz.UTC).isoformat()]


def _parse_tag(tag):
    """Extract and return relavant fields from the html tag."""

    try:
        values = _parse_urls(tag.find_all('a'))
        values.extend(_parse_watched(tag.text))

    except IndexError:
        raise DeletedVideoError

    return dict(zip(TAG_FIELDS,values))


def setup(app):
    """Do any required setup actions like read config file, create tmp dir, etc."""
    app['info'] = {
        'time_start': datetime.now(),
        'records': {
            'count': 0,
            'orphans': 0,
            'deleted': 0,
            'errors': 0
            },
        }

    app['files'] = {
        'dst': Path('watch-history.csv'),
        'src': Path(app['args']['history_file'])
        }


def cleanup(app):
    """Perform any necessary cleanup operations like deleting a tmp dir."""
    time_run = (datetime.now() - app['info']['time_start']).total_seconds()

    print('Run Time:         {:.1f} seconds'.format(time_run))
    print('Records:')
    print('    Total:        {}'.format(app['info']['records']['count']))
    print('    Orphans:      {}'.format(app['info']['records']['orphans']))
    print('    Deleted:      {}'.format(app['info']['records']['deleted']))
    print('    Parse Errors: {}'.format(app['info']['records']['errors']))
    print()


def main(app):
    """Actual business logic goes here."""

    with app['files']['src'].open() as fd_src:
        selectors = {"class": "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"}
        soup = BeautifulSoup(fd_src.read(),
                             "html.parser",
                             parse_only=SoupStrainer(**selectors)
                             )

    with app['files']['dst'].open('w') as fd_out:
        writer = csv.DictWriter(fd_out, fieldnames=TAG_FIELDS)
        writer.writeheader()

        for tag in soup:
            app['info']['records']['count'] += 1

            try:
                record = _parse_tag(tag)

                if not record['channel_id']:
                    app['info']['records']['orphans'] += 1

                writer.writerow(record)

            except DeletedVideoError:
                app['info']['records']['deleted'] += 1


if __name__ == '__main__':
    app = collections.defaultdict(dict)

    try:
        app['args'] = _cli()
        setup(app)
        main(app)

    finally:
        cleanup(app)
