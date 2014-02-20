# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.ssh.forward_agent = true
  config.vm.synced_folder "/.", "/vagrant"
  config.vm.network :forwarded_port, guest: 5000, host: 5001
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :forwarded_port, guest: 81, host: 8081

  config.vm.provision :shell, :path => "bootstrap.sh"
end
