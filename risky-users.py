from spotify import dataset

risky_users = 0

for record in dataset:

    skip_rate = float(record["skip_rate"])
    listening_time = int(record["listening_time"])
    free_account = record["subscription_type"]
    offline_listening = int(record["offline_listening"])
    ads_listened_per_week = int(record["ads_listened_per_week"])

    if (skip_rate > 0.30 and listening_time < 100) or (free_account and offline_listening == 0 and ads_listened_per_week > 20):
        risky_users += 1

print(f"{risky_users} users have been identified as at risk.")