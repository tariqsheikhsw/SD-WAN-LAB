# SD-WAN-LAB
SD-WAN LAB

# Cisco SD-WAN Lab Setup (using CML) 

Here's the summary of activities performed during this lab :

🔘 CML Setup   
🔘 WSL - Ubuntu 

# Scenario / Architecture



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
source <(kubectl completion bash) # setup autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```


CONFIGURATION FILES:

🔗 Deployment 'alpha-xyz'
🔗 Service 'alpha-svc'
🔗 NetworkPolicy 'restrict-inbound'
🔗 NetworkPolicy 'external-network-policy'
🔗 AppArmor Profile 'custom-nginx'


# FINAL STATUS:

    [✔️] PVC to PV binding
    [✔️] Image Scanning using Aquasec Trivy
    [✔️] Ingress and Egress Network Policy Implementation
    [✔️] Secure Deployment using AppArmor Profile
    [✔️] Expose Deployment with NodePort Type Service




# REFERENCE:

🔗 https://github.com/cisco-open/sdwan-lab-deployment-tool
