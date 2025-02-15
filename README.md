# SD-WAN-LAB
SD-WAN LAB

# Cisco SD-WAN Lab Setup (using CML) 

Here's the summary of activities performed during this lab :

🔘 CML Setup   
🔘 WSL - Ubuntu 

# Scenario / Architecture



# WSL - (Ubuntu) Initial Setup 

BASH
```
% python3 -c "import sys;assert sys.version_info>(3,9)" && echo "ALL GOOD"
```

BASH
```
mkdir csdwan
cd csdwan
```

BASH
```
python3 -m venv venv
source venv/bin/activate
```

BASH
```
pip install --upgrade pip setuptools
pip install --upgrade catalyst-sdwan-lab
```

BASH
```
sdwan-lab --version
```


BASH
```
csdwan --version
```

Commands
BASH
```
source <(kubectl completion bash) # setup autocomplete in bash into the current shell, bash-completion package should be installed first.
echo "source <(kubectl completion bash)" >> ~/.bashrc # add autocomplete permanently to your bash shell.
```


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
