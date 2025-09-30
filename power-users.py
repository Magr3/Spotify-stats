from spotify import dataset

powers_users = 0

for record in dataset:
    if int(record["listening_time"]) > 200 and int(record["songs_played_per_day"]) > 50:
        powers_users += 1

print(f"we have {powers_users} power users")

