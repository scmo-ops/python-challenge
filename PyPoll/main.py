# Second part of the Py Me Up, Charlie

# Modules
import os
import csv

# Variables

total_votes=0
correy_votes=0
khan_votes=0
li_votes=0
otooley_votes_=0
candidates=[] 

#Set the cvs file to work with it

csv_path = os.path.join('.', 'Resources', 'election_data.csv')
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

    for row in csv_reader:

        #Total number of votes

        total_votes +=1

        # Number of votes each candidate got
        if (row[2] == 'Khan'):
            khan_votes +=1
        elif (row[2] == 'Correy'):
            correy_votes +=1
        elif (row[2] == 'Li'):
            li_votes +=1
        else:
            otooley_votes_ +=1

# Vote % and who won

khan_percentage = khan_votes / total_votes
correy_percentage = correy_votes / total_votes
li_percentage = li_votes / total_votes
otooley_percentage = otooley_votes_/total_votes
win_percentage  = max(khan_percentage, correy_percentage, li_percentage, otooley_percentage)
if win_percentage == khan_percentage:
    winner="Khan"
elif win_percentage == correy_percentage:
    winner="Correy"
elif win_percentage == li_percentage:
    winner="Li"
else:
    winner="O'Tooley"

#Display results

print('Election results')
print('-------------------------')
print(f'Total votes: {total_votes}')
print('-------------------------')
print(f'Khan: {khan_percentage} ({khan_votes})')
print(f'Correy: {correy_percentage} ({correy_votes})')
print(f'Li: {li_percentage} ({li_votes})')
print(f'OTooley: {otooley_percentage} ({otooley_votes_})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# Export results

analysis_file = os.path.join('.', 'analysis', 'Analysis_results.txt')
with open(analysis_file,'w',) as txt_file:
    txt_file.write('Election results\n')
    txt_file.write('------------------------\n')
    txt_file.write(f'Total votes: {total_votes}\n')
    txt_file.write('------------------------\n')
    txt_file.write(f'Khan: {khan_percentage} ({khan_votes})\n')
    txt_file.write(f'Correy: {correy_percentage} ({correy_votes})\n')
    txt_file.write(f'Li: {li_percentage} ({li_votes})\n')
    txt_file.write(f'OTooley: {otooley_percentage} ({otooley_votes_})\n')
    txt_file.write('-------------------------\n')
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write('------------------------\n')
