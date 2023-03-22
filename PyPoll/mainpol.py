#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#create the list
names = set()
#set the starting variables to 0
total_votes = 0

#Opening and reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Keeping track of the votes
        total_votes += 1
        #add the value from the candidate column to the set
        names.add(row[2])

print ("Total Votes: ", int(total_votes))
print ("Candidates: ", str(names))
