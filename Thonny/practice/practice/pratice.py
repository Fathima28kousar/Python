# L1 = [11,22,33]
# print(L1+L1)
# print(L1*2)
# print(L1*1)
# print(L1*-2)
# L1.append(23)
# print(L1)
# print(sum(L1))
# print(max(L1))
# print(min(L1))
# # L1.insert(-1,"a")
# # print(L1)
# print(L1)
# print(L1)
# print(L1.pop())
# print(L1)
# L1.extend([4,5,6])
# print(L1)
# print(min(L1))
# print(L1)
# L1.append([4,5,6])
# print(L1)
# print(L1.index(6))
# print(L1)
# # L1.remove("a")
# print(L1)
# print(L1.pop(4))
# print(L1)
ids = [101,102,103]
ids.append(104)
print(ids)
ids.insert(0,105)
print(ids)
enames = ["rahul","soniya"]
enames.append("priyanka")
print(enames)
l1 = [10,20,30,40,50]
l2 = [60,70]
l1.extend(l2)
# print(l1)
# l1.extend([100])
# print(l1)
# enames.remove("soniya")
# print(enames)
# #enames.remove(10)
# print(l1)
# print(enames)
# el = enames.pop()
# print(enames)
# print(el)
l1 = [10,20,30,40]
l2=l1.copy()
print(l1)
l2[2] = 45
print(l2)
print(l1)
l1 = l2 
print(l1)
l1  = [400,300,200,500]
l2 = l1 [:]
print(l2)
####tuples
t1 = (40,20,10,30)
# t1.reverse()
# print(t1)
l1.sort()
print(l1)
print(t1)
l1 = sorted(t1)
print(type(l1))
t1 = tuple(l1)
print(t1)
l1 = [1,2,3]
l2 = [1,2,3,4,5,6]
l = ["amit", "anita" , "zee", "longestword"]
print(max(l))
l1 = list("www.csiplearninghub.com")
print(l1[20:1])
l2 = ["amit","sumit","naina"]
print(l2[-1][-1])
# print(l2**3)
l= [0.5*x for x in range(4)]
print(l)
li = [1*x for x in range(10,1,-4)] 
print(li)

# for i in L:
#     print(i,end=" ")
#     i = i+1
# L = ["amit","sumit","naina"] 
# L1 = ["sunil"]
# # print(L+L1)  
# L.append("4")
# l = 
# print(L)
L = [1,2,3,4,5]
L.append(6)
print(L)

L = "123456"
L = list(L)
print(type(L[0]))

T = (1,2,3,4,5.5)
L = list(T)
print(L[3]*2.5)

T = [1,2,3,4]
T1=T
T[0] ="A"
print(T)
print(T1)

T = [1,2,3,4]
T1 =[5,6,7]
T.append(T1)
print(T)

L = ["amit" ,"sumit" ,"naina"]
L1 = ["sumit"]
print(L+L1)
L =[1,5,9]
print(sum(L)+max(L)-min(L))