from spotify import dataset

r1 = r2 = r3 = r4 = 0

for record in dataset:
    age = int(record["age"])

    if age < 20:
        r1 += 1
    elif age <= 35:
        r2 += 1
    elif age <= 50 :
        r3 += 1
    else:
        r4 += 1
    
print(f"Users age is less than 20: {r1}\n"
      f"Users age is between 20 and 35: {r2}\n"
      f"Users age is between 36 and 50: {r3}\n"
      f"Users age is more than 50: {r4}"
      )
   