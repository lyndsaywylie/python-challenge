import os
import csv

csv_reader = os.path.join("Resources", "budget_data.csv")

# Lists to store data 
date = []
profitloss = []
monthly_changes = []
unique_count = 0
total_profit = 0
profit_changes = 0
begin_profit = 0

with open(csv_reader, newline="") as csv_file:
    budgetdata = csv.reader(csv_file, delimiter=",")
    cvs_header = next(budgetdata)

    for row in budgetdata:
      unique_count = unique_count +1
      date.append(row[0])
      profitloss.append(row[1])

      total_profit = total_profit + int(row[1])

      final_profit = int(row[1])
      m_profit_changes = final_profit - begin_profit
      monthly_changes.append(m_profit_changes)
      total_profit = total_profit + m_profit_changes

      average_profits = (total_profit/unique_count) 


      greatest_increase = max(monthly_changes)
      greatest_decrease = min(monthly_changes)
      increase_date = date[monthly_changes.index(greatest_increase)]
      decrease_date = date[monthly_changes.index(greatest_decrease)]

print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(unique_count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease)+ ")")
print("----------------------------------------------------------")


with open('analysis.txt', 'w') as text:  
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(unique_count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")
