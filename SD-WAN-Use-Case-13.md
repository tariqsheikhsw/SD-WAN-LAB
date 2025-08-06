
<img width="1788" height="686" alt="image" src="https://github.com/user-attachments/assets/45abb1e0-f783-43f7-853d-056fa64f6e53" />

### Centralized Data Policies :

### 🔘 Use-Case 13 : Protecting Corporate Users with a Cloud-Delivered Firewall / Secure Internet Gateway (Umbrella / Zscaler)

Building on previous Use-Case :
### Use-Case 10 : Direct Internet Access for Guest Users

- Service Route steers all traffic to SIG
- Use Centralized Data Policies to steer certain Application Traffic to SIG 

<img width="593" height="347" alt="image" src="https://github.com/user-attachments/assets/4c26fbae-42a5-46fd-a0a4-0e803c3e0716" />

# Configure SIG Feature Tempalte and Attach it to the Device Template 

<img width="726" height="264" alt="image" src="https://github.com/user-attachments/assets/d1b45aa5-4b01-4a1d-ae05-4e9b7ed16ebc" />

# Configure SIG Credentials and Attached it to the Device Tempalte 

<img width="693" height="70" alt="image" src="https://github.com/user-attachments/assets/5461db54-1609-44f2-a082-32956db286be" />


# Cisco Umbrella Dashboard 

- Ensure Network Tunnels are established from Branch SD-WAN device to Cisco Umbrella 

Deployments -> Core Identities -> Network Tunnels 

<img width="1849" height="567" alt="image" src="https://github.com/user-attachments/assets/8e3e1716-0ca1-4bbe-89d2-63d4373f916d" />

# Centralized Data Policy Configuration 
- Traffic Data
- i.e. Facebook/M365 traffic goes through Umbrella SIG , while GuestUsers Traffic goes to internet directly via NAT (Direct Internet Access-DIA) 

<img width="1906" height="718" alt="image" src="https://github.com/user-attachments/assets/bb339b25-5901-4bbe-ab1c-c09c22c04866" />

- Full Policy 

<img width="1904" height="753" alt="image" src="https://github.com/user-attachments/assets/412185dd-d430-4a91-8cbd-fa44c04bd308" />

- Cisco Umbrella Web Policy (applied to tunnels to restrict access)

<img width="1777" height="989" alt="image" src="https://github.com/user-attachments/assets/c1dd1f05-c30e-4ec2-be62-22d806a24b8a" />

- Reporting -> Core Reports -> Activity Search

<img width="1863" height="495" alt="image" src="https://github.com/user-attachments/assets/2523a0b3-27df-4246-b936-ac40896fe136" />


