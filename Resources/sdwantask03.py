import os

from vmanage.api.authentication import Authentication
from vmanage.api.device import Device
from vmanage.api.device_templates import DeviceTemplates
from vmanage.api.feature_templates import FeatureTemplates
from vmanage.data.template_data import TemplateData


def switch_feature_templates(device_template, feature_templates, old_template_name, new_template_name):
    print(f"Switching feature templates {old_template_name} and {new_template_name} on device template {device_template['templateName']}")
    
    #Code from here
    



def get_attach_device(device_object, device_name):
    device_list = device_object.get_device_list("controllers")
    attach_device = None
    for device in device_list:
        if "host-name" in device and device["host-name"] == device_name:
            return device
    return None


def main():
    manager_host = os.environ.get('MANAGER_HOST')
    manager_username = os.environ.get('MANAGER_USERNAME')
    manager_password = os.environ.get('MANAGER_PASSWORD')
    manager_port = 8443

    if not (manager_host and manager_username and manager_password):
        print(f"CISCO SDWAN details must be set via environment variables before running the script!\n"
              f"   export MANAGER_HOST=X.X.X.X\n"
              f"   export MANAGER_USERNAME=admin\n"
              f"   export MANAGER_PASSWORD=PassWord\n")
        exit(1)

    session = Authentication(host=manager_host, user=manager_username, password=manager_password, port=manager_port).login()
    attach_device = get_attach_device(Device(session, manager_host, port=manager_port), "vSmart")
    
    device_templates=DeviceTemplates(session, manager_host, manager_port)
    device_templates_list = device_templates.get_device_template_list(name_list=["vSmart_Golden_Template_v1"])
    
    feature_templates = FeatureTemplates(session, manager_host, manager_port)
    feature_templates_dict = feature_templates.get_feature_template_dict(key_name="templateName")
    
    if device_templates_list:
        updated_template = switch_feature_templates(device_templates_list[0], feature_templates_dict, "vSmart_aaa_template", "new_vSmart_aaa_template")
        device_templates.update_device_template(updated_template)
        print("Device template updated!")
        
        device_variables = {
            "system_host_name": "vSmart", 
            "system_system_ip": "X.X.X.X",
            "system_site-id": "100"
        }
        device_templates.attach_to_template(updated_template["templateId"], 
                                            attach_device["uuid"], 
                                            attach_device["system-ip"], 
                                            attach_device["host-name"], 
                                            attach_device["site-id"], 
                                            device_variables) 

        print("Updated device template is attached to the device!")
        
        
if __name__ == "__main__":
    main()
