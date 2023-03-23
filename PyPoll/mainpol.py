#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#create the list
names = set()
dict_candidates = {}
candidate_list = []

#set the starting variables to 0
total_votes = 0
winner = ""

#Opening and reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Keeping track of the votes
        total_votes += 1
        candidate = row[2]
        #add the value from the candidate column to the set
        names.add(row[2])
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            dict_candidates[candidate] = 0
        dict_candidates[candidate]+=1
winner = max(dict_candidates, key=dict_candidates.get)
winning_vote_count = dict_candidates[winner]

print ("Total Votes: ", int(total_votes))
print ("Candidates: ", str(names))
print (dict_candidates)
print (f"The winner is {winner} with {winning_vote_count} votes.")
