# import modules 
import csv
import os

# create variable for the path
poll_path = os.path.join("Resources", "election_data.csv")

# create variables


# read csv data
with open(poll_path) as csv_file: 
	csv_reader = csv.reader(csv_file, delimiter=',')

	#skip the header line
	csv_header = next(csv_reader)