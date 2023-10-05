#1
'''list1 = ['red','yellow','pink','white','black']
print(list[::-1])

list1.reverse()
print(list1)

my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list)  # Output: [5, 4, 3, 2, 1]'''
#2
'''l1 = ["m","na","i","fath"]
l2 = ["y","me","s","ima"]   
l3 = []
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)    '''
#3
'''l1 = [1,2,3,4,5,6,7,8,9]
for i in l1:
    print(i**2,end=' ')
'''
#10

# l1 = [1,1,1,4,5,6,7,8,9]
# item1 = 1
# fil1 = [x for x in l1 if x!=item1]
# print(fil1)

# fil2 = list(filter(lambda x :x !=item1,l1))
# print(fil2)

# while item1 in l1:
#     l1.remove(item1)
# print(l1)    

# for item in l1:
#     if item1 == item:
#         l1.remove(item1)
# print(l1)    



# l1 = [1,2,3,4,5]
# l1[0:4]=[11,12,13,14,15]
# print(l1)

# l1 = [1,2,3,4,2,2]
# item_to_replace =2
# new_value = 90
# for i in range(len(l1)):
#     if l1[i] ==item_to_replace:
#         l1[i] = new_value
# print(l1)


#8
'''l1 = [1,2,3,4,5,[6,7,8]]
l1.extend([[9,10]])
print(l1)

nested_list = [1,2,3]
new_sub_list =[4,5]
nested_list+=[new_sub_list]
print(nested_list)
'''
#7
'''l1 = [1,2,3,2]
specified = 2
number = 1111111111111111111111
index = l1.index(specified)
l1.insert(index+1,number)
print(l1)
'''
#6
l2 = ["s","","e","f","E","w","q","b"]
l3 = [i for i in l2 if i!=""]
print(l3)


list1 = [1,2,3]
list2 = ['a','b','c']
for item1,item2 in zip(list1,list2):
    print(item1,item2)

help(zip)