# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 18:49:05 2019
#PyPoll
@author: Gene Barhorst
"""

import os
import csv

#Open the CSV
csvpath = os.path.join("Resources",'election_data.csv')

#Delimit the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        
    # Skip CSV Header  
    next(csvreader, None)

#Creates an emptyt list for candidate names
    poll = {}       
#creates a list
    total_votes = 0

    for row in csvreader:
        total_votes += 1
        if row[2] in poll:
            poll[row[2]] += 1
        else:
            poll[row[2]] = 1
    
# creates variables
vote_percent = {}
max_vote_percent = 0
winning_candidate = ''
message = ''
for candidate in poll:
    candidate_votes = poll[candidate]
    candidate_vote_percent = round((candidate_votes / total_votes)*100, 3)
    vote_percent[candidate] = [candidate_vote_percent, candidate_votes]
    if candidate_vote_percent > max_vote_percent:
        winning_candidate = candidate 
        max_vote_percent = candidate_vote_percent
 
     
## Creates a message
    
    message += f'{candidate}: {candidate_vote_percent}% ({candidate_votes})\n'
#Output message
output = (
        'Election Results\n'
        '--------------------------------\n'
        f'Total Voters: {total_votes}\n'
        '--------------------------------\n'
        f'{message}'
        '--------------------------------\n'
        f'Winner:  {winning_candidate}'
        )

#Prints the output
print(output)
          
# Specify the file to write to
output_path = os.path.join("Resources",'PyPoll_Export.txt')

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    # Output the text file
     txtfile.write(output)