#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check all directories in $DEV_ROOT and alert on those that have:

1.  Running vagrant machines
2.  Repos with local branches
3.  Repos with commits that haven't been pushed to origin

ENV VARS: (add to $HOME/.profile)
    DEV_ROOT:                 Dev root directory ($HOME/dev)
"""
import os
import subprocess

from pathlib import Path

def _git_get_repos(dev_root):
    """Walk root directory and yield all childer containing a .git folder

    :param dev_root: Path to development root directory
    :type dev_root: :class:`pathlib.Path()`

    :return: Path to directory containing .git child directory
    :rtype: :class:`pathlib.Path()`
    """
    for path in dev_root.glob('**/.git'):
        yield path.parent


def _git_get_branches(repo):
    """Get current branches for git repo.

    :param repo: Path to directory containing a git repo
    :type repo: :class:`pathlib.Path()`

    :return: tuple of lists containing local and remote branches
    :rtype: tuple(list, list)
    """
    options = ['git', '-C', str(repo), 'branch', '-a']
    result = _run_cmd(options)

    branches = [ x for x in result.stdout.decode().split() if x != '*']

    filter_elements = [x for x in branches if 'HEAD -> origin' in x]
    filter_branches = [x for x in branches if x not in filter_elements]

    remote = [x[-1] for x in filter_branches if x[0] == 'remotes']
    local = [x[-1] for x in filter_branches if x[-1] not in remote]

    return (local, remote)


def _git_get_ahead(repo):
    """Return True if there are remote branches that are ahead of origin.

    :param repo: Path to directory containing a git repo
    :type repo: :class:`pathlib.Path()`

    :return: True if there are branches ahead of origin.
    :rtype: bool
    """
    branches_ahead = False
    options = ['git', '-C', str(repo), 'for-each-ref',
               '--format="%(refname:short) %(upstream:track)"', 'refs/heads']
    results = _run_cmd(options).stdout.decode().split()

    for line in results:
        if 'ahead' in line:
            branches_ahead = True

    return branches_ahead


def _git_is_dirty(status):
    """Test if repo status is dirty.

    :params status: repos status information
    :type status: dict

    :return: Is Dirty
    :rtype: bool
    """
    if status['uncommited changes'] or status['local only branches'] or status['ahead of origin']:
        return True

    return False


def _git_repo_status(repo):
    """Get current git repo status.

    :param repo: Path to directory containing a git repo
    :type repo: :class:`pathlib.Path()`

    :return: Repo status
    :rtype: dict
    """
    repo_status = {
        'path': repo
        }

    options = ['git', '-C', str(repo), 'status', '-s']
    changes = _run_cmd(options).stdout.decode()
    repo_status['uncommited changes'] = True if len(changes) else False

    local, remote = _git_get_branches(repo)
    repo_status['local only branches'] = bool(set(remote) - set(local))

    repo_status['ahead of origin'] = _git_get_ahead(repo)

    return repo_status


def _vagrant_parse_results(result):
    """Yield lines containing 'running' as vm status.

    :param result: STDOUT response from calling vagrant global-status
    :type result: str

    :return: vm status == running
    :rtype: str
    """
    for line in result.split('\n'):
        if 'running' in line:
            yield line


def _vagrant_format_results(line):
    """Extract fields from vm status line.

    :param line: Status line for a running vm
    :type line: str

    :return: (<vm directory path>, <vm status>)
    :rtype: tuple of strings
    """
    line_split = line.split()
    return (line_split[-1], line_split[-2],)


def _run_cmd(options):
    """Run a system command/program as a subprocess.

    :param options: List of arguments to pass to :class:`subprocess.run()`
    :type options: list

    :return: :class:`subprocess.run()` results
    :rtype: :class:`subprocess.CompletedProcess`
    """
    return subprocess.run(options, stdout=subprocess.PIPE)


def check_vagrant_status():
    """Get Vagrant global status.

    :return: [(<vm directory path>, <vm status>)]
    :rtype: list of tuples
    """
    options = ['/usr/bin/env', 'vagrant', 'global-status']
    result = _run_cmd(options)

    return [_vagrant_format_results(x) for x in _vagrant_parse_results(result.stdout.decode())]


def check_repo_status(dev_root):
    """Check status of all directories with a .git child under DEV_ROOT for is_dirty.

    :param dev_root: Path to dev root directory
    :type repo: :class:`pathlib.Path()`

    :return: A list of repos where status == dirty
    :rtype: [dict]
    """
    repo_status = [_git_repo_status(x) for x in _git_get_repos(dev_root)]
    repos_dirty = [x for x in repo_status if _git_is_dirty(x)]

    return repos_dirty


def main(dev_root):

    print('Running VMs')
    print('-'*60)
    for vm_path, _ in check_vagrant_status():
        print('\t{}'.format(vm_path))

    print()
    print('Dirty Repos')
    print('-'*60)
    keys_filter = ['path']
    for repo in check_repo_status(dev_root):
        print('{}'.format(repo['path'].relative_to(dev_root)))

        for key, value in repo.items():
            if key not in keys_filter and value:
                print('\t{:20}'.format(key))


if __name__ == '__main__':
    main(Path(os.environ['DEV_ROOT']))
