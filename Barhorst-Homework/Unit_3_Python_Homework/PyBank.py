# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:47:40 2019
#PyBank
@author: Gene Barhorst
"""

import os
import csv

#Open the CSV
csvpath = os.path.join("Resources",'budget_data.csv')

# Delimit the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
  
    # Skip Header  
    next(csvreader, None)
    
    #Print a header
    print(f'Financial Analysis')
    print(f'--------------------------------') 
    
    # variables
    month = 0
    total = 0
    revenue = []
    previous_revenue = 0
    month_of_change = []
    revenue_change = 0
    greatest_decrease = ["", 9999999]
    greatest_increase = ["", 0]
    revenue_change_list = []
    revenue_average = 0
    for row in csvreader:
# Counts months
        month += 1
# Counts total
        total += int(row[1])
        revenue_change == int(row[1])
        previous_revenue == int(row[1])
        month_of_change = (month, total)
               
#Loop though and calculate the average change in revenue between months over the entire period
        revenue_change = float(row[1]) - previous_revenue
        previous_revenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + ['Date']
        
#The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row[0]
            
#The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row[0]
    revenue_average = round(sum(revenue_change_list)/len(revenue_change_list))
          
        
 # Loop through and print to count the number of months        
    print(f'Total Months: {month}')
# Loop through and print the net total amount of "Profit/Losses" over the entire period     
    print(f'Total: $ {total}')
# Loop through and print the average of the changes in "Profit/Losses" over the entire period   
    print(f'Average Change: $ {revenue_average}')
# Loop through and print the greatest increase in profits (date and amount) over the entire period
    print(f'Greatest Increase of Profits: {greatest_increase[0]} (${greatest_increase[1]})')
# Loop through and print the the greatest decrease in losses (date and amount) over the entire period
    print(f'Greatest Decrease of Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
              
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
     csvwriter.writerow([(f'Total Months: {month}')])
     
      # Write the financial results
     csvwriter.writerow([(f'Total: {total}')])
     
      # Write the financial results
     csvwriter.writerow([(f'Average Change: {revenue_change}')])
     
      # Write the financial results
     csvwriter.writerow([(f'Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})')])
     
      # Write the financial results
     csvwriter.writerow([(f'')])