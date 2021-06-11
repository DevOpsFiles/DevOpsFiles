#List All VM's on your vSphere Environment
#This Func relys on the "connect_to_vsphere.py"/gist
#so if you dont use it in the same file you have to import json,import requests & from requests.auth import HTTPBasicAuth

def list_vms():
    url = "https://<vSphere FQDN/or/I.P>/rest/com/vmware/cis/session"
    authentication = conn
    payload={}
    headers = {
        'vmware-api-session-id':conn,
        'Content-Type' : 'application/json'
        }

    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    json_vm_list = json.loads(response.text)
    print(json_vm_list)
    return json_vm_list

#Call Function
list_vms()