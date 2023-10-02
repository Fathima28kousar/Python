#1
'''num1 = 10
num2 = 20
print(num1+num2)'''

#2
'''x,y = input("Enter 2 values with space in between: ").split()
print("No. of boys: ",x)
print("No. of girls: ",y)
'''

'''a,b = input("Enter values : ").split()
print("first number is {} and the second number is {}".format(a,b))'''

'''x = list(map(int,input("Enter the values: ").split()))
print("List is: ",x)'''

'''
x = [str(x) for x in input("Enter the values: ").split()]
print("No. of lists are : ",x)'''

#3
'''num = int(input("Enter the number: "))
if num%7==0:
    print("Number is divisible by 7")

else:
    print("Not divisible by 7")'''

#4
'''num = int(input("Enter the number: "))
if num%3==0:
    print("Number is divisible by 3")

else:
    print("Not divisible by 3")
'''
#5
'''num = int(input("Enter the number: "))
if num>0:
    print("Number is positive")

elif num<0:
    print("Number is negative")

else:
    print("Number is Zero")'''

#6
'''num = int(input("Enter the number: "))
letters = ["","one","two","three","four","five","six","seven","eight","nine"]
def convert_to_words(num):
    if num==0:
        return "zero"
    elif num<10:
        return letters[num]
words = convert_to_words(num)
print(words)'''

#7
'''num = (input("Enter the number: "))
if len(num)!=3:
    print("Please enter a 3-digit number")
else:
    # print(num[1])
    print(int(num)%100//10)'''

#8
'''n = int(input("Enter the number: "))
even_numbers = []
odd_numbers = []

for i in range(1,n+1):
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("Even numbers are: ")
for even in even_numbers:
    print(even)

print("Odd numbers are: ")
for odd in odd_numbers:
    print(odd)'''

#9
'''num1 = int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))
if num1>num2:
    print(num1," is greater than ",num2)

else:
    print(num2," is greater than ",num1)'''

#10
'''num1 = int(input("Enter 1st number: "))
num2= int(input("Enter 2nd number: "))
if num1<num2:
    print(num1," is lesser than ",num2)

else:
    print(num2," is lesser than ",num1)'''

#11
'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3= float(input("Enter the third number: "))
greatest = max(num1, num2,num3)
print("The greatest number is:", greatest)'''

#12
'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
numbers = [num1, num2, num3]
numbers.sort()
print("Ascending ordered numbers are: ",numbers)'''
#13
'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
numbers = [num1, num2, num3]
numbers.sort(reverse=True) 
print("Ascending ordered numbers are: ",numbers)'''

#14
#15
#16,17-to be continued

