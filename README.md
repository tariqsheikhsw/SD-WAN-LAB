# SD-WAN-LAB
SD-WAN LAB

# Cisco SD-WAN Lab Setup (using CML) 

Here's the summary of activities performed during this lab :

🔘 CML Setup   
🔘 WSL - Ubuntu 

# Scenario / Architecture


Commands
BASH
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


FINAL STATUS:

    [✔️] PVC to PV binding
    [✔️] Image Scanning using Aquasec Trivy
    [✔️] Ingress and Egress Network Policy Implementation
    [✔️] Secure Deployment using AppArmor Profile
    [✔️] Expose Deployment with NodePort Type Service



