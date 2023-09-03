# def add(a,*b):
#     print(a,b)
# add(10,20)    
# add(10,20,30)    
# add(10,20,30,40)    
# add(10,20,30,40,50)
mylist = [("apple",50),("mango",59),("banana",30),("peach",3)]
sortedlist = sorted(mylist,key = lambda x:x[1])
print(sortedlist)

mylist = ["apple","mango","banana","peach"]
sortedlist = sorted(mylist,key = lambda x:x[1])
print(sortedlist)

mylist = ["apple","mango","banana","peach"]
sortedlist = sorted(mylist)
print(sortedlist)

mylist = [1,2,3,45,6]
newlist = [(lambda x:x+2)(x) for x in mylist]
print(newlist)
