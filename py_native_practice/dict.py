#**************** Convert two lists into a dictionary******************************************
'''keys = [1,2,3]
values = ["one","two","three"]
new_dict = dict(zip(keys,values))
print(new_dict)'''
#**************** Merge two Python dictionaries into one******************************************
'''dict1  = {"Ten":10, "Twenty":20, "Thirty":30}
dict2 = {"Fourty":40, "Fifty": 50, "Sixty": 60}
dict1.update(dict2)
print(dict1)  #dict1 gets updated
print(dict2)
'''
#****************  Print the value of key ‘history’ from the below dict******************************************
'''sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
sampleDict = {     "class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80 }}  }}
print(sampleDict["class"]["student"]["marks"]["history"])'''
#****************Initialize dictionary with default values******************************************
'''employees = ["kelly","emma"]
defaults = {"designation":"Developer","salary":8000}

new = dict.fromkeys(employees,defaults)
print(new)
print(new["kelly"])
'''
#********Create a dictionary by extracting the keys from a given dictionary****************************
'''sample_dict = {
    "name" : "kelly",
    "age": 25,
    "salary":1000,
    "city": "new york"
}
keys = ["name","salary"]

newDict = {k: sample_dict[k] for k in keys }
print(newDict)'''
#**************************Delete a list of keys from a dictionary*************************
'''emp = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary","age"]

for k in keys :
    emp.pop(k)
print(emp)'''    
#******************Check if a value exists in a dictionary************************
'''dict = {"a":100 , "b" : 200 , "c" :300}   
print(dict.values())
if 200 in dict.values():
    print("200 is present in dict")
else:
    print("200 is not present in a dict")    '''
#****************Rename key of a dictionary**********************
'''sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict.pop("city") 
sample_dict["location"] = "New york"
print(sample_dict)
                '''
#***************Get the key of a minimum value from the following dictionary#***************
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))                
         
#****************Change value of a key in a nested dictionary#****************        
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}    

sample_dict["emp3"]["salary"] = 8500
print(sample_dict)
