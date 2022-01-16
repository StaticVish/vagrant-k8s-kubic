#!/usr/bin/env python3
import subprocess
import json


ansible_base_inventory_template = {
    '_meta': {
        'hostvars': {
        }
    },
    'all': {
        'children': [
            "lbs",
            "masters",
            "minions"
        ]
    },
    "lbs": {
        "hosts": [],
    },
    "masters": {
        "hosts": []
    },
    "minions": {
        "hosts": []
    }
}

lbs = []
masters = []
minions = []

ansible_lbs = {}
ansible_masters = {}
ansible_minions = {}

status_cmd = "vagrant status --machine-readable"
status_output_lines = subprocess.check_output(
    status_cmd.split()).rstrip().decode('utf-8')

for line in status_output_lines.split('\n'):
    statuskey = line.split(',')
    if (len(statuskey) == 4):
        if (str(statuskey[2]) == "state"):
            node_name = statuskey[1]
            node_state = statuskey[3]
            if("-lbs-" in node_name and node_state == "running"):
                lbs.append(node_name)
            elif("-masters-" in node_name and node_state == "running"):
                masters.append(node_name)
            elif("-minions-" in node_name and node_state == "running"):
                minions.append(node_name)

for node in lbs:
    cmd = "vagrant address {}".format(node)

    node_address = subprocess.check_output(
        cmd.split()).rstrip().decode('utf-8')

    node_name = "ip-%s.sslip.io" % (
        node_address.rstrip('\n').replace(".", "-"))

    ansible_lbs[node_name] = node_address.rstrip('\n')

for node in masters:
    cmd = "vagrant address {}".format(node)

    node_address = subprocess.check_output(
        cmd.split()).rstrip().decode('utf-8')

    node_name = "ip-%s.sslip.io" % (
        node_address.rstrip('\n').replace(".", "-"))

    ansible_masters[node_name] = node_address.rstrip('\n')


for node in minions:
    cmd = "vagrant address {}".format(node)

    node_address = subprocess.check_output(
        cmd.split()).rstrip().decode('utf-8')

    node_name = "ip-%s.sslip.io" % (
        node_address.rstrip('\n').replace(".", "-"))

    ansible_minions[node_name] = node_address.rstrip('\n')


# print(json.dumps(ansible_lbs), json.dumps(
#     ansible_masters), json.dumps(ansible_minions))


for key, value in ansible_lbs.items():
    ansible_base_inventory_template["lbs"]["hosts"].append(key)
    ansible_base_inventory_template["_meta"]["hostvars"][key] = {}
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_host"] = value
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_python_interpreter"] = "/usr/bin/python3"
    ansible_base_inventory_template["_meta"]["hostvars"][key][
        "ansible_ssh_private_key_file"] = "~/.vagrant.d/insecure_private_key"
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_user"] = "vagrant"

for key, value in ansible_masters.items():
    ansible_base_inventory_template["masters"]["hosts"].append(key)
    ansible_base_inventory_template["_meta"]["hostvars"][key] = {}
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_host"] = value
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_python_interpreter"] = "/usr/bin/python3"
    ansible_base_inventory_template["_meta"]["hostvars"][key][
        "ansible_ssh_private_key_file"] = "~/.vagrant.d/insecure_private_key"
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_user"] = "vagrant"

for key, value in ansible_minions.items():
    ansible_base_inventory_template["minions"]["hosts"].append(key)
    ansible_base_inventory_template["_meta"]["hostvars"][key] = {}
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_host"] = value
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_python_interpreter"] = "/usr/bin/python3"
    ansible_base_inventory_template["_meta"]["hostvars"][key][
        "ansible_ssh_private_key_file"] = "~/.vagrant.d/insecure_private_key"
    ansible_base_inventory_template["_meta"]["hostvars"][key]["ansible_user"] = "vagrant"

ansible_inventory = json.dumps(ansible_base_inventory_template)
print(ansible_inventory)
