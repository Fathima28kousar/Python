def add(first,second):
    return(first + second)

def subtract(first,second):
    return(first - second)
    
def multiply(first,second):
    return(first * second)
    
def divide(first,second):
    return(first / second)

def remainder(first,second):
    return(first % second)

try:   
    first = int(input("Enter the first number: "))
    op = input("Enter the operation (add,subtract,multiply,divide,remainder): ").lower()
    second = int(input("Enter the second number: "))

    if op == "add":
        print(f"Result is: {add(first,second)}")
    elif  op == "subtract":
        print(f"Result is: {subtract(first,second)}")
    elif  op == "multiply":
        print(f"Result is: {multiply(first,second)}")
    elif  op == "divide":
        print(f"Result is: {divide(first,second)}")
    elif  op == "remainder":
        print(f"Result is: {remainder(first,second)}")
        

except :
    print("Something went wrong")


