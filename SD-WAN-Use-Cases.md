### SD-WAN Use Cases 

### Cisco SD-WAN Policy Tree  

<img width="1262" height="897" alt="image" src="https://github.com/user-attachments/assets/461ff64b-e1a8-4d90-b036-9217f4c5461f" />

### Cisco SD-WAN Order of Operations (vedge/cedge)  

<img width="1061" height="537" alt="image" src="https://github.com/user-attachments/assets/b89cee37-1e1f-4aa1-9aa3-7a375879b9b6" />



# Centralized Control Policies :

### 🔘 Use-Case 1 :  Isolating Remote Branches from Each Other  

* Restrict TLOC advertisements from Branch Sites  
* Only DC TLOCs to be advertised to Branch Sites   

--- Approach1 : Traditional Control Policies - (Feature Templates/Device Templates Approach)   
--- Approach2 : Newer Topology Polciies - Topology Workflow Approach (Configuration Groups workflow)    


### 🔘 Use-Case 2 :  Enabling Branch-to-Branch Communication Through Data Centers  

* Through Route Summarization  
* Through TLOC Lists  


--- Summary Routes : Advertise Summary Prefixes from Data Center (DC)   
--- TLOC Lists : Routes advertised through branches should have DC-TLOC as tloc-list  

🔘 Use-Case 3 :  Traffic Engineering at Sites with Multiple Routers  

🔘 Use-Case 4 :  Preferring Regional Data Centers for Internet Access  

🔘 Use-Case 5 :  Regional Mesh Networks  

### 🔘 Use-Case 6 :  Enforcing Security Perimeters with Service Insertion 

* Through Service FW advertisement   

--- Service FW : Advertised from DC cEdge to vSmart and other sites   
  Branch1 traffic will traverse to Branch2 through DC Firewall for inspection...
 

🔘 Use-Case 7 :  Isolating Guest Users from the Corporate WAN  

* VPN Membership policies  


🔘 Use-Case 8 :  Creating Different Network Topologies per Segment  

* MultiTopology Policy

VPN-X : Hub n Spoke Topology  
VPX-Y : Branch to Branch Through DC Topology   

🔘 Use-Case 9 :  Creating Extranets and Access to Shared Services  

* VRF Leaking



# Centralized Data Policies :

🔘 Use-Case 10 :  Direct Internet Access for Guest Users   

🔘 Use-Case 11 :  Direct Cloud Access for Trusted Applications  

🔘 Use-Case 12 :  Application-Based Traffic Engineering  

### 🔘 Use-Case 13 :  Protecting Corporate Users with a Cloud-Delivered Firewall / Secure Internet Gateway  


