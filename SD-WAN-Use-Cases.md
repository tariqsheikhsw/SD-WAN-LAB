### SD-WAN Use Cases 

# Centralized Control Policies :

🔘 Use-Case 1 :  Isolating Remote Branches from Each Other  

* Restrict TLOC advertisements from Branch Sites  
* Only DC TLOCs to be advertised to Branch Sites   

--- Approach1 : Traditional Control Policies - (Feature Templates/Device Templates Approach)   
--- Approach2 : Newer Topology Polciies - Topology Workflow Approach (Configuration Groups workflow)    


🔘 Use-Case 2 :  Enabling Branch-to-Branch Communication Through Data Centers  

* Through Route Summarization  
* Through TLOC Lists  


--- Summary Routes : Advertise Summary Prefixes from Data Center (DC) 
--- TLOC Lists : Routes advertised through branches should have DC-TLOC as tloc-list  

🔘 Use-Case 3 :  Traffic Engineering at Sites with Multiple Routers  

🔘 Use-Case 4 :  Preferring Regional Data Centers for Internet Access  

🔘 Use-Case 5 :  Regional Mesh Networks  

🔘 Use-Case 6 :  Enforcing Security Perimeters with Service Insertion  

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

🔘 Use-Case 13 :  Protecting Corporate Users with a Cloud-Delivered Firewall


