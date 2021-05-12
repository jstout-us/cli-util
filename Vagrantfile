# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

DEV_CFG_ROOT = ENV["DEV_CFG_ROOT"]

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.ssh.forward_agent = true
  config.vm.hostname = "cli-util"
  config.vm.provision "file", source: "#{DEV_CFG_ROOT}/locations/jstout-us/gitconfig",
                              destination: ".gitconfig",
                              run: "always"
  config.vm.provision "shell", path: "bin/vagrant_provision.sh"
  config.vm.provision "shell", path: "bin/vagrant_provision_user.sh", privileged: false
end
