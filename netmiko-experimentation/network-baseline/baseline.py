import os
from netmiko import ConnectHandler
from getpass import getpass

if os.getenv("NETMIKO_PASSWORD"):
    password = os.getenv("NETMIKO_PASSWORD")
else:
    password = getpass()

device = {
    "device_type": "cisco_ios",
    "host": "172.20.20.3",
    "username": "admin",
    "password": password,
    "ssh_config_file": "/home/adminuser/.ssh/config",
}

BASELINE_CONFIGS = [
    "configs/common/banner.txt",
    "configs/common/service.txt",
    "configs/common/clock.txt",
    "configs/common/snmp.txt",
    "configs/common/acl.txt",

]


with ConnectHandler(**device) as net_connect:

    print(f"Connected to {net_connect.find_prompt()}")

    for config_file in BASELINE_CONFIGS:

        print(f"Applying {config_file}...")

        output = net_connect.send_config_from_file(
            config_file,
            cmd_verify=False,
            read_timeout=30
        )

        print(output)