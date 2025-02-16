# SD-WAN-LAB
SD-WAN LAB

# Cisco SD-WAN Lab Setup (using CML) 

Here's the summary of activities performed during this lab :

🔘 CML Setup   
🔘 WSL - Ubuntu   
🔘 Backup    
🔘 Automation   



# Scenario / Architecture


# HQ SITE SETUP 

![image](https://github.com/user-attachments/assets/1950c64f-003a-4856-bd7e-f12cffed9573)

# BRANCHES SETUP 

![image](https://github.com/user-attachments/assets/92a6abe0-928e-4177-8e77-ae251d1c7617)

# ALPINE (END HOSTS) ADDED 

![image](https://github.com/user-attachments/assets/24e87c96-a3a6-4896-adfb-f7868d422fe7)


# WSL - (Ubuntu) Initial Setup 

Check Environment
```
% python3 -c "import sys;assert sys.version_info>(3,9)" && echo "ALL GOOD"
```

Create Working Directory
```
mkdir csdwan
cd csdwan
```

Setup Virtual Environment and Activate 
```
python3 -m venv venv
source venv/bin/activate
```

Update Package and Upgrade Setup Files etc.
```
sudo apt-get update -y 
pip install --upgrade pip setuptools
pip install --upgrade catalyst-sdwan-lab
```

Verify
```
pip freeze | grep catalyst
```


Check lab version
```
sdwan-lab --version
```


Check csdwan version
```
csdwan --version
```

Commands
Add any new SDWAN images (in qcow) format 
```
ls | grep qcow
```



```
csdwan setup
```


```
csdwan deploy 20.15.1
```
//Parameters : /24 , 192.168.255.1 (NAT) environment


# WSL - (Ubuntu) Recurring Commands 


```
cd csdwan
source ./sdwan.sh
source venv/bin/activate
```


```
csdwan setup
csdwan deploy 20.15.1
```
Parameters : /24 and 192.168.255.1 (as Gateway ) for NATted Mode  
Parameters : /24 and 192.168.1.1 (as Gateway) for Bridge Mode  

Add one Edge device at a time (if CPU/Memory constrants)  

```
csdwan add 1 edge 17.15.01a --lab "CSD-WAN-LAB-01"
```

Adding More Devices
```
csdwan add 2 edge 17.15.01a --lab "CSD-WAN-LAB-01"
```

CONFIGURATION FILES:

🔗 SDWAN Setup Script 'sdwan.sh'



```
csdwan add 2 edge 17.15.01a --lab "CSD-WAN-LAB-01"
```


# Backup : 

```
csdwan backup
```

# Delete Lab : 
```
csdwan delete --lab "CSD-WAN-LAB-01"
```


### Alpine (End User Host):
Check IP address (assinged via DHCP)
```
ip addr show
```

Change hostname
```
sudo -E -s

hostname alpine-1
```

Traceroute from Host1 to Host2
```
traceroute -I -n 192.168.2.100
(from 192.168.1.100)
```


Disconnect mpls link, and observer traffic routing through internet link   
Test both failover and fallback scenario

```
while [ 1 == 1 ]; do
traceroute -I -n 192.168.1.100
sleep 1
done

```


### cEdge Device (Cisco) : Edge1 / Edge2

Default Login for Edge Devices
```
admin/admin
```

Look for Gig3 (DHCP settings)
```
show ip interface brief
```

# Labs Included :

🔘 Setup Configuration Groups    
🔘 TLOC / OMP Routes   
🔘 Color Restrict   
🔘 Public and Private TLOC Colors  
🔘 BFD  
🔘 Underlay vs Overlay Routing  
🔘 VPNs and Labels  
🔘 Localized Policy and Centralized Policy    
🔘 TLOC Extensions  
🔘 SD-WAN UseCases     
🔘 AAR (Application Aware Routing etc.)  
🔘 Many More...




# FINAL STATUS:

    [✔️] Add Manager, Validator , Controller
    [✔️] Add cEdges (c8000v)
    [✔️] Add Alpine (End Hosts)
    [✔️] Validate Traffic from Branch1 to Branch2 via MPLS Link
    [✔️] Remove MPLS link and Validate Traffic from Branch1 to Branch2 via Internet Link




# REFERENCE:

🔗 https://github.com/cisco-open/sdwan-lab-deployment-tool
