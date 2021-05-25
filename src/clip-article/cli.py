# -*- coding: utf-8 -*-
"""Clip web article as a cleaned/simplified PDF file with metadata."""
import argparse
import collections
import tempfile

from pathlib import Path

from clipper.__main__ import main


def _cli():
    """Parse cli options and return a dictionary."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        argument_default=argparse.SUPPRESS)

    parser.add_argument('url', help="Article URL")
    parser.add_argument('file_name', type=Path, help="Output File Name")

    args = parser.parse_args()

    return vars(args)


if __name__ == '__main__':
    app = collections.defaultdict(dict)     # pylint: disable=invalid-name

    try:
        app['args'] = _cli()
        with tempfile.TemporaryDirectory() as work_dir:
            app['work_dir'] = Path(work_dir)
            main(app)

    finally:
        pass
