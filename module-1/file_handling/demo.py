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
# import os
# if os.path.exists("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("file does not exist")

# import os 
# os.rmdir("m")

# import json
# print(json.dumps({"name":"fathima","age":10}))
# print(json.dumps(["apple","banana","orange"]))
# print(json.dumps(("apple","banana","orange")))
# print(json.dumps("hello!"))
# print(json.dumps(70))
# print(json.dumps(78.44))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

import json
x = {
     "name": "John",
  "age": 30,
  "avail": True,
  "loc": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))




