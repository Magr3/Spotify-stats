from spotify import dataset

while True:
    try:
        id_value = int(input("choose user ID: "))
        break
    except ValueError:
        print("Invalid input: please enter a valid integer number")

for record in dataset:
    if id_value == int(record["user_id"]):
        print(f"--- User Summary (ID: {record["user_id"]}) ---")
        print(f"Gender:               {record["gender"]}")
        print(f"Age:                  {record["age"]} years")
        print(f"Country:              {record["country"]}")
        print(f"Subscription Type:    {record["subscription_type"]}")
        print(f"Listening Time:       {record["listening_time"]} hours per week")
        print(f"Songs Played/Day:     {record["songs_played_per_day"]}")
        print(f"Skip Rate:            {float(record["skip_rate"]) * 100:.1f}%")
        print(f"Device Type:          {record["device_type"]}")
        print(f"Ads Listened/Week:    {record["ads_listened_per_week"]}")
        print(f"Offline Listening:    {record["offline_listening"]}")
        print(f"Churned:              {bool(int(record["is_churned"]))}")
        print(f"-------------------------------")