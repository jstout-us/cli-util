# -*- coding: utf-8 -*-
"""Utility methods for clipper."""
import json

from pathlib import Path


def get_resource_path(resource_name):
    """Return path to module resource dir.

    :return: Path to module resource dir.
    :rtype: Path()
    """
    bundle_dir = Path(__file__).parent
    return Path.cwd() / bundle_dir / 'resources'/ resource_name


def write_attach(root_dir, name, data):
    """Write article attachments to disk.

    :param root_dir: path to output directory
    :type root_dir: Path()
    :param name: output file name
    :type name: str
    :param data: data to write to disk
    :type data: dict or str
    """
    target = root_dir / name

    with target.open('w') as fd_out:
        if isinstance(data, dict):
            json.dump(data, fd_out, indent=4, sort_keys=True)

        else:
            fd_out.write(data)

    return target
