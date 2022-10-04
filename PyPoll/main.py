import os
import csv


candidates = []
num_votes = 0
vote_counts = []

election_data = ['1', '2']


for files in election_data:
    
    election_dataCSV = os.path.join("Resources", "election_data.csv")

    with open(election_dataCSV) as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')
        line = next(csvReader,None)

        # Process the votes
        for line in csvReader:
            num_votes = num_votes + 1
            candidate = line[2]

            # If the candidate has other votes then add to vote total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            # Else create new spot in list for candidate
            else:
                candidates.append(candidate)
                vote_counts.append(1)

    # Create variables for calculations
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/num_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    # Round decimal

    percentages = [round(i,3) for i in percentages]

   
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

with open('analysis.txt', 'w') as text:
    text.write("Election Results")
    text.write("--------------------------")
    text.write(f"Total Votes: {num_votes}")
    for count in range(len(candidates)):
        text.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    text.write("---------------------------")
    text.write(f"Winner: {winner}")
    text.write("---------------------------")

    