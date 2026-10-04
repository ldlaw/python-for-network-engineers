import os
from netmiko import ConnectHandler
from getpass import getpass

if os.getenv("NETMIKO_PASSWORD"):
    password = os.getenv("NETMIKO_PASSWORD")
else:
    password = getpass()


cisco_c8k1 = {
    "device_type": "cisco_ios",
    "host": "172.20.20.4",
    "username": "admin",
    "password": password,
    "ssh_config_file": "/home/adminuser/.ssh/config",
}

cisco_c8k2 = {
    "device_type": "cisco_ios",
    "host": "172.20.20.3",
    "username": "admin",
    "password": password,
    "ssh_config_file": "/home/adminuser/.ssh/config",
}

cisco_c8k3 = {
    "device_type": "cisco_ios",
    "host": "172.20.20.2",
    "username": "admin",
    "password": password,
    "ssh_config_file": "/home/adminuser/.ssh/config",
}

##########################################
# CONFIGURE IP ADDRESS 
##########################################

net_connect = ConnectHandler(**cisco_c8k1)

cfg_list = [
    "hostname C8k-1",
    "interface gi2",
    "ip address 10.0.12.1 255.255.255.240",
    "no shut",
    "interface gi3",
    "ip address 10.0.13.1 255.255.255.240",
    "no shut",
]

cfg_output = net_connect.send_config_set(cfg_list)


net_connect = ConnectHandler(**cisco_c8k2)

cfg_list = [
    "hostname C8k-2",
    "interface gi2",
    "ip address 10.0.12.2 255.255.255.240",
    "no shut",
    "interface gi3",
    "ip address 10.0.23.2 255.255.255.240",
    "no shut",
]

cfg_output = net_connect.send_config_set(cfg_list)



net_connect = ConnectHandler(**cisco_c8k3)

cfg_list = [
    "hostname C8k-3",
    "interface gi2",
    "ip address 10.0.23.3 255.255.255.240",
    "no shut",
    "interface gi3",
    "ip address 10.0.13.3 255.255.255.240",
    "no shut",
]

cfg_output = net_connect.send_config_set(cfg_list)
