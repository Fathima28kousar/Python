# p = 7
# e = 5
# t = p *5 + e*2
# print(t)
# print("total cost paid by ananya is: ", t)

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
print(my_list[0])
print(my_list[1])
print(my_list[2])
for x in my_list:
    print(x)

# mylist = [1,2,3]
# print(mylist[10])

numbers = []
strings = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("Hello")
strings.append("world")
print(numbers)
print(strings)
names = ["John","eric","jessica"]
second_name = names[1]
# second_name = None
# names.insert(1,second_name)
# print(names)
print(names[1])
print("The second name on the names list is %s" % second_name )
print("The second name on the names list is " , second_name )

# temp = "5 degrees"
# cel = 0
# fahr = float(temp)
# cel = (fahr -32.0)*5/9.0
# print(cel)

astr = "hello workd"
try:
    istr = int(astr)
except:
    istr = -1
print("first",istr)