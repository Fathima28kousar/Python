'''print("Hello",end = '\n' )
print("Hello", "\n good morning")
print("Bye",end = '\n')
id = 101
ename = "Rahul"
print("employeename:",ename, "employeeid:",  id)
print("Hello", end = '\n') 
print("GM")
print("Hello ", end = "")
print("GM")
id = 101
ename : "Rahul"
print(id,ename)
id = 101
ename = 'Rahul'
print(id,ename,sep=':')
'''
'''
id = 101
ename = "Rahul"
print("Empid", id ,"Empname", ename)
print("Empid{0},Empname{1}.format(id,ename)")
print("Empid{a} and Empname{b}" .format(a=id,b=ename))
'''
'''
Id = input("Enter empId: ")
ename = input("Enter Empname: ")
esal = input("Enter Emp salary: ")
print(type(Id))
print(type(ename))
print(type(esal))
'''
'''a = int(input ("Enter first Number: "))
b = int(input ("Enter second number: "))
print(a+b)
'''
#print(int(input("First no. ")) + int(input("Second no.: "))

#nested if statements
'''num = 7423897

if (num < 0):
    print("Number is negative.")

elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")

else:
    print("Number is zero")
    
    
age = int(input("Enter your present age: "))
if age>18:
    print("You are eligible to vote")
    
else:
    print("You are not eligible to vote")
'''
'''num = int(input("Enter the number: "))
if num % 2 ==0:
    print("Number is even")
else:
    print("Number is odd")
'''

'''num = int(input("Enter the number: "))
if num % 7 == 0:
    print("Number is divisible")
    
else:
    print("Number is not divisible")
'''
#num = int(input("Enter a number:"))
'''if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
'''
'''num = int(input("Enter the number: "))
print(num%10)'''

'''num = int(input("Enter the number: "))
id = num%10
if id%3==0:
    print("Last digit of number is divisible by 3")
else:
    print("last digit of number is not divisible by 3")
'''
'''marks = int(input("Enter the percentage : "))
if marks>90 and marks<=100:
    print("Your grade is A")
if marks>80 and marks<=90:
    print("Your grade is B")
if marks>=60 and marks<=80:
    print("Your grade is C")
if marks<60:
    print("Your grade is D")
if marks>=101:
    print("Invalid input")
'''
'''num = int(input("Enter the number between 0-7 : "))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")    
elif num==3:
    print("Tuesday")    
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thursday")
elif num==6:
    print("Friday")
elif num==7:
    print("Saturday")
else:
    print("Please enter number between 1-7")
'''
'''city = (input("Enter City name: "))
if city.lower() == "delhi":
    print("Monument name is :Red fort")
elif city.lower() == "agra":
    print("Monument name is :Taj Mahal")
elif city.lower() == "jaipur":
    print("Monument name is :Jai Mahal")
else:
    print("Enter the correct city")
'''
'''num = int(input("Enter the number : "))
if num>99 and num<1000:
    print("Entered number is three digit number")
else:
    print("Entered number is not a three digit number")
'''
num = (input("Enter the number : "))
l = len(num)
if l != 3:
    print("Enter three digit number")
else:
    print("Middle digit is",(int(num)%10))

































































































