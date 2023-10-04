#1
'''
JSON is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays
JSON stands for "JavaScript Object Notation." It is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate. JSON is often used to transmit data between a server and a web application as an alternative to XML'''
#2
'''
json
JSON uses a lightweight and easy-to-read syntax ,It uses key-value pairs ,JSON data is enclosed in curly braces {}
JSON is generally more human-readable,easier to parse and generate for both humans and machines
JSON format is used to store and transmit data
JSON is used in modern web development, especially for APIs and data exchange between web servers and web applications.
JSON is independent of any programming language and is a common API output in a wide variety of applications.

xml
XML uses a markup language with tags and attributes, similar to HTML,XML data is enclosed in angle brackets <></> and uses open and close tags 
XML is more verbose and complex and can be less human-readable due to its use of tags and attributes.
XML is used to represent data in a machine readable way
XML has a broader range of applications, including configuration files, data interchange, document markup, and more.
XML is a markup language that provides rules to define any data.'''
#3
'''
JSON has a more straightforward syntax for editing and creating new documents, making debugging errors in your data more accessible. JSON is more flexible than XML - it can be used in many different programming languages, whereas XML can only be used in one programming language simultaneously (usually Java)'''
#4
'''import json
json_string = """
    {
  "first_name": "Audry",
  "last_name": "Lambot",
  "email": "alambot0@wufoo.com",
  "gender": "Genderfluid"
}
"""
python_dict = json.loads(json_string)
print(python_dict)
print(type(python_dict))'''
#5
'''import json
python_dict = {
  "first_name": "Audry",
  "last_name": "Lambot",
  "email": "alambot0@wufoo.com",
  "gender": "Genderfluid"
}
json_str = json.dumps(python_dict)
print(json_str)
print(type(json_str))'''
#6
'''import json
f = open('one.json','r')
dict = json.load(f)
print(dict)
for k,v in dict.items():
    print(k,v)
    print(k)
    print(v)
print(list(dict.keys()))
print(list(dict.values()))'''
#7
'''
Serialization:
Serialization is the process of converting a data structure, such as an object or a complex data type, into a format that can be easily stored, transmitted, or reconstructed later.

Purpose: Serialization is used when you want to represent data as a compact, platform-independent, and human-readable format, like JSON. Serialized data can be stored in files or sent over a network.

Example (Python to JSON): Converting a Python dictionary to a JSON string is an example of serialization:
'''
'''
Deserialization:
Definition: Deserialization is the process of converting serialized data (such as a JSON string) back into a data structure or object that can be manipulated or used in a programming language. In the context of JSON, deserialization means converting a JSON string into a native data structure or object.

Purpose: Deserialization is used to reconstruct data from a serialized format, allowing you to work with the data in a programming language. It is commonly used when reading data from files or receiving data over a network.

Example (JSON to Python): Converting a JSON string back to a Python dictionary is an example of deserialization:
'''
#8 json.loads() method is used to convert a json string to python dict

#9 what is the best way to extract data from a dictionary
'''# list comprehension
data = [
   {"name": "John", "age": 30},
   {"name": "Alice", "age": 25},
   {"name": "Bob", "age": 35}
]
names = [entry["name"] for entry in data]
ages = [entry["age"] for entry in data]'''
'''
looping
data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
names = []
ages = []
for entry in data:
    names.append(entry["name"])
    ages.append(entry["age"])*****************************************************************
'''
'''
map function
data = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}
]
names = list(map(lambda entry: entry["name"], data))
ages = list(map(lambda entry: entry["age"], data))*****************************************************************'''
'''
test_list = [{"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35}]
print("The original list is : " + str(test_list))
key = 'name'
res = [d for d in test_list if key in d.keys()]
print("The filtered Dictionaries : " + str(res))
'''
#10
'''The most common use of the with statement is for file handling. When working with files, you can use the with statement to ensure that the file is properly opened and closed, even if an exception occurs.'''
#11,12 pickling unpickling,serialization and deserialization