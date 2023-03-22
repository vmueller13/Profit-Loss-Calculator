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
        candidate
for value in names:
    percentage = round(float(names[candidate])/float(total_votes),2)
for key in votesByCandidate.items():
    percentage_of_votes.append(v/total_votes)

print ("Total Votes: ", int(total_votes))
print ("Candidates: ", str(names))
print ("Percentage of Votes: ", int(percentage_of_votes))
