import csv
f = open("one.csv","r")
cp = csv.reader(f)
print(cp)
print(type(csv))



for line in list(cp):
    for word in line:
        print(word,end= " ")
    print()  
 
