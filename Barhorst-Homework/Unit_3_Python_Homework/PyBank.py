# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 20:03:55 2019

@author: EasyE
"""

#import modules
import os
import csv

# Files to Load
csvpath = os.path.join("Resources",'budget_data.csv')

with open(csvpath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Create empty lists to iterate through specific rows for the following variables
    total_months = []
    total_profit = []
    monthly_profit_change = []
 
    # Skip the header labels to iterate with the values
    next(csvreader, None) 

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Specify the file to write to
output_path = os.path.join("Resources",'PyBank_Export.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
#
#    # Initialize csv.writer
     txtwriter = csv.writer(csvfile, delimiter=',')
#
#    # Write the first row (column headers)
     txtwriter.writerow(['Financial Analysis'])
#
#    # Write the line breaker second row
     txtwriter.writerow(['---------------------------------------------'])
#    
#      # Write the financial results
     txtwriter.writerow([(f'Total Months: {len(total_months)}')])
     
      # Write the financial results
     txtwriter.writerow([(f'Total: ${sum(total_profit)}')])
     
      # Write the financial results
     txtwriter.writerow([(f'Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')])
     
      # Write the financial results
     txtwriter.writerow([(f'Greatest Increase: {total_months[max_increase_month]} (${(str(max_increase_value))})')])
     
      # Write the financial results
     txtwriter.writerow([(f'Greatest Decrease: {total_months[max_decrease_month]} (${(str(max_decrease_value))})')])
     

