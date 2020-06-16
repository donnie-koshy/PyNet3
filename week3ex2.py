#!usr/bin/env python
#Program to demonstrate how to export data to YAML file

import yaml

pydevice=[
{'device_name':'cisco3','host':'cisco3.lasthop.io','username':'user','password':'pass'},
{'device_name':'cisco4','host':'cisco4.lasthop.io','username':'user','password':'pass'},
{'device_name':'arista1','host':'arista1.lasthop.io','username':'user','password':'pass'},
{'device_name':'arista2','host':'arista2.lasthop.io','username':'user','password':'pass'}
]

with open("py_to_yaml.yml",'w') as f:
    yaml.dump(pydevice,f,default_flow_style=False)

