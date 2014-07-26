# -*- mode: ruby -*-
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise64"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/site.yml"
    #ansible.verbose = "vvvv"
  end
end
