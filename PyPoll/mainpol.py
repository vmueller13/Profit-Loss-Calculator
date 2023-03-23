#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#create the lists and dictionaries
names = set()
dict_candidates = {}
candidate_list = []
dict_percentages = {}

#Opening and reading the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    #Reading the header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Keeping track of the votes
        candidate = row[2]
        #add the value from the candidate column to the set
        names.add(row[2])
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            dict_candidates[candidate] = 0
        dict_candidates[candidate]+=1
#total the votes
total_votes = sum(dict_candidates.values())

#find the winner of the election
winner = max(dict_candidates, key=dict_candidates.get)
winning_vote_count = dict_candidates[winner]

#find the percentage of votes per candidate
for candidate, vote_count in dict_candidates.items():
    percentage = round((vote_count / total_votes) * 100, 3)
    dict_percentages[candidate] = f"{percentage}%"

print ("Election Results")
print ("-------------------------")
print ("Total Votes: ", total_votes)
print ("Percentage of Votes by Candidate: ", dict_percentages)
print ("Total Votes Per Candidate: ", dict_candidates)
print (f"The winner is {winner} with {winning_vote_count} votes.")

#Exporting to .txt file, how to get into the analysis folder?
file_path = os.path.join("analysis", "electionresults.txt")

with open("electionresults.txt", "w") as f:
    line1 = ("Election Results")
    line2 = ("-------------------------")
    line3 = str(f"Total Votes: {str(total_votes)}")
    line4 = str(f"Percentage of Votes by Candidate: {str(dict_percentages)}")
    line5 = str(f"Total Votes Per Candidate: {str(dict_candidates)}")
    line6 = str(f"The winner is {str(winner)} with {str(winning_vote_count)} votes.")
    f.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6))

    #Close the file
    f.close()