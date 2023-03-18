# Modules
import os
import csv

#File to read
csvpath = os.path.join('Resources', 'budget_data.csv')

#define variables
months = []
net_loss_list = []

total_months = 0
net_loss = 0
current_loss = 0
previous_loss = 0

#open and read csv
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#read the header first
    csv_header = next(csvfile)
    first_row = next(csvreader)
    
    # Loop through each row
    for row in csvreader:
        total_months +=1
            
      #add each month to the months count  
        months.append(row[0])


print ("Financial Analysis")
print ("-----------------------------")
print (f"Total Months: {total_months}")