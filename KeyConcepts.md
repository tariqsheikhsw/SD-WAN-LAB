### Key Concepts 

# Q1 - Feature Template vs Device Template

- Feature Templates
i.e. System , Banner, VPN , VPN Interface Ethernet , OSPF

🔘 C8K-SYSTEM-FT   
🔘 C8K-BANNER-FT   
🔘 C8K-VPN-VPN0-FT    
(TRANSPORT VPN)  
🔘 C8K-VPN-VPN512-FT    
(MANAGEMENT VPN)  
🔘 C8K-VPNINT-VPN0-G1   
(G1 is connected to INTERNET)  
🔘 C8K-VPNINT-VPN0-G2   
(G2 is connected to MPLS)  
🔘 C8K-VPNINT-VPN512-G4   
(G4 is for MGMT access)   
🔘 C8K-OSPF-VPN0   
(OSPF Configuration on G2 interface-MPLS)-Area0  

- Device Templates (and attach to device)  
i.e. add all feature templates

🔘 C8K-DT

# Q2 - VPN0 vs VPN512 vs VPN1 etc.

🔘 VPN0 = Transport VPN 
🔘 VPN512 = Management VPN 
🔘 VPN1 = Data VPN / Service VPN (HQ)


# Q3 - OMP Routes (using Service VPN)
- Overlay  

# Q4 - Devices
🔘 vEdge
🔘 cEdge 
🔘 CSR1000v

# Q5- Export/Import/Backup Configuration 

request nms configuration-db backup path /opt/data/backup/Config-Backup-01

# Q6 - Application Aware Routing (AAR) 







