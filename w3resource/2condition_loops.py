#1
'''num = []
for x in range(1500,2701):
    if x%7 ==0 and x%5 == 0:
        print(x,end=" ")'''

#2
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
def print_full_name(first, last):
    return(f"Hello {first} {last}! You just delved into python")
