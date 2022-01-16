# -*- mode: ruby -*-
# vi:set ft=ruby sw=2 ts=2 sts=2:

OS_IMAGE = 'opensuse/Kubic.x86_64'

NUM_LBS = 1
NUM_MASTERS = 3
NUM_WORKERS = 3


Vagrant.configure("2") do |config|
  config.ssh.insert_key = false

  # Provision the Empty Nodes
  (1..NUM_LBS).each do |i|
    config.vm.define "kubic-lbs-#{i}" do |node|
      node.vm.box = OS_IMAGE
      node.vm.synced_folder ".", "/vagrant", disabled: true      
      node.vm.provider :libvirt do |v|
        v.qemu_use_session = false
        v.memory = 2048
        v.cpus= 2
      end
    end
  end

  # Provision the Empty Nodes
  (1..NUM_MASTERS).each do |i|
    config.vm.define "kubic-masters-#{i}" do |node|
      node.vm.box = OS_IMAGE
      node.vm.synced_folder ".", "/vagrant", disabled: true      
      node.vm.provider :libvirt do |v|
        v.qemu_use_session = false
        v.memory = 2048
        v.cpus= 2
      end
    end
  end

  # Provision the Empty Nodes
  (1..NUM_WORKERS).each do |i|
    config.vm.define "kubic-minions-#{i}" do |node|
      node.vm.box = OS_IMAGE
      node.vm.synced_folder ".", "/vagrant", disabled: true      
      node.vm.provider :libvirt do |v|
        v.qemu_use_session = false
        v.memory = 2048
        v.cpus= 2
        v.storage :file, :size => '50GB',:path => "kubic_node_#{i}_vdb.img", :allow_existing => true, :type => 'raw'
      end
    end
  end
end
