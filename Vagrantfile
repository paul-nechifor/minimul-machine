Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/precise64"
  vmname = "minimul"
  config.vm.define vmname.to_sym do |machine|
    machine.vm.host_name = vmname
    machine.vm.network "private_network", ip: "10.10.10.10"
    machine.vm.provider "virtualbox" do |v|
      v.name = vmname
      v.memory = 512
      v.cpus = 1
    end
    machine.vm.provision "shell", path: "scripts/provision.sh"
  end
end
