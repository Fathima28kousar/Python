first = input("enter first number: " )
operator = input ("enter operator (+,-,/,%) : ")
second = input("enter second number : ")

first = int(first)
second = int(second)


if operator == "+":
    print(first + second)
    
elif operator == "-":
    print(first - second)

elif operator == "/":
    print(first / second)

elif operator == "%":
    print(first % second)
    
else:
    print("Invalid input")    
    
    
 first = int(input("Enter the first number: "))
op = input("Enter the operator [+,-,/,%,*]: ")
second = int(input("Enter the second number: "))
if op == "+":
    print(first+second)
elif  op == "-":
    print(first-second)
elif  op == "/":
    print(first/second)    
elif  op == "%":
    print(first%second)
elif  op == "*":
    print(first*second)   
else:
    print("invalid statement")          