#1
'''num = []
for x in range(1500,2701):
    if x%7 ==0 and x%5 == 0:
        print(x,end=" ")'''

#2
''''''''''def convert_temperature(value,unit):
    if unit == "C" or "c":
        return (value*9/5) +32
    elif unit == "F" or "f":
        return (value-32) *5/9
    else:
        return None
unit = input("Enter the unit (C or F): ")
value = float(input("Enter the temperature value: "))
converted_value = convert_temperature(value,unit)

if converted_value is not None:
    print(f"{value} {unit} is equal to {converted_value:.2f} {'F' if unit == 'C' else 'C'}")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")'''''''''

#3
'''import random
secret_number = random.randint(1,10)
while True:
     num = int(input("Enter "))
     if num == secret_number:
          print("Well guessed!")
          break
     else:
          print("Try again")
'''
#4
'''rows = int(input("Enter the number of rows: "))
for i in range(1,rows):
    for j in range(1,i+1):
        print("_",end=" ")    
    print()

for i in range(rows,0,-1):
    for j in range(i):
        print("_",end=" ")
    print()
'''
#5
'''word = str(input("Enter a word: "))  
reversed_word = word[::-1]
print("Reversed word is", reversed_word)'''

#6
'''numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
count_odd = 0
count_even = 0 
for i in numbers:
    if i %2==0:
        count_even+=1   
        
    else:
        count_odd+=1
    
print("even numbers are: ",count_even)
print("odd numbers are",count_odd)'''

#7
'''datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for i in datalist:
    print(type(i))'''

#8
'''if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range (n):
        a.append(i)
    for i in a:
        print(i**2,end="\n")    '''
#9
'''def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input("Enter the number of terms: "))
for i in range(1, n + 1):
    print(fibo(i), end=" ")'''


#10
'''for i in range(51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        continue
    elif i%3==0:
        print("Fizz")
        continue
    elif i%5==0:
        print("Buzz")
        continue
    print(i)'''
#12
'''L =[]
while True:
    line = input("Enter a sequence (or 'q' to quit):")
    if line.lower() =='q':
        break
    L.append(line.lower())
print("Sentences in lowercase: ")
for sentence in L:
    print(sentence)'''
'''binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ")
binary_list = binary_numbers.split(',')
divisible_by_5 = []
for binary in binary_list:
    decimal_number = int(binary, 2)
    if decimal_number % 5 == 0:
        divisible_by_5.append(binary)
result = ','.join(divisible_by_5)
print("Numbers divisible by 5:", result)'''
#13
'''num = int(input("Enter the 4 digit binary numbers separated by comas: "))
num_list = num.split(',')
divisible_by_5 =[]
for num in num_list:
    decimal = int(num,2)

    if decimal%5==0:
        divisible_by_5.append(num)
result = ','.join(divisible_by_5)
print("Numbers divisible by 5: ",result)'''
#14
'''inp = input("Enter your desired sentences: ")
letters =[]
digits = []
count1 = 0
count =0
for i in inp:
    if i.isalpha():
        count+=1
        letters.append(i)
    if i.isnumeric():
        count1+=1
        digits.append(i)
print(letters)
print("the number of letters are: ",count)
print(digits)
print("the number of digits are: ",count1)'''
#15
'''import re
p= input("Input your password: ")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")'''
''''''
#16
'''L =[]
for i in range(100,401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
        L.append(s)
print(','.join((L)))'''
#31
'''human = float(input("Enter the human years: "))
if human<0:
    print("Age must be postitve: ")
    exit()
elif human<=2:
    dog = human*10.5
else:
    dog = 21 +(human-2)*4
print("dogs age in dog years is:",dog)'''
#32
'''inputt = input("enter: ")
if inputt == 'a' or inputt == 'e' or inputt == 'i' or inputt == 'u'or inputt == 'o':
    print(inputt,"is a vowel")
else:
    print(inputt,"is a consonant")'''
#33
'''month = input("Enter the month: ")
if  month== "February":
    print("28/29 days")
elif month in ("April", "June", "September", "November"):
    print("30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
    print("31 days")
else:
    print("Wrong month")'''
#34
'''def sum(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sum(10,6))
print(sum(17,5))
'''
#35
'''str = input("Enter the number: ")
if str.isnumeric():
    print("It is an interger")
else:
    print("It is not an integer")
'''
#36    
'''print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
if x==y==z:
    print("Equalene triangle")
elif x==y or y==z or z==x:
    print("Isosceles triangle")
else :
    print("Scalene triangle")
'''
#37
print("The months are: J")
month = input("Enter the month: ")
day = int(input("Enter the day: "))
if month in ('January', 'February', 'March'):
    season='winter'
elif month in ('April', 'May', 'June'):
    season = 'spring'
elif month in ('July', 'August', 'September'):
    season = 'summer'
else:
    season ='autumn'
if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)

# m = int(input("Enter the number of rows: "))
# n = int(input("Enter the number of columns: "))
# i = range(0,m-1)
# j = range(0,n-1)
# print(i*j)
# lines = []
# for i in range(2):
#     l=input()
#     print(l)
# print(l)

#44
'''num = int(input("Enter the number: "))
for i in range(num):
    for j in range(i):
        print(j+1,end=" ")
        
    print()
	'''
#40
'''import statistics
while True:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))
    print("The median is: ",statistics.median([n1,n2,n3]))
    input_ =input("Enter 0 to finish: ")
    if input_== "0":
        break'''




# for row in range(7):
#     for col in range(5):
#         if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
#             print("*",end="")

#         else:
#             print(end=" ")

#     print()


# for row in range(7):
#     for col in range(5):
#         if (col==0 ) or (col==4 and (row!=0 and row!=6)):
#             if 
'''def print_full_name(first, last):
    return(f"Hello {first} {last}! You just delved into python")'''

