#!usr/bin/env python
import re
from pprint import pprint

arp_data="""
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
#print (arp_data)
#arp_data=arp_data.strip()
#arp_list=arp_data.splitlines()
#print (arp_list)

IPRegexObject=re.compile(r"\d+\.\d+\.\d+\.\d+")
ip_addr_list=IPRegexObject.findall(arp_data)
MACRegexObject=re.compile(r'\w{4}\.\w{4}\.\w{4}')
mac_list=MACRegexObject.findall(arp_data)
infRegexObject=re.compile(r'Gi\d\/\d\/\d')
inf_list=infRegexObject.findall(arp_data)

print (ip_addr_list)
print (mac_list)
print (inf_list)

arp_dict={}
arp_list=[]

for i in range(5):
    ip=ip_addr_list[i]
    mac=mac_list[i]
    inf=inf_list[i]    
    arp_dict={'ip_addr':ip, 'mac_addr':mac, 'interface':inf}
    arp_list.append(arp_dict)

pprint(arp_list)
