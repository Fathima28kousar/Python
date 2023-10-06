#1
'''import re
data = 'abcXYZ123'
pattern = '^[a-zA-Z0-9]'
match = re.findall(pattern,data)
if match :
    print("The string contains only allowed characters")
else:
    print("The string contains characters other than a-z,A-Z and 0-9")
'''
#2
# import re 
# data = 'am good how about you a000bb'
# pattern = 'a0b'
# match = re.findall(pattern,data,re.IGNORECASE)
# print(match)


# import re
# def text_match(text):
#     pattern = r'[a-z]'
#     if re.search(pattern,text):
#         return("match found")
#     else:
#         return("match not found")
# print(text_match('hello hw are you 98674953498'))

'''import re 
input = 'full stack developer'
found = re.search('stack',input)
if found:
    print("match found")
else:
    print("match not found")

print(found.group())
print(found.start())
print(found.end())'''

