#Generate 3 random integers between 100 and 999 which is divisible by 5***************
# import random 
# for i in range (3):
#     x = random.randrange(100,1000,5)
#     print(x, end=" ")
#Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
# import random
# lottery_ticket_list = []
# for i in range (100):
#     lottery_ticket_list.append(random.randrange(1000000000, 9999999999))

# winnes = random.sample(lottery_ticket_list,2)
# print(winnes)    
# import random

# aList = [20, 40, 80, 100, 120]
# sampled_list = random.sample(aList, 3)
# print(sampled_list)

#Generate 6 digit random secure OTP
'''import secrets
secretsGenerator = secrets.SystemRandom()
print("generating 6 digit random otp :")
otp = secretsGenerator.randrange(1000,9999)
print(otp)'''
#Pick a random character from a given String
'''import random
L = ["Rahul","sonia","Priyanka"]
if len(L)>5:
    print(random.choice(L))'''
#Calculate multiplication of two random float numbers
import random
num1 = random.random()
print(num1)
num2 = random.uniform(9.5,99.5)
print(num2)
num3 = num1*num2
print(num3)

   