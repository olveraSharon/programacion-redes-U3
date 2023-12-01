#Autor: Shraon Michelle Olvera Ibarra
#Descripción: NETCONF con Python: Capacidades de lista
#Fecha: 01/12/2023

import ncclient

from ncclient import manager
m = manager.connect(
    host = "10.10.20.48",
    port = 830,
    username = "developer",
    password = "C1sco12345",
    hostkey_verify = False
)
print("# Supported Capacidades (modelos YANG):")
for capacidad in m.server_capabilities:
    print(capacidad)
    