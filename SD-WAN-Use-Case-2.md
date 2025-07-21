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
