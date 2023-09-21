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
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range (n):
        a.append(i)
    for i in a:
        print(i**2,end="\n")    