#11
'''import csv
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "San Francisco"},
    {"Name": "Charlie", "Age": 22, "City": "Los Angeles"}
]

f = open('output.csv', 'w', newline='') 
fieldnames = ["Name", "Age", "City"]
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

for row in data:
    writer.writerow(row)

f =  open('output.csv', 'r') 
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()'''
#10
'''import csv
f = open('data.csv','w',newline='')
wr = csv.writer(f)
wr.writerow(['Name','class','marks'])
wr.writerow(['fathima','XII',89])
wr.writerow(['Yves','XII',91])
wr.writerow(['Sonni','XI',100])
f.close()

f = open('data.csv','r')
d = csv.reader(f)
for row in d:
    print(row)
f.close()'''

#9
'''import csv
fields = ['Name','Class','Marks']
f = open('data1.csv','w',newline='')
wr = csv.writer(f)
wr.writerow(fields)
wr.writerow(['fathima','XII',99])
wr.writerow(['kousar','XI',89])
wr.writerow(['naseera','X',100])
print(wr)
f.close()

f = open('data.csv','r')
d = csv.reader(f)
for i in d:
    print(i)
f.close()'''
#8
'''import csv
f = open('data.csv','r')
d = csv.reader(f)
header = next(d)
count = 0
for row in d:
    count +=1
    
print("The number of rows are: ",count)
print("Field names are: ",header)
f.close()'''
#7
'''import csv
f = open('data.csv','r')
d = csv.DictReader(f)
for row in d:
    print(row['Name'],row['Class'])
f.close()
'''
#2
'''import csv
f = open('data.csv','r')
d = csv.reader(f,delimiter='\t')
for row in d:
    print(row)
f.close()'''
#3
'''import csv
f = open('data.csv','r')
d = csv.reader(f)
data = list(d)
print(data)'''
