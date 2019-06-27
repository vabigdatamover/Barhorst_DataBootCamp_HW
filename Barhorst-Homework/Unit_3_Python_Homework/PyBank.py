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
  
    # Skip Header  
    next(csvreader, None)
    #print(f"Header: {csvreader}")
    
    print(f'Financial Analysis')
    print(f'--------------------------------') 
    
    # Loop through and print to count the number of months
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
        month += 1
        total += int(row[1])
        revenue_change += int(row[1])
        
        
#        if month % 2 =! 0:
#            #SAVE THIS VALUE AS odd_row_value
#        else:
#            #SUBTRACT THIS ROW VALUE FROM odd_row_value
#            #put that difference in differences
        
#Loop though and calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row['Profit/Losses'])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]
        
#The greatest increase in revenue (date and amount) over the entire period
      
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']
            
#The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)
          
        
 # Loop through and print to count the number of months        
    print(f'Total Months: {month}')
# Loop through and print the net total amount of "Profit/Losses" over the entire period     
    print(f'Total: $ {total}')
# Loop through and print the average of the changes in "Profit/Losses" over the entire period   
    print(f'Average Change: $ {revenue_average}')
# Loop through and print the greatest increase in profits (date and amount) over the entire period
    print(f'Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})')
# Loop through and print the the greatest decrease in losses (date and amount) over the entire period
    print(f'Greatest Decrease of Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')
    
    
    
    

#set the output of the text file
#text_path = "output.txt"
        
    
#def BankData(data):
#    monthes = data[0]
#    values = int(data[1])
#    

                    
## Loop through print the net total amount of "Profit/Losses" over the entire period
#    profit_losses = sum(values)*100
#    print(f'Total: $ {profit_losses}%')
           
# Loop through and print the average of the changes in "Profit/Losses" over the entire period
#    average_change = values.mean()*100
#    print(f'Average Change: $ {average_change}')
            
# Loop through and print the greatest increase in profits (date and amount) over the entire period

#    greatest_increase = max(values)*100
#    print(f'Greatest Increase: {monthes} (${greatest_increase})')
#            
# Loop through and print the the greatest decrease in losses (date and amount) over the entire period
#    greatest_decrease = min(values)*100
#    print(f'Greatest Decrease of Profits: {monthes} (${greatest_decrease})')
    
#    return 
          
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
     #csvwriter.writerow([(f'Average Change: {average_change}')])
     
      # Write the financial results
     #csvwriter.writerow([(f'Greatest Increase: {monthes} (${greatest_increase}')])
     
      # Write the financial results
     #csvwriter.writerow([(f'Greatest Decrease of Profits: {monthes} (${greatest_decrease})')])