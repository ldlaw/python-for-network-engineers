import os
from netmiko import ConnectHandler
from getpass import getpass

if os.getenv("NETMIKO_PASSWORD"):
    password = os.getenv("NETMIKO_PASSWORD")
else:
    password = getpass()

device = {
    "device_type": "cisco_ios",
    "host": "172.20.20.4",
    "username": "admin",
    "password": password,
    "ssh_config_file": "/home/adminuser/.ssh/config",
}


with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command("show ip interface brief")
    print(output)
