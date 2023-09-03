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

list = [(101,"Rahul"),(102,"Raj")]
dict = {k:v for k,v in list}
print(dict)