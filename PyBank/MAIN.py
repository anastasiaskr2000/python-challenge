import os
import csv

file_to_open = os.path.join('Resources', 'budget_data.csv')
#print(file_to_open)

text_path = os.path.join("Analysis","financial_analysis.txt")

total_months = 0
net_total = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]
revenue_change_list = []
revenue_average = 0

with open(file_to_open) as csvfile:
# code here
    csvreader = csv.reader(csvfile)
# skip the header row
    header = next(csvreader)
# print(header)
    for row in csvreader:
        print(row)
        total_months = total_months + 1
        net_total = net_total + int(row[1])
        if total_months>1:
            revenue_change = float(row[1])- previous_revenue
            revenue_change_list = revenue_change_list + [revenue_change]
        previous_revenue = float(row[1])
        month_of_change = [month_of_change] + [row[0]]

        if revenue_change>greatest_increase[1]:
            greatest_increase[1]=revenue_change
            greatest_increase[0]=row[0]

        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]=revenue_change
            greatest_decrease[0]=row[0]
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

# Print calculations to terminal

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: $", {net_total})
print(f"Average Change: ${revenue_average:.2f}") 
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print Calculations to txt
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Net Total: ${net_total}\n")
    file.write(f"Average Change: ${revenue_average:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
