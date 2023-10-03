'''import re 
text = 'On 2023-02-23 ,the conference was held . The event began on 2023-05-09'
pattern = r'\d{4}-\d{2}-\d{2}'
dates = re.finditer(pattern,text)
for date in dates:
    print(date)'''
'''
import re 
pattern = 'python'
data = 'python is a powerfull programming language. Python is easy, python has more features.'
match = re.finditer(pattern,data,re.IGNORECASE)
for d in match:
    print(d.start())'''
'''import re 
pattern = 'python'
data = 'python is a powerfull programming language. Python is easy, python has more features.'
match = re.findall(pattern,data,re.IGNORECASE)
print(match)'''

'''import re 
pattern = re.compile(r'python',re.IGNORECASE)
data = 'python is a powerfull programming language. Python is easy, python has more features.'
match = re.finditer(pattern,data)
for m in match :
    print(m)'''

'''import re 
pattern = 'ab'
data = 'abababaaba'
match = re.finditer(pattern,data,re.IGNORECASE)
for m in match:
    print(m)
'''
# import re 
# pattern = re.compile(r'ab',re.IGNORECASE)
# data = 'ababaaba'
# match_iter = re.finditer(pattern,data)
# count = 0
# for matchs in match_iter:
#     count+=1
#     print(matchs)
# print(count)

'''import re 
pattern = re.compile(r'ab',re.IGNORECASE)
data = 'ababaaba'
match_list = re.findall(pattern,data)
print(match_list)'''

'''import re
pattern = r'dog|cat'
data = "I saw a Dog running behind a cat and the cat climbed the wall but the dog couldn't "
match_iter = re.finditer(pattern,data,re.IGNORECASE)
count = 0
for matchs in match_iter:
    count+=1
    print(matchs)
print(count)'''

'''import re 
data = 'bbbabb'
pattern = 'bb'
match = re.findall(pattern,data)
print(match)'''

'''import re 
data = 'bbbabb'
pattern = 'bb'
match = re.finditer(pattern,data)
for ma in match:
    print(ma)'''
