import os
import csv

file_to_open = os.path.join('Resources', 'election_data.csv')
#print(file_to_open)

text_path = os.path.join("Analysis","financial_analysis.txt")
candidate_votes = dict()
total_number_votes = 0 

with open(file_to_open) as csvfile:
    # code here
    csvreader = csv.reader(csvfile)
    # skip the header row
    header = next(csvreader)
    for row in csvreader:
        total_number_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_votes:
            candidate_votes [candidate_name] = 1
        candidate_votes [candidate_name] += 1


# Print the total number of votes cast
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_number_votes}")
print("-------------------------")
# Print the " " to txt file
with open(text_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_number_votes}\n")
    file.write("-------------------------\n")

    
    # Initialize variables for calculating the winner
    max_votes = 0
    winner = ""

    # Loop through the candidates dictionary to calculate and print the percentage of votes each candidate won
    for candidate_name, votes in candidate_votes.items():
        percentage = (votes / total_number_votes) * 100
        print(f"{candidate_name}: {percentage:.3f}% ({votes})")
        file.write(f"{candidate_name}: {percentage:.3f}% ({votes})\n")

        # Check if the current candidate has more votes than the current maximum
        if votes > max_votes:
            max_votes = votes
            winner = candidate_name

    

    output = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )

    print(output)
    file.write(output)

    



    
