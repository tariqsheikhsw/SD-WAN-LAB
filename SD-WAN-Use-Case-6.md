### 🔘 Use-Case 6 : Enforcing Security Perimeters with Service Insertion

    Through Service FW advertisement

--- Service FW : Advertised from DC cEdge to vSmart and other sites...  
Branch1 traffic will traverse to Branch2 through DC Firewall for inspection...


### SERVICE FIREWALL TOPOLOGY 

Using Cisco ASA firewall ... 


<img width="827" height="712" alt="image" src="https://github.com/user-attachments/assets/5eea0b71-9672-4726-a149-4bf6fb1b6623" />


<img width="1568" height="522" alt="image" src="https://github.com/user-attachments/assets/7f40529f-a7f7-49c1-a66b-3ebb3d32bc65" />




### SERVICE FIREWALL 

<img width="653" height="121" alt="image" src="https://github.com/user-attachments/assets/6fa157e2-41a1-4520-92d8-8c51c124a6dc" />

<img width="1192" height="546" alt="image" src="https://github.com/user-attachments/assets/113daf87-6e55-4041-8ced-ddda54852693" />


### Verification on vSmart 

<img width="1132" height="415" alt="image" src="https://github.com/user-attachments/assets/360675dc-504f-4d8a-83d9-be342164e79b" />


### Centralized Policies Configuration 

<img width="1853" height="617" alt="image" src="https://github.com/user-attachments/assets/56ddaf83-97e1-418c-b32f-33b7655f0772" />

<img width="1622" height="637" alt="image" src="https://github.com/user-attachments/assets/bfc67811-cb7a-4ecb-8051-7e021d17bb2b" />

<img width="1847" height="566" alt="image" src="https://github.com/user-attachments/assets/ba8dfdac-a196-4815-899a-5018e0b06c00" />

<img width="1837" height="716" alt="image" src="https://github.com/user-attachments/assets/966ebfb9-3f68-41e2-b9fa-00b561c7a741" />


### POLICY CHANGES 

```
86	  policy
87	   lists
88	    site-list Hub-Site
89	     site-id 100
90	    !
91	    site-list Spokes-Site
92	     site-id 1001-1003
93	    !
94	    prefix-list _AnyIpv4PrefixList
95	     ip-prefix 0.0.0.0/0 le 32
96	    !
97	   !
98	   control-policy Branches_Policy_with_FW
99	    sequence 1
100	     match tloc
101	      site-list Hub-Site
102	     !
103	     action accept
104	     !
105	    !
106	    sequence 11
107	     match route
108	      prefix-list _AnyIpv4PrefixList
109	      site-list   Hub-Site
110	     !
111	     action accept
112	     !
113	    !
114	    sequence 21
115	     match route
116	      prefix-list _AnyIpv4PrefixList
117	      site-list   Spokes-Site
118	     !
119	     action accept
120	      set
121	       service FW
122	      !
123	     !
124	    !
125	    default-action reject
126	   !
127	  !
128	  apply-policy
129	   site-list Spokes-Site
130	    control-policy Branches_Policy_with_FW out
131	   !
132	  !
```

<img width="953" height="526" alt="image" src="https://github.com/user-attachments/assets/7136b007-1c81-4353-9089-1f6b9deb25b8" />


### VERFICATON 

BEFORE AND AFTER on BR1 and BR2 Devices

#ping vrf 1 10.10.22.1   
#traceroute vrf 1 10.10.22.1   


#ping vrf 1 10.10.21.1   
#traceroute vrf 1 10.10.21.1  
  
