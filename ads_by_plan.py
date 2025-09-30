from spotify import dataset

ads_by_plan = {}
free_users = 0

for record in dataset:
    p = record["subscription_type"]
    ads = int(record["ads_listened_per_week"])

    if p == "Free":
        free_users += 1

    if p not in ads_by_plan.keys():
        ads_by_plan[p] = 0
    
    ads_by_plan[p] += ads

print(f"There are {ads_by_plan['Free']} ads viewed by {free_users} Free users, with an average of {ads_by_plan['Free'] / free_users:.2f} ads per user.")
