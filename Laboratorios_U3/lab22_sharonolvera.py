#Autor: Shraon Michelle Olvera Ibarra
#Descripción: Conexión a servicio SSH de IOS XE usando netmiko
#Fecha: 24/11/2023

from netmiko import ConnectHandler

device_params = {
    'device_type': 'cisco_ios',
    'host': '10.10.20.48',
    'port': '22',
    'username': 'developer',
    'password': 'C1sco12345',
}

sshCli = ConnectHandler(**device_params)

config_commands = [
    'interface loopback 2',
    'ip address 2.2.2.2 255.255.255.0',
    'description ANOTHER_DESCRIPTION'
]

output = sshCli.send_config_set(config_commands)

print(output)

current_interfaces = sshCli.send_command('show ip int brief')
print(current_interfaces)



