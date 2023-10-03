#1
'''A CSV (Comma-Separated Values) file is a simple and widely used file format for storing and exchanging structured data. It is a plain text file that uses commas (or other delimiters like semicolons or tabs) to separate values into rows and columns. CSV files are often used for storing data in a tabular format, similar to a spreadsheet.'''
#2
'''import csv
f = open('emp.csv','r')
d = csv.reader(f)
for row in d:
    print(row)
'''
#3
'''import csv
fields = ['eid','ename','esal']
f = open('emp1.csv','w',newline='')
wr = csv.writer(f)
wr.writerow(fields)
ch = 'y'
while ch=='y' or ch=="Y":
    eid = int(input("Enter employee id: "))
    ename = input("Enter employee name: ")
    esal = float(input("Enter salary: "))
    rec = [eid,ename,esal]
    wr.writerow(rec)
    ch = input("Enter more record Y/N? ")
f.close()
'''
#4
'''import csv
f = open('emp.csv','r')
d = csv.reader(f)
f1 = open('temp.csv','w',newline='')
d1 = csv.writer(f1)
for row in d :
    d1.writerow(row)
f.close()
f1.close()
'''
#5
'''import csv
f = open('emp.csv','r')
d = csv.reader(f)
next(d)
for row in d:
    if len(row)>=3 and int(row[2])>5000:
        print("eid: ",row[0])
        print("ename: ",row[1])
        print("salary: ",row[2])
        print()
f.close()'''
#6
'''import csv
f = open('emp.csv','r')
d = csv.reader(f)
next(d)
count =0
for row in d:
    count +=1
print("Total records present are: ",count)
f.close()'''
#7
'''import csv
import os

f = open('emp.csv','r')
f1 = open('temp1.csv','w',newline='')
d = csv.reader(f)
d1 = csv.writer(f1)
next(d)

id = int(input("Enter the id: "))
nam = input("Enter the name: ")
sal = float(input("Enter the salary: "))
rec = [id,nam,sal]

header = ['e_id','e_name','e_salary']
d1.writerow(header)
for i in d:
    if int(i[0]) == id:
        d1.writerow(rec)
    else:
        d1.writerow(i)
f.close()
f1.close()

os.remove('emp.csv')
os.rename('temp1.csv','emp.csv')'''
#8
'''import csv
f = open('emp.csv','r')
d = csv.reader(f)
next(d)
max = 0
for i in d:
    if int(i[2]) > max :
        max = int(i[2])
f.close()

f = open('emp.csv','r')
d = csv.reader(f)
next(d)
for i in d:
    if int(i[2]) == max:
        print(i)
f.close()
'''