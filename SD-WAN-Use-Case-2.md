🔘 Use-Case 2 :  Enabling Branch-to-Branch Communication Through Data Centers  

* Through Route Summarization  
* Through TLOC Lists  


--- Summary Routes : Advertise Summary Prefixes from Data Center (DC)   
--- TLOC Lists : Routes advertised through branches should have DC-TLOC as tloc-list  

### TLOC LIST 

### BEFORE APPLYING CENTRALIZED POLICY : Direct Tunnel

<img width="1757" height="492" alt="image" src="https://github.com/user-attachments/assets/82f8ff29-ddb1-40ed-849c-ac072e0b0530" />

<img width="1225" height="238" alt="image" src="https://github.com/user-attachments/assets/06013eca-695b-490e-b0a7-42820760b36a" />


<img width="1702" height="568" alt="image" src="https://github.com/user-attachments/assets/e5bef249-8d58-4911-91c2-3fb0da04d70c" />

<img width="1105" height="238" alt="image" src="https://github.com/user-attachments/assets/3b9e36a7-310b-4511-a716-7b215e0a4b79" />

### POLICY CHANGES 

```
86	  policy
87	   lists
88	    tloc-list DC_TLOCS
89	     tloc 10.10.1.11 color mpls encap ipsec
90	     tloc 10.10.1.11 color public-internet encap ipsec
91	    !
92	    site-list Hub-Site
93	     site-id 100
94	    !
95	    site-list Spokes-Site
96	     site-id 1001-1003
97	    !
98	    prefix-list _AnyIpv4PrefixList
99	     ip-prefix 0.0.0.0/0 le 32
100	    !
101	   !
102	   control-policy Hub_n_Spoke_Policy_TLOC_Lists
103	    sequence 1
104	     match tloc
105	      site-list Hub-Site
106	     !
107	     action accept
108	     !
109	    !
110	    sequence 11
111	     match route
112	      prefix-list _AnyIpv4PrefixList
113	      site-list   Hub-Site
114	     !
115	     action accept
116	     !
117	    !
118	    sequence 21
119	     match route
120	      prefix-list _AnyIpv4PrefixList
121	      site-list   Spokes-Site
122	     !
123	     action accept
124	      set
125	       tloc-list DC_TLOCS
126	      !
127	     !
128	    !
129	    default-action reject
130	   !
131	  !
132	  apply-policy
133	   site-list Spokes-Site
134	    control-policy Hub_n_Spoke_Policy_TLOC_Lists out
135	   !
136	  !
```


### AFTER APPLYING CENTRALIZED POLICY : Modified TLOC LIST 

<img width="1743" height="738" alt="image" src="https://github.com/user-attachments/assets/2ac64c7e-ba9f-45e7-b823-0cc42b5a7aa1" />

<img width="1731" height="817" alt="image" src="https://github.com/user-attachments/assets/37d6dd0f-5cc3-4d31-a8cf-cc4e093d913b" />



### STEPS : CUSTOM CONTROL POLICY with TRADITIONAL Workflow 

1) Define TLOC List  
2) Create Centralized Policy 
- Custom Control (Route & TLOC)
  Control Policy (Route / TLOC)

Centralized_Policy_v2
 -> Topology : Hub_n_Spoke_Policy_TLOC_Lists

<img width="1632" height="647" alt="image" src="https://github.com/user-attachments/assets/9d291990-c4b7-4841-87b1-6ded9bf9096d" />

<img width="1807" height="572" alt="image" src="https://github.com/user-attachments/assets/9be82ee9-d727-4a08-a767-4bcd10248ab2" />

<img width="1465" height="432" alt="image" src="https://github.com/user-attachments/assets/2f4a509b-c1a4-4626-9e8e-11f39d74923c" />

<img width="1681" height="757" alt="image" src="https://github.com/user-attachments/assets/c7226df4-c8d6-4175-8713-4688d1f5e88c" />

<img width="1585" height="622" alt="image" src="https://github.com/user-attachments/assets/4d86c4c1-9085-43c7-8e91-949b7e092a60" />

