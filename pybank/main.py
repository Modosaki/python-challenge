import os
import csv
#import pandas as pd
totalMonth=0
total=0
budget_csv = os.path.join("..", "Resources", "budget_data.csv")
totalrow=0
change=0
avg_chgelist=[]
dates=[]

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
        dates.append(row[0])

#print(avg_chgelist.index(min(avg_chgelist)))
mindate=(dates[(avg_chgelist.index(min(avg_chgelist)))])
maxdate=(dates[(avg_chgelist.index(max(avg_chgelist)))])
del avg_chgelist[0]
avgchange = round((sum(avg_chgelist)/len(avg_chgelist)),2)
with open("Output.txt", "w") as text_file:
    print("Financial Analysis",file=text_file)
    print("----------------------------",file=text_file)
    print(f"Total Months: {str(totalMonth)}",file=text_file)
    print(f"Total: ${str(total)}",file=text_file)
    print(f"Average  Change: ${str(avgchange)}",file=text_file)
    print(f"Greatest Increase in Profits:{maxdate} $({(max(avg_chgelist))})",file=text_file)
    print(f"Greatest Increase in Profits:{mindate} $({(min(avg_chgelist))})",file=text_file)


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(totalMonth)}")
print(f"Total: ${str(total)}")
print(f"Average  Change: ${str(avgchange)}")
print(f"Greatest Increase in Profits:{maxdate} $({(max(avg_chgelist))})")
print(f"Greatest Increase in Profits:{mindate} $({(min(avg_chgelist))})")





#def getStats(moneyData):

    # # Total matches can be./ found by adding wins, losses, and draws together
    # totalMonths = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])

    # # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    # total = (int(wrestlerData[1]) / totalMatches) * 100

    # # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    # AvgChange = (int(wrestlerData[2]) / totalMatches) * 100

    # # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    # GreatestInc = (int(wrestlerData[3]) / totalMatches) * 100

    # GreatestDec = (int(wrestlerData[3]) / totalMatches) * 100

    # # If the loss percentage is over 50, typeOfWrestler is "Jobber". Otherwise it is "Superstar".
    # if(lossPercent > 50):
    #     typeOfWrestler = "Jobber" 
    #     typeOfWrestler = "Superstar"

    # # Print out the wrestler's name and their percentage stats
    # print(f"Stats for {wrestlerData[0]}")
    # print(f"WIN PERCENT: {str(winPercent)}")
    # print(f"LOSS PERCENT: {str(lossPercent)}")
    # print(f"DRAW PERCENT: {str(drawPercent)}")
#qualities = [float(item[-1]) for item in wines[1:]]

#sum(qualities) / len(qualities)
#with open(budget_csv, 'r') as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
  #  month = list(csv.reader(csvfile,delimiter=",")
