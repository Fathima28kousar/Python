import csv
f = open('data.csv','r')
d = csv.reader(f)
for row in d:
    print(','.join(row))
    print(type(','.join(row)))
    print()

f.close()