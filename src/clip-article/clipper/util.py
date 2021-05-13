# -*- coding: utf-8 -*-
import json

from pathlib import Path


def get_resource_path(resource_name):
    bundle_dir = Path(__file__).parent
    return Path.cwd() / bundle_dir / 'resources'/ resource_name


def write_attach(root_dir, name, data):

    target = root_dir / name

    with target.open('w') as fd_out:
        if type(data) is dict:
            json.dump(data, fd_out, indent=4, sort_keys=True)

        else:
            fd_out.write(data)

    return target
