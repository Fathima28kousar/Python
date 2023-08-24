#***********Display three string “Name”, “Is”, “James” as “Name**Is**James”***********************************
# print("Name","is","James", sep="**")

#***********Convert Decimal number to octal using print() output formatting***********
# print(oct(8))
# print('%o' % 8)


#***********Display float number with 2 decimal places using print()******
# num = 233.678909876
# print('%.2f' % num)


#***********Accept a list of 5 float numbers as an input from the user#***********
# numbers = []
# for i in range(6):
#     print("Enter the number ",i,": ")
#     item = float(input())
#     numbers.append(item)
# print("The list is : ",numbers)    

##Write all content of a given file into a new file by skipping line number 5
# num = []
# for i in range(10):
#     if i%3==0:
#         continue
#     print("Line",i)

# print("Bye")    

#***********Accept any three string from one input() call#***********

# str1,str2,str3 = input("Enter three words with space : ").split()
# print(str1)
# print(str2)
# print(str3)

# eid = 101
# ename = "Rahul"
# esal = 45000
# ("empid empname sal".format())
# # print("Employee Id",eid)
# print("Employee Id {0} and Employee Name {1} {2}".format(eid,ename,esal))

totalMoney = 1000
quantity = 3
price = 450
statement = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars"
print(statement.format(totalMoney,quantity,price))