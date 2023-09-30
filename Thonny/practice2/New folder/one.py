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
'''import csv 
f = open('product.csv','r')
d = csv.reader(f)
next(d)
found = False
for row in d:
    if int(row[2]) >= 300:
        print("Product_id = ",row[0])
        print("Product_name = ",row[1])
        print("Price = ",row[2])
        found = True
        

if not found :
    print("Record not found")
'''
'''import csv
f = open('data1.csv','r')
d = csv.reader(f)
next(d)
s = 0
for row in d:
   s+=1

print("Number of records are: ",s)
f.close()'''

'''import csv
import os
f = open('data1.csv','r')
f1 = open('temp1.csv','w')
d = csv.reader(f)
d1 = csv.writer(f1)
next(f)
s = 0
roll_no = int(input("Enter the roll number: "))
mn = input("Enter the modified name: ")
mm = int(input("Enter modified marks: "))
mr = [roll_no,mn,mm]
header = ["Roll number","Name","Marks"]
d1.writerow(header)
for i in d:
    if int(i[0]) == roll_no:
        d1.writerow(mr)
    else:
        d1.writerow(i)
f.close()
f1.close()

os.remove('data1.csv')
os.rename('temp.csv','data1.csv')
'''
# import csv
# f = open('temp1.csv','r')
# d = csv.reader(f)
# next(d)
# max=0
# for row in d:
#     if int(row[2])>max:
#         max=int(row[2])
        
# f.close()
# f = open('temp1.csv','r')
# d = csv.reader(f)
# next(d)
# for row in d:
#     if int(row[2])==max:
#         print(row)
# f.close()

'''import csv
f = open('data.csv','r')
d = csv.reader(f)
for row in d:
    print(','.join(row))
    print(type(','.join(row)))
    '''

'''import csv
field = ['Name','Class','Section','Marks']
rows = [['Fathim','12','A','96'],['Lubna','13','C','90'],['Naseera','14','B','50']]
f = open('data10.csv','w',newline='')
wr = csv.writer(f)
wr.writerows(field)
wr.writerows(rows)
f.close()'''

