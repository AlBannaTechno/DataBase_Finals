import csv
with open('persons.csv','r') as f:
    rows=csv.reader(f)
    for row in rows:
        print(row)
