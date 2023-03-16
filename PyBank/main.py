# Modules
import os
import csv

#File to read
csvpath = os.path.join('Resources', 'budget_data.csv')

def import_csv(csvpath):
    total_months =[]
#count the number of months
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if row:
                row_index += 1
                columns = [str(row_index), row[0], row[1], row [2]]
                total_months.append(columns)
    return total_months
total_months = import_csv(csvpath)  
last_row = total_months[-1]
print (total_months)


















# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

financial_analysis = "Total Months: " + "Net amount of profit/losses: " + "Date and amount of greatest increase in profits: " + "Date and ammount of greatest decrease: "


#write the info into a new csv
# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join ("Resources", "analysis_bank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase', 'Greatest Decrease'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])


print ("Financial Analysis")
print ("-----------------------------")
print (financial_analysis)