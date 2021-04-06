#PyBank's main code
#Dependencies
import os
import csv
#Variables
total_months=0
total_gains=0
change_gains_list=[]
greatest_increase_amount=1
greatest_increase_month=[]
greatest_decrease_month=[]


#Set the cvs file to work with it

csv_path = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    row = next(csv_reader)
    total_months +=1
    total_gains +=int(row[1])
    greatest_increase_amount= int(row[1])
    greatest_increase_month= row[0]
    greatest_decrease_amount=int(row[1])
    prior_row_value=int(row[1])

    for row in csv_reader:
        # Total number of months

        total_months += 1

        # Total amount of "Profit/Losses" over the period
        total_gains += int(row[1])

        #Changes in "Profit/Losses" over the entire period

        change_gains_value= int(row[1]) - prior_row_value
        change_gains_list.append(change_gains_value)
        prior_row_value= int(row[1])

        # To calculate the greatest increase and decrease

        if  greatest_increase_amount < int(row[1]):
            greatest_increase_amount = int(row[1])
            greatest_increase_month = row[0]
        if int(row[1]) < greatest_decrease_amount:
            greatest_decrease_amount = int(row[1])
            greatest_decrease_month = row[0]
    #To calculate the average changes
    average_change = sum(change_gains_list)/ len(change_gains_list)

#For this; I didn't quite undesrtand what we were being asking for, 
# for one part one can argue that the answer are the 2 values with the 
# biggest difference between them in one period of time. But on the other hand, 
# the answer could be the actual biggest/lowest values that there are on the data set, 
# but the answer in the text suggests that the actual lowest/biggest values are 
# what is expected from the code. But some clarification might be nice since I'm 
#curious, thx.

biggest_value= max(change_gains_list)
lowest_value=min(change_gains_list)

#Display results
print('Financial Analysis')
print('----------------------------')
print(f'Total months: {total_months}')
print(f'Total: {total_gains}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${biggest_value})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${lowest_value})')

#Export the results

analysis_file = os.path.join('.','analysis', 'Analysis_results.txt')
with open(analysis_file,'w',) as txt_file:
    txt_file.write('Financial Analysis\n')
    txt_file.write('----------------------------\n')
    txt_file.write(f'Total months: {total_months}\n')
    txt_file.write(f'Total: {total_gains}\n')
    txt_file.write(f'Average Change: ${average_change}\n')
    txt_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${biggest_value})\n')
    txt_file.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${lowest_value})\n')