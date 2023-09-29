'''import csv 
f = open('data.csv','r')
row = csv.reader(f)
for i in row:
    print(i)'''

'''import csv
f = open('data1.csv', 'r')
d = csv.reader(f)
next(d)

adm = int(input("Enter the admission number: "))
found = False  # Add a flag to keep track of whether a record is found or not

for row in d:
    if len(row) >= 5 and int(row[0]) == adm:
        print("Adm no. =", row[0])
        print("Name =", row[1])
        print("Class =", row[2])
        print("Section =", row[3])
        print("Marks =", row[4])  # Corrected to row[4] for marks
        found = True
        break

if not found:
    print("Record not found")

f.close()  # Close the file when done'''

'''import csv
field = ['Roll_no.','Name','Class']
f = open('data2.csv','w')
d = csv.writer(f)
d.writerow(field)
ch ='y'
while ch =='y' or ch == 'Y':
    rn = int(input("Enter the Roll no.: "))
    nm =input("Enter the name: ")
    clas = input("Enter class: ")
    rec = [rn,nm,clas]
    d.writerow(rec)
    ch = input("Enter more record? Y/N: ")
f.close()
'''
import csv
f = open('data.csv', 'r')
d = csv.reader(f)
next(d)  # Skip the header row

print("Students who scored marks more than 80 are: ")
for i in d:
    if int(i[4]) >= 80:  # Check if marks are more than 80
        print("Roll number: ",i[0])
        print("Name: ",i[1])
        print("Class: ",i[2])
        print("Section: ",i[3])
        print("Marks: ",i[4])

f.close()



