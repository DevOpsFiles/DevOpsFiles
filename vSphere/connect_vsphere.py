# Create Session to your vSphere Environment
# Notice to save u\n and password outside this file for security reasons.

import requests
from requests.auth import HTTPBasicAuth
import json 

conn = ""

def connect_vc():
    global conn
    url = "https://<vSphere FQDN/or/I.P>/rest/com/vmware/cis/session"
    user='your user for vpshere login'
    password='your user password'
    payload={}
    files={}
    response = requests.request("POST", url, auth=HTTPBasicAuth(user, password), data=payload, files=files,verify=False)
    myconn = response.text
    conn_json = json.loads(myconn)
    conn_value = conn_json['value']
    print("Open Connetion")
    conn = conn_value
    print(conn)
    return str(conn)

  
connect_vc()  
