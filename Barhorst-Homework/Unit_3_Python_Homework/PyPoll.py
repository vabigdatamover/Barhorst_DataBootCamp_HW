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
    
    #Print a header
    print(f'Election Results')
    print(f'--------------------------------')
    
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
            
#Prints out total voters
    print(f'Total Voters: {total_votes}')
    print(f'--------------------------------')
    
# creates vote percent list
# creates winner_list to put winners (even if there is a tie)
vote_percent = {}
max_vote_percent = 0
winning_candidate = ''
for candidate in poll:
    candidate_votes = poll[candidate]
    candidate_vote_percent = round((candidate_votes / total_votes)*100, 3)
    vote_percent[candidate] = [candidate_vote_percent, candidate_votes]
    if candidate_vote_percent > max_vote_percent:
        winning_candidate = candidate 
        max_vote_percent = candidate_vote_percent
 
     
## Loop through print a complete list of candidates who received votes
    print(f'{candidate}: {candidate_vote_percent}% ({candidate_votes}) ') 
#prints a winner_list to show winners (even if there is a tie)
else:
    print(f'--------------------------------')
    
    print(f'Winner:  {winning_candidate}')  
    


          
# Specify the file to write to
output_path = os.path.join("Resources",'PyPoll_Export.txt')

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    # Initialize csv.writer
     txtwriter = csv.writer(txtfile, delimiter=',')
     
    # Write Election Results 
     txtwriter.writerow(['Election Results'])

   # Write the line breaker first formula
     txtwriter.writerow(['---------------------------------------------'])
    
      # Write the Total Voters
     txtwriter.writerow([(f'Total Voters: {total_votes}')])
     
    # Write the line breaker second formula
     txtwriter.writerow(['---------------------------------------------'])
     
      # Write the candidate: vote percentage and candidate votes
     txtwriter.writerow([f'{candidate}: {candidate_vote_percent}% ({candidate_votes})'])
          
     # Write the line breaker third formula
     txtwriter.writerow(f'--------------------------------')
    
    # Write the winning candidate    
     txtwriter.writerow(f'Winner:  {winning_candidate}')