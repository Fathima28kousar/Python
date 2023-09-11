
'''a = 10
b = 5
c = 0
try:
    result = a/c
    print(result)
except:
    result = a/1
    print(result)

print("GM")'''


'''filename = input("Enter File name: ")   

try:

    fp = open(filename,"r")
    data = fp.read()

except:
    fp = open("emp.json","r")
    data = fp.read()   
    print("except block")'''



'''filename = input("Enter file name :")
try:
    fp = open(filename,"r")
    data = fp.read()
    print(data)

except:
    print("except bolck exe")
    fp = open("emp.json","r")
    data = fp.read()   
    print(data) '''



'''filename= input("Enter file Name:")

try:
    fp=open(filename,'r')
    data = fp.read()
    print(data)
except FileNotFoundError as fnf:
    print(fnf)


print("GM")
#FileNotFoundError'''


'''try:
    f = open("test.file.txt")
except:
    print("sorry file does not exist")
'''
print("Enter num1")
num1 = input()
print("Enter num2")
num2 = input()

try:
    print("the sum of these two numbers is",int(num1)+int(num2))

except Exception as e:
    print(e)

print("this line is very important")
