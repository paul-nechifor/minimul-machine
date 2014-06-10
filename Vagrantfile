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
  if File.file?('private/client_id')
    config.vm.provider :digital_ocean do |provider, override|
      override.ssh.private_key_path = '~/.ssh/id_rsa'
      override.vm.box = 'digital_ocean'
      override.vm.box_url = 'https://github.com/smdahlen/vagrant-digitalocean/raw/master/box/digital_ocean.box'
      provider.client_id = File.read('private/client_id').strip
      provider.api_key = File.read('private/api_key').strip
    end
  end
end
