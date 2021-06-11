#Get the UUID of selected VM by its name
#This Func relys on the "connect_to_vsphere.py" and "list_vms.py"/gist
#so if you dont use it in the same file you have to import json,import requests & from requests.auth import HTTPBasicAuth

def get_vm_uuid(VM):
    vm_uuid = ""
    print("find the UUID for VM:" + VM)
    vms_list = list_vms()
    for v in vms_list['value']:
        if VM == v['name']:
            print("Found Requested VM.")
            print(VM)
            vm_uuid = v["vm"]
            print(vm_uuid)
        elif VM != v['name']:
            vm_uuid = 'VM NOT FOUND'    
    return str(vm_uuid)

#Call Function
get_vm_uuid('VM Name')