x = "hello World"

def myfunc():
    print("This is " + x)
    
myfunc()

x = "hi"

def myfunc():
    x = "hello"
    print("this is " + x)
    
myfunc()
print("this is " + x)

x = "awsome"

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("python is " + x)

