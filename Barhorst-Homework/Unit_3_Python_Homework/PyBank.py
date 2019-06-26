# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:47:40 2019
#PyBank
@author: Gene Barhorst
"""

import os
import csv

csvpath = os.path.join("Resources",'budget_data.csv')

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#set the output of the text file
#text_path = "output.txt"
    
    print(f'Financial Analysis')
    print(f'--------------------------------')  
 
def BankData(data):
    monthes = data[0]
    values = int(data[1])
    
    # Skip Header  
    next(csvreader, None)
    #print(f"Header: {csvreader}")
      
# Loop through and print to count the number of months
    month = 0
    for row in csvreader:
        month += 1
    print(f'Total Months: {month}')
                    
# Loop through print the net total amount of "Profit/Losses" over the entire period
    profit_losses = sum(values)*100
    print(f'Total: $ {profit_losses}%')
           
# Loop through and print the average of the changes in "Profit/Losses" over the entire period
    average_change = values.mean()*100
    print(f'Average Change: $ {average_change}')
            
# Loop through and print the greatest increase in profits (date and amount) over the entire period

    greatest_increase = max(values)*100
    print(f'Greatest Increase: {monthes} (${greatest_increase})')
            
# Loop through and print the the greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(values)*100
    print(f'Greatest Decrease of Profits: {monthes} (${greatest_decrease})')
          
# Specify the file to write to
output_path = os.path.join("Resources",'PyBank_Export.csv')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
#
#    # Initialize csv.writer
     csvwriter = csv.writer(csvfile, delimiter=',')
#
#    # Write the first row (column headers)
     csvwriter.writerow(['Financial Analysis'])
#
#    # Write the line breaker second row
     csvwriter.writerow(['---------------------------------------------'])
#    
#      # Write the financial results
     csvwriter.writerow([''])