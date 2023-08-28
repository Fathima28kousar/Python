# import json 
# f = open("one.json","r")
# emp_json_string =json.load(f)
# print(emp_json_string)
# print(type(emp_json_string))
# for k,v in emp_json_string():
#     print(k,v)


# import json
# emp_json_string='''{"id": 101, "name": "Rahul", "salary": null, "avail": true}'''
# #conver into json string to pyton dict

# print(emp_json_string)
# print(type(emp_json_string))
# emp_dict=json.loads(emp_json_string)
# print(emp_dict)
# print(type(emp_dict))
# import json

# with open('one.json', 'r') as f:
#     emp_list = json.load(f)
    
# print(emp_list)
# print(type(emp_list))

# # Iterate through list of dictionaries
# for emp_dict in emp_list:
#     for key, value in emp_dict.items():
#         print(f"{key}: {value}")

# import json

# f= open('one.json','r')
# emp_list=json.load(f)
# print(emp_list)
# print(type(emp_list))

# #print dict object key,values
# for emp_dict in emp_list:
#     for key , value in emp_list.items():
#         print(key,":",value)

import json 
emp_dict = {
    "id":101,
    "name": "rahul",
    "salary":True,
    "avail": None,
}

print(emp_dict)
print(type(emp_dict))

emp_json = json.dumps(emp_dict)
print(emp_json)
print(type(emp_json))

