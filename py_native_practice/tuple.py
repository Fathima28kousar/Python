#Reverse the tuple****************************
'''tuple1 = (10,20,30,40)
s = tuple1[::-1]
print(s)'''
#Access value 20 from the tuple****************************
'''tuple1 = ("orange",[10,20,30,40],(5,15,25))
s = tuple1[1][1]
print(s)'''
#Create a tuple with single item 50****************************
'''
tuple1 = (50)
print(tuple1)'''
#Unpack the tuple into 4 variables**************************************************
'''tuple1 = (10,20,30,40)
a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)'''
#Swap two tuples in Python**************************************************
'''tuple1 = (10,20,30)
tuple2 = (100,200,300)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)'''
#Copy specific elements from one tuple to a new tuple**************************************************
'''tuple1 = (11,22,33,44,55,66)
tuple2 = tuple1[3:5]
print(tuple2)'''
# Modify the tuple************************************************************************************
'''tuple1 = (11,[22,33],44,55,66,77)
tuple1[1][0] = 222
tuple1[1][1] = 333
print(tuple1)'''
#Sort a tuple of tuples by 2nd item****************************************************************
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple2 = tuple(sorted(list(tuple1),key=lambda x:x[1]))
print(tuple2)
#Counts the number of occurrences of item 50 from a tuple***********************************************
tuple = (50,60,70,80,50)
print(tuple.count(50))
#Check if all items in the tuple are the same***********************************************************

def check(t):
    return all(i == t[0] for i in t)
tuple1 = (45,45,45,45,45)
print(check(tuple1))
