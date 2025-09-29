from spotify import dataset

churners = 0
total_user = 0

free_churners = premium_churners = family_churners = student_churners  = 0


for record in dataset:
    total_user += 1
    if bool(int(record["is_churned"])):
        churners += 1
        match record["subscription_type"]:
            case "Free":
                free_churners += 1
            case "Premium":
                premium_churners += 1
            case  "Family":
                family_churners += 1
            case "Student":
                student_churners += 1
        

churn_percentage = (churners/total_user)*100

print(f"We have {total_user} and {churners} are churners\n"
      f"it's { churn_percentage :.0f}%\n"   
      f"Free subscription churners {free_churners}\n"  
      f"Premium subscription churners {premium_churners}\n" 
      f"Family subscription churners {family_churners}\n" 
      f"Student subscription churners {student_churners}"  
    )

