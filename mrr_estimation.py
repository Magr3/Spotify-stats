from spotify import dataset
import json

PRICES = {"Free": 0.0, "Premium": 9.99, "Family": 14.99,
"Student": 4.99}

mrr_by_plan_country = {}

for record in dataset:
    c = record["country"]
    p = record["subscription_type"]
    if bool(int(record["is_churned"])):
        continue
    if c not in mrr_by_plan_country.keys():
        mrr_by_plan_country[c] = {
            k: 0 for k in PRICES.keys() 
        }
    
    mrr_by_plan_country[c][p] += PRICES[p]
    mrr_by_plan_country[c][p] = round(mrr_by_plan_country[c][p], 2) 

print(json.dumps(mrr_by_plan_country, indent=2))