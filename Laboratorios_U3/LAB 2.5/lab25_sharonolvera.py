#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Conexión RESTCONF con python
#Fecha: 05/12/2023

import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json", 
             "Content-type":"application/yang-data+json"
           } 

basicauth = ("developer", "C1sco12345")
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
response_json = resp.json()
print(json.dumps(response_json, indent=4))
