# -*- coding: utf-8 -*-
"""
A simple utility for fetching and simplifying an web article for passing to pandoc
"""

import argparse
import collections

# from boilerpy3 import extractors

import requests
# from readability import Document
import readability

"""
Notes:

print() is sent to stdout, while error text like unhandled exception text is sent to stderr; and can
be redirected/sorted by the standard shell tricks.

Exit Codes -  Any unhandled exception will result in a non-zero exit code.

References:

1.  https://docs.python.org/3/howto/argparse.html
2.  https://docs.python.org/3/library/argparse.html
"""

__author__      = 'Justin Stout'
__copyright__   = 'Copyright 2021, {}'.format(__author__)
__credits__     = [__author__]
__license__     = 'MIT'
__version__     = '0.1.0'               # major.minor.hotfix/patch
__maintainer__  = __author__
__email__       = 'justin@jstout.us'
__status__      = 'Alpha'            # 'Pre-Alpha'. 'Alpha', 'Beta', 'Production/Stable'
__doc__         = 'Simplify a web article'  # will be displayed in --help message


def _cli():
    """Parse cli options and return a dictionary."""
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)

    # optional arguments
    # parser.add_argument('-f', '--foo', help="This is the foo argument")
    # parser.add_argument('-b', '--bar', help="This is the bar argument")

    # qux_help = ("This argument will show its default in the help due to "
    #             "ArgumentDefaultsHelpFormatter")
    # parser.add_argument('-q', '--qux', default=3, help=qux_help)

    # required positional args
    parser.add_argument('url', help="Article URL")

    args = parser.parse_args()

    return vars(args)


def setup(app):
    """Do any required setup actions like read config file, create tmp dir, etc."""
    pass


def cleanup(app):
    """Perform any necessary cleanup operations like deleting a tmp dir."""
    pass


def main(app):
    """Actual business logic goes here."""
    print(app['args']['url'])

    # extractor = extractors.ArticleExtractor()

    # doc = extractor.get_doc_from_url(app['args']['url'])
    # print(doc.title)
    # print("\n")
    # print(doc.content)

    # print(extractor.get_content_from_url(app['args']['url']))

    # print()
    # print('=========================')
    # print()

    # print(doc.title)
    # print()
    # print('=========================')
    # print()
    # print(doc.content)

    # print(extractor.get_content_from_url(app['args']['url']))

    # extractor = extractors.CanolaExtractor()
    # print(extractor.get_content_from_url(app['args']['url']))

if __name__ == '__main__':
    app = collections.defaultdict(dict)

    try:
        app['args'] = _cli()
        main(app)

    # except ExpectedException:
    #     """Optional - An expected exception that requires special handeling."""
    #     # handle_exception(app)
    #     # raise (re-raise exception if non-zero exit code is desired)

    finally:
        """This always runs; if, and if not, and exception was raised."""
        cleanup(app)
