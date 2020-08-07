# import modules 
import csv
import os

# create variables
candidate_list = []
candidate_votes = []
total_votes = 0  

# create variable for the path
poll_path = os.path.join("Resources", "election_data.csv")

# read csv data
with open(poll_path) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    #skip the header line
    csv_header = next(csv_reader)
    
    # use for loop to go though the election_data
    for row in csv_reader: 

        total_votes = total_votes +1
        candidate = row[2]

        # calculate running total for each candidate 
        if candidate in candidate_list:
            index = candidate_list.index(candidate)
            candidate_votes[index] = candidate_votes[index] +1 
            
        # make new spot for another candidate
        else:
            candidate_list.append(candidate)
            candidate_votes.append(1)

    # create temp variables
    candidate_percentages = []
    max_vote = candidate_votes[0]
    max_index = 0

    # calculate percentage each candidate win and find the winner
    for i in range(len(candidate_list)): 
        percentage = round(candidate_votes[i]/total_votes*100, 2) 
        candidate_percentages.append(percentage)
        #find winner
        if candidate_votes[i] > max_vote:
            max_vote = candidate_votes
            max_index = i
    winner = candidate_list[max_index]

    candidate_percentage_vote = {}
    candidate_percentage_vote["names"] = candidate_list
    candidate_percentage_vote["percent"] = candidate_percentages
    candidate_percentage_vote["counts"] = candidate_votes
    # print(candidate_percentage_vote)
 
    # print results
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    for i in range(len(candidate_list)):
        print(f"{candidate_list[i]}: {candidate_percentages[i]}% ({candidate_votes[i]})")
    print("-----------------------------")
    print(f"Winner:  {winner}")
    print("-----------------------------")

# generate output

# save the results to analysis text file
write_path = os.path.join("analysis","py_poll_result.txt")
with open(write_path, "w") as file: 
    file.write("Election Results\n")
    file.write("-----------------------------\n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write("-----------------------------\n")
    for i in range(len(candidate_list)):
        file.write(f"{candidate_list[i]}: {candidate_percentages[i]}% ({candidate_votes[i]})\n")
    file.write("-----------------------------\n")
    file.write(f"Winner:  {winner}\n")
    file.write("-----------------------------")