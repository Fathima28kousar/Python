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
import json
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
print(dict["email"])