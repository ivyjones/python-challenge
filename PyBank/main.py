import os
import csv

budget_data = os.path.join(".", "Resources", "budget_data.csv")

#declare variables
total_months=[]
total_profits=[]
change=[]
greatest_increase=0
greatest_increase_month=""
greatest_decrease=0
greatest_decrease_month=""



#open csv file
with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_reader=next(csvreader)

    #read through every row after header
    for row in csvreader:
        total_months.append(row[0])
        total_profits.append(row[1])

    #print
    print("Financial Analysis")
    print("----------------------------")
    #total number of months included in the dataset
    print("Total Months: " + str(len(total_months)))

    #net total amount of "Profit/Losses" over the entire period
    total_profits=[int(x) for x in total_profits]
    total_profits_sum=sum(total_profits)
    print("Total: $" + str(total_profits_sum))

    #changes in "Profit/Losses" over the entire period
    for i in range(len(total_profits)-1):
        change.append(total_profits[i+1]-total_profits[i])
        
        if (greatest_increase < change[i]) :
            greatest_increase = change[i]
            greatest_increase_month=total_months[i+1]


        if (greatest_decrease > change[i]):
            greatest_decrease=change[i]
            greatest_decrease_month=total_months[i+1]
    
    #the average of those changes
    average=sum(change)/len(change)
    print("Average Change: $" + str(average))

    #The greatest increase in profits (date and amount) over the entire period
    #greatest_increase=max(total_profits)
    print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")")

    #The greatest decrease in profits (date and amount) over the entire period
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")")
   
#export results to analysis folder
f=open("./analysis/pybank_analysis.txt", "w")
print("Financial Analysis", file=f)
print("----------------------------", file=f)
print("Total Months: " + str(len(total_months)), file=f)
print("Total: $" + str(total_profits_sum), file=f)
print("Average Change: $" + str(average), file=f)
print("Greatest Increase in Profits: " + str(greatest_increase_month) + " ($" + str(greatest_increase) + ")", file=f)
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) + " ($" + str(greatest_decrease) + ")", file=f)
f.close()






