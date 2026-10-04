##########################################
# INITIAL DEVICE CONFIGURATION
##########################################

from netmiko import ConnectHandler

cisco_c8k1 = {
    "device_type": "cisco_ios",
    "host": "10.1.6.163",
    "username": "admin",
    "password": "Cisco123!",
}

cisco_c8k2 = {
    "device_type": "cisco_ios",
    "host": "10.1.6.168",
    "username": "admin",
    "password": "Cisco123!",
}

cisco_c8k3 = {
    "device_type": "cisco_ios",
    "host": "10.1.6.173",
    "username": "admin",
    "password": "Cisco123!",
}


##########################################
# SHOW COMMANDS 
##########################################
net_connect = ConnectHandler(**cisco_c8k1)

output = net_connect.send_command("show ip interface brief")
print(output)

output = net_connect.send_command("show ip arp")
print(output)
############################

net_connect = ConnectHandler(**cisco_c8k2)

output = net_connect.send_command("show ip interface brief")
print(output)

output = net_connect.send_command("show ip arp")
print(output)
############################

net_connect = ConnectHandler(**cisco_c8k3)

output = net_connect.send_command("show ip interface brief")
print(output)

output = net_connect.send_command("show ip arp")
print(output)

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
    "interface gi1",
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
    "interface gi1",
    "ip address 10.0.13.3 255.255.255.240",
    "no shut",
]

cfg_output = net_connect.send_config_set(cfg_list)
