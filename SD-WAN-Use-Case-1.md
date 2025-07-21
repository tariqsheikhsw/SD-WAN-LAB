🔘 Use-Case 1 : Isolating Remote Branches from Each Other
- Restrict TLOC advertisements from Branch Sites
- Only DC TLOCs to be advertised to Branch Sites

--- Approach1 : Traditional Control Policies - (Feature Templates/Device Templates Approach)
--- Approach2 : Newer Topology Polciies - Topology Workflow Approach (Configuration Groups workflow)

### SITE-1

<img width="1006" height="306" alt="image" src="https://github.com/user-attachments/assets/964eca9a-eeef-4c53-9ce7-ac087556b632" />


<img width="892" height="376" alt="image" src="https://github.com/user-attachments/assets/2d474d8e-bd27-48d9-8b50-7d2dcbba3122" />
<img width="1683" height="556" alt="image" src="https://github.com/user-attachments/assets/fd5641f8-4e5c-4426-b7ad-dc8900ac3166" />


### SITE-2

<img width="960" height="302" alt="image" src="https://github.com/user-attachments/assets/7bab80fe-7046-4437-ba50-4b74f97f4551" />

<img width="772" height="387" alt="image" src="https://github.com/user-attachments/assets/6c894fb5-0cd2-405d-900a-b44b5b87c2b8" />
<img width="1673" height="566" alt="image" src="https://github.com/user-attachments/assets/a7bed01e-22cf-4a0b-9a55-fafbaa9ef212" />



### BEFORE APPLYING CENTRALIZED POLICY : Direct Tunnel

<img width="962" height="257" alt="image" src="https://github.com/user-attachments/assets/e8c4f67d-970e-4605-ba36-182e1df059f1" />

<img width="812" height="253" alt="image" src="https://github.com/user-attachments/assets/6dea630a-74a1-48c9-a7e1-4d6619e9f3d5" />



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
98	   control-policy Hub_n_Spoke_Policy
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
114	    default-action reject
115	   !
116	  !
117	  apply-policy
118	   site-list Spokes-Site
119	    control-policy Hub_n_Spoke_Policy out
120	   !
121	  !
```
### AFTER APPLYING CENTRALIZED POLICY : Traffic Routed Through DC 

<img width="563" height="126" alt="image" src="https://github.com/user-attachments/assets/1a48e015-69b4-4e32-9761-f953469e8ff0" />


<img width="681" height="153" alt="image" src="https://github.com/user-attachments/assets/39bef050-eebc-47b0-bd4f-e3c786f6fccb" />

