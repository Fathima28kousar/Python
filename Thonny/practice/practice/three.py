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
'''
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
list1=list(["welcome"])
print(list1)
L = ["amita", "anita" ,"zee", "longestworld"]
print(max(L))
#nested lists
L5 = [["aman",30],["rahul",67],["fathima",100]]
#        0             1           2
print(L5)
print(L5[1+1])
L1 = [55,48,90,39,29,71,31]
print(L1[4])
L1[4] = 899
print(L1)
print(L1[4])'''
'''L1 = [10,20,30,40,50,60]
L2 =[900,800,700,600]
print(L1+L2)
L3 = ["red","blue","green"]
L4 = ["yellow","brown","pink"]
print(L3+L4)
print(L1+L2+L3+L4)
L5 =[1,2,3]
L6 = "hello"
print(L5+L6)'''
'''L1 = [1,2,3,4,5,6,78,3]
print(L1*2)
L2 = ["lemon"]
print(L2*3)
print("a" in L1)
print(L1[1:4])
'''
'''L1 = ["Ram ","gyan","brij", "ravi", "manav", "summit", "raman"]
print(L1[1:4])
print(L1[3:1])
print( L1[:3])
print(L1[0:6:2])
print(L1[::2])
print(L1[-6:-3])'''

'''L1 = [1,2,3,4,5,[40,50,60,70],6,7,8]
print(L1[5])
print(L1[5][2])'''
L1 = [1,2,3,4,5,[40,50,60,70],6,7,8]

L2 = L1
print(L2)













































































































