import os
import csv
candidates=[]
csv_path = os.path.join('.', 'election_data.csv')
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    for row in csv_reader:
        x=row[2]
        if x not in candidates:
            candidates.append(x)
print(candidates)