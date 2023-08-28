# f = open("demofile.txt","a")
# f.write("Now file has more content")
# f.close()

# f= open("demofile.txt","r")
# data = f.read()
# print(data)
'''f = open("demofile3.txt","w")
f.write("good content!!")
f.close()

f = open("demofile3.txt","r")
print(f.read())'''
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("file does not exist")

import os 
os.rmdir("m")