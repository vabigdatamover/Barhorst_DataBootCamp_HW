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

#Creates an emptyt list for canidate names
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
vote_percent = {}
for candidate in poll:
    candidate_votes = poll[candidate]
    candidate_vote_percent = round((candidate_votes / total_votes)*100, 3)
    vote_percent[candidate] = [candidate_vote_percent, candidate_votes]

## Loop through print a complete list of candidates who received votes
    print(f'{candidate}: {candidate_vote_percent} ({candidate_votes}) ')   
# zips candidates, num_votes, vote_percent into tuples
#clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in winner_list:
    if max(total_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
#winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
#if len(winner_list) > 1:
#    for w in range(1, len(winner_list)):
#        winner = winner + ", " + winner_list[w]
                    
## Loop through print a complete list of candidates who received votes

    #print(f'{candidate}: {candidate_vote_percent} ({candidate_votes}) ')   
       
## Loop through and print the percentage and total of votes each candidate won
    print(f'--------------------------------')
    print(f'Winner:  {winner_list}')  
     
    #print(f'--------------------------------')
#            
### Loop through and print the winner of the election based on popular vote
##        canidate_winner = min(value)*100
##        print(f'Winner: {monthes} (${greatest_decrease})')
      
    print(f'--------------------------------')
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