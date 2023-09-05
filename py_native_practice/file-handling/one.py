'''f = open("story.txt", "r")
content = f.read()
m = content.split()
f.close()

c = 0

for i in m:
    if i=="Me" or i=="My" or i=="me" or i=="my":
        c+=1

print("Character count is:", c)'''
'''def myfunc():
    f = open("story.txt","r")
    content = f.read()
    m = content.split()
    c  = 0
    for i in m:
        e = i.lower()
        if e=="a" or e=="m":
            c +=1
    print("the no. of occurences are: ",c)        
myfunc()    
'''
# f = open("story.txt","r")
# c = 0
# d = f.readlines()
# for i in d:
#     if i[0] == "A":
#         c = c+1
#     print("Lines starting from A are :",c)

# f = open("story.txt", "r")
# c = 0
# d = f.readlines()
# for i in d:
#     if i[0] == "A":
#         c = c + 1

# print("Lines starting with 'A':", c)

# f.close()  # It's important to close the file when you're done with it.
    

# def count_lines_starting_with_a(file_path):
#     with open(file_path, "r") as file:
#         c = 0
#         d = file.readlines()
#         for i in d:
#             if i.strip()[0].lower() == "a":
#                 c += 1
#         return c

# # Specify the file path
# file_path = "story.txt"

# # Call the function to count lines starting with "A"
# count = count_lines_starting_with_a(file_path)

# print("Number of lines starting with 'A':", count)


'''f = open("story.txt", "r")
c = 0
d = f.readlines()
for i in d:
    if i[0] == "A":
        c = c + 1
f.close()


print("Number of lines starting with 'A':", c)'''


'''def displaywords():
    f = open("story.txt","r")
    d = f.read()
    m = d.split()
    for i in m:
        if (len(i)<=4):
            print(i)
displaywords()'''

# def lowercase():
#     f = open("story.txt","r")
#     d = f.read()
#     c = 0
#     for i in d:
#         if i.islower():
#              c = c+1    
#     print("total lowercase char are: ",c)
# lowercase()


# print(bin(25))
# print(bin(31))
# print(bin(65))
'''class Bank:
    bank_name = "BOI"
    rate_of_interest = 12.25
    @staticmethod
    def simple_interest(prin,n):
        si = (prin*n*Bank.rate_of_interest)/100
        print(si)
prin = float(input("Enter principal amount : "))
n = int(input("Enter no. of years: "))
Bank.simple_interest(prin,n)
'''

# file = open("roll.txt","w")
# for i in range(2):
#     name = input("Enter name : ")
#     roll_number = input("Enter roll number : ")
#     file.write("Roll no.: " + roll_number + "\tname: " + name + "\n")
# file.close()    

'''# file = open("story.txt","r")
# data = file.read()
# c = 0
# for i in data:
#     if i=="a":
#         c = c+1
# print("frequency of a is : ",c)'''


# file = open("story.txt","r")
# data = file.read()
# print("total number of characters in data is :" , len(data))


# f = open("story.txt","r")
# data = f.read()
# cm = 0
# ca = 0
# for i in data:
#     if i =="m" or i == "M":
#         cm+=1
#     if i == "a" or i=="A":
#         ca+=1
# print("A for a ",ca ,"\nM for m ",cm)            

'''# f = open("story.txt","r")
# data = f.readlines()
# c = 0
# for i in data:
#     if i[0] =="A" or i[0]=="a":
#         c = c+1
# f.close()
# print("number of A are",c)        
'''
# f = open("story.txt","r")
# data = f.read()
# m = data.split()
# for i in m:
#     if len(i)<=4:
#         print(len(i))     

       

     
