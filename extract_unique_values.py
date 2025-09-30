from spotify import dataset

countrys = set()
subscriptions = set()
devices = set()

for record in dataset:
    countrys.add(record["country"])
    subscriptions.add(record["subscription_type"])
    devices.add(record["device_type"])

print(countrys)
print(subscriptions)
print(devices)