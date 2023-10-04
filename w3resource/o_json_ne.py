#1
'''import json
string1 = """{
  "id": 1,
  "first_name": "Claudetta",
  "last_name": "Laybourn",
  "email": "claybourn0@uol.com.br",
  "gender": "Female",
  "ip_address": "204.174.237.154"
}"""
dict = json.loads(string1)
print(dict)
print(dict["id"])
print(dict["first_name"])
print(dict["last_name"])
print(dict["email"])'''
#2
'''import json
dict = {
  'id': 1,
  'first_name': 'Claudetta',
  'last_name': 'Laybourn',
  'email': 'claybourn0@uol.com.br',
  'gender': 'Female',
  'ip_address': '204.174.237.154'
}
print(type(dict))
string = json.dumps(dict)
print(type(string))
print(string)
'''
#3
'''import json
string1 = """{
  "id": 1,
  "first_name": "Claudetta",
  "last_name": "Laybourn",
  "email": "claybourn0@uol.com.br",
  "gender": "Female",
  "ip_address": "204.174.237.154"
}"""
dict = json.loads(string1)
print(dict)
print(dict["id"])

print(dict["first_name"])
print(dict["last_name"])
print(dict["email"])'''
#4
'''import json
dictionary = {
  "first_name": "Claudetta",
  "id": 1,
  "last_name": "Laybourn",
  "email": "claybourn0@uol.com.br",
  "gender": "Female",
  "ip_address": "204.174.237.154"
}
json_object = json.dumps(dictionary,indent=4,sort_keys="True")
print(json_object)
'''
#5
'''import json
json_dict = '{"name":"fathima","age":6,"class":12,"availability":"True"}'
jobj_list =   '["red","green","blue"]'
jobj_string = '"python string"'
jobj_int = '12345'
jobj_float =  '21.34'

python_dict = json.loads(json_dict)
python_list = json.loads(jobj_list)
python_string = json.loads(jobj_string)
python_int = json.loads(jobj_int)
python_float = json.loads(jobj_float)

print(python_dict)
print(python_list)
print(python_string)
print(python_int)
print(python_float)
'''
#6
'''import json
file=open('existing_data.json', 'r')
existing_data = json.load(file)

existing_data['new_key'] = 'new_value'

new_file = open('new_data.json', 'w')
json.dump(existing_data, new_file, indent=4)
print("New JSON file created successfully.")'''
import json
json_object = '{"a":1,"a":4,"b":2,"b":3}'
python_obj=json.loads(json_object)
print(python_obj)
print(type(python_obj))


 

