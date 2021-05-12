export DEBIAN_FRONTEND=noninteractive

echo "Set Time Zone"
timedatectl set-timezone America/Los_Angeles

echo "Install base Ubuntu dependencies"
apt-get update
apt-get install -y apt-transport-https \
                   ca-certificates \
                   curl \
                   software-properties-common

echo "Add Ubuntu Dependencies"

apt-get install -y build-essential \
                   git \
                   git-flow \
                   pandoc \
                   python3-dev \
                   python3-pip \
                   texlive-latex-extra \
                   tig

echo "Installing python dependencies"

/usr/bin/env python3 -m pip install --upgrade bumpversion==0.5.3 \
                                              goose3 \
                                              invoke==1.1.1 \
                                              js-invoke==2.1.1 \
                                              nanoid==2.0.0 \
                                              newspaper3k==0.2.8 \
                                              pip \
                                              pyclean \
                                              pycodestyle==2.4.0 \
                                              pydocstyle==2.1.1 \
                                              pyinstaller \
                                              pylint==2.3.1 \
                                              pypdf4==1.27.0 \
                                              pytest-cov==2.5.1 \
                                              pytest==3.7.1 \
                                              readability-lxml \
                                              requests
