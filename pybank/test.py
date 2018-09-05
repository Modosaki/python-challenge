import os
import csv

totalMonth=0
total=0
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
totalrow=0
change=0
avg_chgelist=[]

with open(budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    

    
    

    for row in csvreader:
        totalMonth = totalMonth + 1
        totalrow=int(row[1])
        total= int(total+totalrow)
        change=int(row[1])-change
        avg_chgelist.append(change)
        change=int(row[1])


print(sum(avg_chgelist)/len(avg_chgelist))
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalMonth)}")
print(f"Total: ${str(total)}") 