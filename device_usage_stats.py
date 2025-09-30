from spotify import dataset
import json

devices = {}


for record in dataset:
    c = record["country"]
    d = record["device_type"]

    if c not in devices.keys():
        devices[c] = {
            "Desktop": 0,
            "Web": 0,
            "Mobile": 0
        }


    devices[c][d] +=1

print(json.dumps(devices, indent=2))