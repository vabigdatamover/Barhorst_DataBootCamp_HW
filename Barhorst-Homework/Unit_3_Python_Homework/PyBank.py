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
    differences = []
    odd_row_value = 0
    even_row_value = 0
    for row in csvreader:
        month += 1
        total += int(row[1])
#        if month % 2 =! 0:
#            #SAVE THIS VALUE AS odd_row_value
#        else:
#            #SUBTRACT THIS ROW VALUE FROM odd_row_value
#            #put that difference in differences
#            
        
 # Loop through and print to count the number of months        
    print(f'Total Months: {month}')
# Loop through print the net total amount of "Profit/Losses" over the entire period     
    print(f'Total: $ {total}')
# Loop through and print the average of the changes in "Profit/Losses" over the entire period   
    #average_change = month.mean()*100
    #print(f'Average Change: $ {sum(total)}')
    
    

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
     csvwriter.writerow([''])