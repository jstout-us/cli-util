import argparse
import collections

from clipper.__main__ import main

def _cli():
    """Parse cli options and return a dictionary."""
    parser = argparse.ArgumentParser(
            description=__doc__,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            argument_default=argparse.SUPPRESS)

    parser.add_argument('url', help="Article URL")

    args = parser.parse_args()

    return vars(args)


if __name__ == '__main__':
    app = collections.defaultdict(dict)

    try:
        app['args'] = _cli()
        main(app)

    finally:
        pass
