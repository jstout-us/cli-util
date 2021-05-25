===================================================================================================
CLI Utilities
===================================================================================================

A collection of my standard CLI scripts and utilities.

Configuration
===================================================================================================

ENV VARS: (add to $HOME/.profile)

- DEV_ROOT:                 Dev root directory ($HOME/dev)
- DEV_CFG_ROOT:             Dev config root ($HOME/.config/dev)
- DEV_CFG_ROOT_BKUP:        Backup directory
- DEV_CFG_BKUP_GPG_KEY:     GPG key name


Install
===================================================================================================

Scripts are installed to $HOME/bin

Ubuntu
---------------------------------------------------------------------------------------------------

.. code-block:: console

    $ sudo apt update
    $ sudo apt install -y pandoc \
                          python3-bs4 \
                          python3-dateutil \
                          texlive-latex-extra

    $ make install


License
===================================================================================================

This software is dstributed under the MIT License, see `LICENSE <LICENSE>`_ for more information.
