# Import functions to create a file path and read the CSV file
import csv
import os

# Path to collect data from the CSV file
csvpath = os.path.join('.', 'Resources','budget_data.csv')
 
# Read the data from the CSV file
with open(csvpath) as csvfile:

    # specify delimiter and variable tha holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

            # Read each row of data after the header
    for row in csvreader:
        print(row)

# Find the total number of months in the dataset

# Caculate the net total amount of profits/losses over the entire period

#Calculate the changes in profits/losses over the entire period

# Calculate average of changes in profits/losses

# Calculate greatest increase in profits over the entire period

# Calculate the greatest decrease in profits over the entire period

# Code to print the results

# Export of CSV file