# Import functions to create a file path and read the CSV file
import csv
import os

# Path to collect data from the CSV file
csvpath = os.path.join('..', 'Resources','election_data.csv')

total_votes = 0


# Complete list of candidates who received votes

# Percentage of votes each candidate won

# Winner of election based on popular vote


# Read the data from the CSV file
with open(csvpath, 'r') as csvfile:

    # specify delimiter and variable tha holds contents 
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first 
    csv_header = next(csvreader)

    for row in csvreader:


        # Store data for each column as variables
        ballot_ID = {" "}
        county = {" "}
        candidate = {" "}

        ballot_ID = row[0]
        county = row[1]
        candidate = row[2]
        
        # Total number of votes cast
        total_votes += 1

        # List of candidates that received votes

        # Percentage of votes each candidate won


# Print election results
print("Election Results")

print("------------------------")

print("Total Votes: " + str(total_votes))


# Export of CSV file

output_path = os.path.join("PyPoll_Results.csv")

with open(output_path, 'w') as datafile:
      writer = csv.writer(datafile)  