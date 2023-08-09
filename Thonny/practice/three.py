'''
li1 = [10,20,30,40,50,40,40,40]
print(len(li1))
print(li1.count(40))
print(li1.index(40))
li2 = [400,500,900,400,100,200]
li2.sort()
print(li2)
enames = ["rahul","dave","sara","heal"]
enames.sort()
print(enames)

ename = ["anjali","rahul","tina","sharma"]
ename.sort(reverse = True)
print(ename)
ids = [101,102,103,104]
print(ids)
ids.append(105)
ids.insert(1,100)
print(ids)

print(ids)'''
users = ["rahul","anjali","sharma","tina",43,67,90,78]
print(users[0:2])
print(users[1])
users.append("elsa")
print(users)
users += ["Jason"]
print(users)
users.extend(["robert","jimmy"])
print(users)
data = ["zimmy","dave","True",43]
users.extend(data)
print(users)
users.insert(-1,"Bob")
print(users)
users[2:2]=["eddie","alex"]
print(users)
users[1:3] = ["Roober","JPJ"]
print(users)
users.remove("tina")
print(users)
print(users.pop())
print(users)
del users[0:10]
print(users)

users[1:2] = ["hello"]
users.sort()
print(users)


users.sort()
print(users)
users.sort(key=str.lower)
print(users)
nums=[1,39,50,55,79,86,44,32]
#print(nums)
'''#nums.sort()
print(nums)
#nums.reverse()
print(nums)
#nums.sort(reverse = True)
print(nums)'''
numscopy = nums.copy()
print(numscopy)
mynums = list(nums)
print(mynums)
mycopy = nums[:]
print(mycopy)
mycopy.sort()
print(mycopy)
print(type(nums))
mylist = list([1,"niel",True])
print(mylist)


mytuple = tuple(("fathima",43,True))
print(mytuple)
anothertuple = (1,2,"grow")
print(anothertuple)
print(type(anothertuple))
newlist = list(mytuple)
newlist.append("niel")
newtuple = tuple(newlist)
print(newlist)


















































































































