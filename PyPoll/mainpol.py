#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#create the lists
votes = []

#set the starting variables to 0
total_votes = 0

#Opening and reading the CSV file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    csv_header = next(csvreader)

    total_votes += 1

    for row in csvreader:
        # Keeping track of the votes
        votes.append(row[0])
        total_votes += 1

print (int(total_votes))