import os
import tabulate

from vmanage.api.authentication import Authentication
from vmanage.api.device import Device

def print_device_table(devices):
    print("Formatting device output.")
    headers = [
        "Host-Name",
        "Device Type",
        "Device ID",
        "Syster IP",
        "Site ID",
        "Version",
        "Device Model",
    ]
    
    #Code from here
    


def main():
    manager_host = os.environ.get('MANAGER_HOST')
    manager_username = os.environ.get('MANAGER_USERNAME')
    manager_password = os.environ.get('MANAGER_PASSWORD')

    if not (manager_host and manager_username and manager_password):
        print(f"CISCO SDWAN details must be set via environment variables before running the script!\n"
              f"   export MANAGER_HOST=X.X.X.X\n"
              f"   export MANAGER_USERNAME=admin\n"
              f"   export MANAGER_PASSWORD=PassWord\n")
        exit(1)

    session = Authentication(host=manager_host, user=manager_username, password=manager_password, port=8443).login()
    device = Device(session, manager_host)
    device_list = device.get_device_list("controllers")
    print_device_table(device_list)


if __name__ == "__main__":
    main()
