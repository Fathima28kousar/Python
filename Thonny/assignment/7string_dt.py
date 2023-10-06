#1
'''str1 = 'This is a world of python,and its a easiest programming languages on earth.'
vowels = 0
for i in str1:
    if (i=='a' or i=='A' or i=='o' or i=='e' or i=='i' or i=='u'):
        vowels+=1
print(vowels)
'''
#2a
'''str2 = 'hello and this is a 5STAR Hotel The LALIT its located in bangalore and its services and hospitality is spot on'
S=[]
ucase =0
for i in str2:
    if (i.isupper()):
       ucase +=1
       S.append(i)
        
print(S)
print("The number of uppercase letters are:",ucase)

print()
print()'''
#2b
'''str2 = 'hello and this is a 5STAR Hotel The LALIT its located in bangalore and its services and hospitality is spot on'
S =[]
lcase =0
for i in str2:
    if (i.islower()):
       lcase +=1
       S.append(i)
print(S)
print("The number of lowercase letters are:",lcase)
'''
#2c
'''str2 = 'hello and this is a 5 STAR Hotel The LALIT its located in bangalore and its services and hospitality is spot on 123'
S =[]
digits =0
for i in str2:
    if (i.isnumeric()):
       digits +=1
       S.append(i)
print(S)
print("The number of digits are:",digits)
'''
#2d
'''str2 = 'hello and this is a 5 STAR Hotel The LALIT its located in bangalore and its services and hospitality is spot on 123'
count = 0
for i in range(len(str2)):
    if str2[i] ==" ":
        count+=1
print(count)
'''
#3
'''string1 = input("Enter the word: ")
print(string1[::-1])
print(type(string1[::-1]))
print(list(reversed(string1)))'''
#4
'''string1 = input("Enter the word: ")
print(string1[::-1])'''
#5
# string1 = 'stack'
# print(string1[1:]+string1[0])
# print(string1[2:]+string1[0:2])
# print(string1[3:]+string1[0:3])
# print(string1[4]+string1[0:4])
# # print(type(string1[1:]+string1[0]))
'''def rotate(input_str):
    length = len(input_str)
    
    # Iterate through the string and rotate it
    for i in range(length):
        rotated_str = input_str[i:] + input_str[:i]
        print(". " + rotated_str)

input_str = "stack"
rotate(input_str)'''
#6
'''str = input("Enter the string: ")
str2 = str[1:]+str[0]
print(str2)
'''


