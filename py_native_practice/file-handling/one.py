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

