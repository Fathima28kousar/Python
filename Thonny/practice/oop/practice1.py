'''from functools import reduce
s = 0
n = int(input("Enter the first number : "))
range = range(n+1)
sum = reduce(lambda s,n:s+n,range)
print(sum)'''

# n = int(input("Enter the number :"))
# x = sum(range(1,n+1))
# print("sum is",x)

# keys =[1,2,3,4,5]
# values = [11,22,33,44,55]
# new_dict = dict(zip(keys,values))
# print(new_dict)

# employees = ["kelly","emma"]
# defaults = ["designation:""developer","salary",800]
# new = dict.fromkeys(employees,defaults)
# print(new)   
'''dict={
    "name":"kelly",
    "age":25,
    "salary":2999,
    "designation":"software-developer",
    "mobile_no.":234546
}

keys = ["name","salary","designation"]
for k in keys :
    dict.pop(k)
print(dict)    '''

'''samp_dict = {"a":100,"b":299,"c":1000}
if 299 in samp_dict.values():
    print("present")

samp_dict = {"a":100,"b":299,"c":1000}
if "b" in samp_dict.keys():
    print("present")'''
'''
sample_dict = {
    "physics":84,
    "maths":222,
    "social":123
}


print(min(sample_dict,key=sample_dict.get))
print(min(sample_dict))'''

# c = 0
# num = int(input("Enter the number :"))
# if num>1:
#     for i in range(2,(int(num/2)+1)):
#         if num%i==0:
#             c=1
#             break
#     if c==1:
#         print("its not a prime no.")    
#     else:
#         print("its a prime no.")    

# else:
#     print("enter another number")
'''
list1 = [i+1 for i in range(20)]
print(list1)
list2 = [i for i in range(20) if i%2==0]
print(list2)
list3 = [i for i in range(20) if i%2==0 if i%3==0]
print(list3)'''


'''list = [1,2,3,4,5,6]
new = []
for i in list:
    new.append(i+1)
print(new)    


list1 = [i+1 for i in list]
print(list1)
'''
''''list = []
for i in range(20):
    if i%2==0:
        list.append(i)
print(list)

list1 = [i for i in range(20) if i%2==0]
print(list1)
print()'''

'''list1 = []
for i in range(20):
    if i%2==0:
        if i%3==0:
            list1.append(i)
print(list1)

list2 =[i for i in range(20) if i%2==0 if i%3==0]
print(list2)'''

# list = []
# for i in range(10):
#     if i%2==0:
#         list.append(i)
#     else:
#         print("invalid")
# print(list)  

# list1 = [i if i%2==0 else "invalid" for i in range(20)]
# print(list1)

'''dict = {}
for i in range(5):
    dict[i] = i*2
print(dict)

dict1 = {n:n*2 for n in range(5)}
print(dict1)
'''
'''dict1 = {}
for i in range(20):
    if i%2==0:
        if i%3==0:
            dict1[i]=i*2
print(dict1)

dict2 = {i:i*2 for i in range(20) if i%2==0 if i%3==0}
print(dict2)'''

'''list = [(101,"Rahul"),(102,"Raj")]
dict = {k:v for k,v in list}
print(dict)'''


'''num = int(input("Enter the number : "))
for i in range (num+1):
    for j in range(i+1):
        print(j+1,end =" ")
    print()      '''

'''import math
print(math.floor(9.7))
print(math.floor(-41.444))
print(math.ceil(-40.34))
print(math.pow(2,3))
print(math.sqrt(625))
print(math.fabs(-33))
print(math.pi)
print(math.e)
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
'''
'''import statistics
print(statistics.median([20,30,40,50,60]))
print(statistics.mean([20,30,40,50,60]))
print(statistics.mode([20,30,40,50,60]))'''


'''a = random.randrange(30)
print(a)
b = random.randrange(40)
print(b)
names = ["fathima","kousar","lubna","sadiya","naseera","banu"]
c = random.randrange(len(names))
print(names[c])'''

# print(random.random()*6+10)
# print(random.random()*900+100)
# print(random.random()*90+10)



'''highest = int(input("Enter the highest limit : "))
lowest = int(input("Enter the lowest limit : "))
even=[]
while len(even)<=5:
    num= random.randint(lowest,highest)
    if num%2==0:
        even.append(num)
print("Random even numbers are : ", even)
'''


'''import datetime
x = datetime.datetime(2020,5,17)
print(x.strftime("%B"))'''

'''import os 
if os.path.exists("one.txt"):
    os.remove("one.txt")
else:
    print("the file does not exist")'''
'''
import os
os.rmdir("folder")'''

import json
x = {
    "name":"john",
    "age": 30,
    "avail":True,
    "hello":None
}

'''y = json.dumps(x)
print(y)
print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,sort_keys=True))'''

# tuple1 = (50,60,70,10,20)
# a,b,c,d,e=tuple1
# print(tuple1)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# tuple2 = (10,20,30,40,50)
# tuple3 = (10,20,30)
# tuple2,tuple3 = tuple3,tuple2
# print(tuple3)
# print(tuple2)

# tuple2 = (10,20,30,40,50)
# tuple1= tuple2[2:5]
# print(tuple1)
'''file = open("data.txt","r")
data = file.read()
c = 0
for i in data:
    if i== "a":
        c = c+1
print("frequency of alphabet a is: ",c)  '''      
file = open("data.txt","r")
data = file.read()
print("Total number of ch in a file are:",len(data))



