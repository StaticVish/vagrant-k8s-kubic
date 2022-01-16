# Vagrant Kubic Kubernetes Cluster for OpenFAAS Learning. 

This is my K8S cluster built on openSUSE for Learning OpenFAAS. The idea is to have an managed Kubernetes cluster with a Simple Just Enough Operating Systems. 


This is a Multi Worker Nodes Cluster. 

Some Vagrant Commands Used in this Project

## Get the Nodes and its State
vagrant status --machine-readable | awk -F "," '$3 ~/^state$/{print $2,$4}'

The Plugin Required is 

vagrant plugin install vagrant-address for generating the 

* vagrant up
* ansible all -m ping
* ansible-playbook ./k8s-setup/01-base-setup.yaml 
* ansible-playbook ./k8s-setup/02-loadbalancer-setup.yaml 
* ansible-playbook ./k8s-setup/03-k8s-master-setup.yaml 
* ansible-playbook ./k8s-setup/04-k8s-minion-setup.yaml 
* ansible-playbook ./k8s-setup/05-k8s-cluster-setup.yaml 
* vagrant destroy -f
