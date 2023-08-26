# A = {}
# B = dict()
# print(A)
# print(B)
# d = {}
# for i in range(2):
#     r = int(input("enter the roll number: "))
#     name = input("enter the name of the student: ")
#     d[r] = name
# print(d)    

# d = {}
# for i in range(2):
#     n = int(input("enter the roll number of student : "))
#     name = input("enter the name of the student : ")
#     d[n] = name
# print(d)    

# for k in A:
#     print(k,"-->",A[k])
#     print(k,A[k])

# A = {1:"fathima", 2:"kousar", 3:"lubna" }
# A[4] = "naseera"
# print(A)
# s1 = {}
# print(type(s1))
# A = {1:"one",2:"two",3:"three"}
# print(A)
# B = {1:"amit",2:"anita",3:"neeti"}
# A.update(B)
# print(A)
# B = {1:"amit",2:"sunil",3:"lata"}
# B[2] = "ram"
# print(B)

# emp = {"id":101,"name":"rahul","salary":45000}
# emp["name"] = "gandhi" #value get replaced
# print(emp)
# emp["loc"] = "bangalore" #new key and value gets added
# print(emp["id"])
# print(emp["name"])
# print(emp["salary"])
# # print(emp["email"])
# del emp["id"]
# print(emp)
# emp = {"id":101,"name":"rahul","salary":45000}
# emp.pop("name")
# print(emp)
# emp.popitem()
# print(emp)
# print(emp.keys())
# print(emp.values())
# print(emp.items())
# print(len(emp))

# emp = {"id":101,"name":"rahul","salary":45000}
# del emp["id"]
# emp.pop("name") #asks for one argument
# emp.popitem() #deletes the last element
# emp.clear()  #clears the dict
# employees =[{"id":1,"first_name":"Franzen","gender":"Male"},
#             {"id":2,"first_name":"Hendrik","gender":"Male"},
#             {"id":3,"first_name":"Nonie","gender":"Female"},
#             {"id":4,"first_name":"Shermy","gender":"Male"},
#             {"id":5,"first_name":"Chet","gender":"Male"}]
# for emp in employees:
#    print(emp["first_name"])
# # i = 0
# while i<len(employees):
#     print(employees[i]["first_name"])
#     i = i+1

# B = {"id": 101, "ename": "fathima", "sal": 45000, "loc": "bangalore"}
# del B["id"]
# print(B)
# B.pop("sal")
# print(B)

# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# for value in my_dict.values():
#     print(value)
# B = {'A':"Apple" ,'B':"Bat",'C':"Cat"}
# A.update(B)
# print(B)
# print(B.values())

# print(A.get(4,"hey"))
# print(A)
# B = {"A": "Apple","B":"Bat", "C":"Cat"}
# for b in A:
#     print(b)
# for b in B:
# #     print(b)   
# A = {1:"one",2:"two",3:"three"}
# B = {"A": "Apple","B":"Bat", "C":"Cat"}
# A.update(B)
# print(A)
# print(B)
# A = {"jan":39 ,"feb":28 ,"march":31}
# print(max(A.values()))
# print(min(A.keys()))
# print(max(A.items()))
# print(A.pop("march"))
# print(A)

# D = {"amit":40 ,"sunil":34, "naina":30}
# print(D.values())
# print(D.keys())
# D["Ravi"] = 45
# print(D)
# print(D["amit"]+D["sunil"])
    # m = {1: "Jan",2:"June",3:"August"}
    # print(m[1])
# num = {1:10,2:20,3:30}
# print(num)
# print(num.items())
# print(len(num))
# print(num.pop(2))
# employees =[{"id":1,"first_name":"Franzen","gender":"Male"},
#             {"id":2,"first_name":"Hendrik","gender":"Male"},
#             {"id":3,"first_name":"Nonie","gender":"Female"},
#             {"id":4,"first_name":"Shermy","gender":"Male"},
#             {"id":5,"first_name":"Chet","gender":"Male"}]
# for emp in employees:
#     print(emp["first_name"])
# i = 0
# while i<len(employees):
#     print(employees[i]["first_name"])
#     i = i+1
A= {1:"one", 2:"two", 3:"three", 4:"four"}
B = {"A": "apple" , "B": "bat" , "c":"cat", "d" :"doll"}
print(A.get(2))
print(B.get("c"))
print(A.get(5)) #this key is not available in dictionary A so return None
print(A.get(5),"key not found") #we can specify our message to display if key not found