file = open("data1.txt","w")
file.write("Hello Hw are you")
file.write("Hw is your studies?")
file.close()  # Close the file after reading
    
if file.closed:
    print("The file is closed.")
else:
    print("The file is not closed.")
print(file.name)    