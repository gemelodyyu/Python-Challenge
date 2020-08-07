# import modules 
import csv
import os

# create variable for the path
bank_path = os.path.join("Resources", "PyBank_Resources_budget_data.csv")

# create lists to store data
monthly_change = []
total_month = []
total_profits = []

# read csv data
with open(bank_path) as csv_file: 
	csv_reader = csv.reader(csv_file, delimiter=',')

	#skip the header line
	csv_header = next(csv_reader)

	for row in csv_reader:

		# add up total month and total profits
		total_month.append(row[0])
		total_profits.append(int(row[1]))

	# within the total profits list, calculate monthly change and add to the list 
	# because the last month do not have an additional month to compare the change, so use len()-1 in the range	
	for i in range(len(total_profits)-1):
		monthly_change.append(total_profits[i+1]-total_profits[i])

	# calculate average profits changes
	# round result to 2 decimal places
	average_profits = round(sum(monthly_change)/len(monthly_change),2) 

	# find max increase and max decrease within the monly change 
	max_increase = max(monthly_change)
	max_decrease = min(monthly_change) 

	# find indexs of max increase and max decrease
	# with these indexs we could find the dates within the month list
	# date indexs should +1 because the change would be reflected/associated with the next month
	max_increase_date = total_month[monthly_change.index(max(monthly_change))+1]
	max_decrease_date = total_month[monthly_change.index(min(monthly_change))+1]

# print results
print("Financial Analysis: ")
print("--------------------------------------------------------")
print(f"Total Months: {len(total_month)}")
print(f"Total: ${sum(total_profits)}")	
print(f"Average Change: ${average_profits}")	
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

# spcify the file to write to
write_path = os.path.join("analysis","py_bank_result.txt")

# write results to a text file
with open(write_path, "w") as file: 
	file.write("Financial Analysis: ")
	file.write("\n")
	file.write("--------------------------------------------------------")
	file.write("\n")
	file.write(f"Total Months: {len(total_month)}")
	file.write("\n")
	file.write(f"Total: ${sum(total_profits)}")	
	file.write("\n")
	file.write(f"Average Change: ${average_profits}")	
	file.write("\n")
	file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
	file.write("\n")
	file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")
