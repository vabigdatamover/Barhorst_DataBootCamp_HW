# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:47:40 2019
#PyBank
@author: Gene Barhorst
"""

import os
import csv

csvpath = os.path.join("../Resources", "budget_data.csv")
csvpath = os.path.join(r"C:\Users\EasyE\Desktop\Unit_3_Python\Resources")
csvpath = os.path.join(r"C:\Users\EasyE\Barhorst_DataBootCamp_HW\Barhorst-Homework\Unit_3_Python_Homework\Resources")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
#set the output of the text file
#text_path = "output.txt"
 

     #print(Financial Analysis)
     #print(--------------------------------)
    
    # Skip Header  
    next(csvreader, None)
    #print(f"Header: {csvreader}")
    
   
    
    # Loop through and print to count the number of months
    for row in csvreader:
        print(f'Total Months: (len(row[0]))')
                    
      # Loop through print the net total amount of "Profit/Losses" over the entire period
    for row in csvreader: 
        print(f'Total: $ (sum(row[1]))')
                     
            
       # Loop through and print the average of the changes in "Profit/Losses" over the entire period
    for row in csvreader:
       print(f'Average Change: $ (avg(row[1]))')
            
        # Loop through and print the greatest increase in profits (date and amount) over the entire period
    for row in csvreader:
        print(f'Greatest Increase of Profits: $ (max(row[1]))')
            
         # Loop through and print the the greatest decrease in losses (date and amount) over the entire period
    for row in csvreader:
        print(f'Greatest Decrease of Profits: $ (min(row[1]))')
    
    
    #for row in csvreader:
       # if float(row[7]) >= 5:
            #print(row[0] + " contains 5 grams of fiber ")
            #print(row[0] + " has " + row[7] + " grams of fiber")
            
# Specify the file to write to
output_path = os.path.join("..", "output", "PyBankResults.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])

    # Write the line breaker second row
    csvwriter.writerow(['---------------------------------------------'])
    
      # Write the financial results
    csvwriter.writerow([''])