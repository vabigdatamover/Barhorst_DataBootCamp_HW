# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:49:05 2019
#PyPoll
@author: Gene Barhorst
"""

import os
import csv

csvpath = os.path.join("Resources",'election_data.csv')

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
##set the output of the text file
##text_path = "output.txt"
# 
#def PollingData(data):
#    voter = int(data[0])
#    county = data[1]
#    canidate = data[2]
#    
#
#    #print(Election Results)
#    #print(--------------------------------)
#    
    # Skip Header  
    next(csvreader, None)
    #print(f"Header: {csvreader}")
    
   
    
# Loop through and print to count the number of voters
    votes = 0
    for row in csvreader:
        votes += 1
    print(f'Total Voters: {votes}')
    
     #print(--------------------------------)
                    
## Loop through print a complete list of candidates who received votes
#    canidate_names = set(canidate)
#    print(f'Total: $ {canidate_names}')
#           
## Loop through and print the percentage and total of votes each candidate won
#    canidate_percentage= dis(canidate_names)*100
#    canidate_total = sum({canidate_name})
#    print(f'{canidate}: {canidate_percentage}% ({canidate_total})')
     
      #print(--------------------------------)
#            
### Loop through and print the winner of the election based on popular vote
##        greatest_decrease = min(value)*100
##        print(f'Greatest Decrease of Profits: {monthes} (${greatest_decrease})')
      
       #print(--------------------------------)
#          
## Specify the file to write to
#output_path = os.path.join("Resources",'PyPoll_Export.csv')
#
## Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:
##
##    # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')
##
##    # Write the first row (column headers)
#     csvwriter.writerow(['Financial Analysis'])
##
##    # Write the line breaker second row
#     csvwriter.writerow(['---------------------------------------------'])
##    
##      # Write the financial results
#     csvwriter.writerow([''])