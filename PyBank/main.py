# Modules
import os
import csv

#File to read
csvpath = os.path.join('Resources', 'budget_data.csv')

#define variables
months = []

total_months = 0
total_profit = 0

#count the rows to find the total months
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#read the header first
    csv_header = next(csvfile)

    # Loop through looking for the video
    for row in csvreader:
        total_months +=1

      #add each month to the months count  
        months.append(row[0])


print ("Financial Analysis")
print ("-----------------------------")
print (f"Total Months: {total_months}")