import csv
with open('persons.csv','w') as csvfile:
    fileWritet=csv.writer(csvfile,delimiter=',',
                          quotechar='|',
                          quoting=csv.QUOTE_MINIMAL,
                          lineterminator='\n'
                          )
    "default lineterminator='\r\n' which case double line"
    fileWritet.writerow(['Name','Profession'])
    fileWritet.writerow(['Osama','Programmer'])
    fileWritet.writerow(['Nor','Developer'])
    fileWritet.writerow(['Anything','any prof'])








