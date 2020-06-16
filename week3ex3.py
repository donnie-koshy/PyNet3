#! usr/bin/env python

import json
from pprint import pprint

with open("nxos.json") as f:
    json_data=json.load(f)

pprint (json_data)

ipv4_list=[]
ipv6_list=[]
intf_list=[]

print("\n"+str(len(json_data)))

for intf,ip_set in json_data.items():
    intf_list.append(intf)
    for label,address in ip_set.items():
        for ip,prefix in address.items():
            prefix_length=prefix['prefix_length']        
            if label=='ipv4':
                ipv4_list.append("{}/{}".format(ip,prefix_length))
            else:
                ipv6_list.append("{}/{}".format(ip,prefix_length))


print (intf_list)
print("\n")
print (ipv4_list)
print("\n")  
print(ipv6_list)
