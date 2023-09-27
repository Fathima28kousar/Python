#1
'''for i in range(1,11):
    print(i)'''
#2
'''i=1
while i<=10:
    print(i)
    i = i+1'''
#3
'''sum_for =0
for i in range(1,11):
    sum_for+=i
print("Sum for first natural numbers is",sum_for)  '''  


'''sum_while = 0
i = 1
while i <= 10:
    sum_while += i
    i += 1

  
print("Sum using while loop:", sum_while)'''
#4

'''for i in range(15,9,-1):
    print(i)
'''
#5
'''print()
i=15
while i>=10:
    print(i)
    i-=1 ''' 
#6
i=0
'''while i<=20:
    i+=1
    if i%2==0:
        print(i)
'''
#7
'''for i in range(21):
    if i%2==0:
        print(i)'''
#8
'''i = 0
while i<=20:
    i+=1
    if i%2 !=0:
        print(i)
'''
#9
'''for i in range(10):
    if i%2 !=0:
        print(i)'''
#11
'''for i in range(1,41):
    if i%4 ==0:
        print(i)'''
#12
'''i = 0
while i<=50:
    i+=1
    if i%5 == 0:
        print(i)'''
#13
'''number = 6
for multiplier in range(1, 11): 
    result = number * multiplier
    print(result)

'''
#14
'''number =6
i = 1
while i<=10:
    result = i*number
    print(result)
    i+=1
'''
#15
'''number = 24
i =1
while i<= number:
    if number % i == 0:
        print(i,end=" ")
    i += 1

number =24
for i in range(1,number+1):
    if number % i ==0:
        print(i,end=" ")'''
#16
'''num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    remainder = num % 10
    reverse= reverse * 10 + remainder
    num = num // 10
print("Reverse of the digits:", reverse)'''
#17
'''list = [1,23,4,5,6,73,56,3]
for i in list:
    if i%2 == 0:
        print(i,end=" ")'''

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 2) + fibo(n - 1)

n = int(input("Enter no. of terms: "))
for i in range(1, n + 1):
    print(fibo(i), end=" ")



#19
'''num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
'''
