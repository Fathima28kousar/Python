'''import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/comments?10")
users_lists = response.json()
print(type(users_lists))
print(users_lists)
for user in users_lists:
    print(user["id"],user["email"])

    fp = open("user.json","w")
    json.dump(users_lists,fp)
fp.close()'''

# import
#  mysql.connector
# connection = mysql.connector.connect(host="localhost",user="root",password="FKW#84#kousar",database="fathima" )
# cursor = connection.cursor()

# create_table_query = """
# CREATE TABLE IF NOT EXISTS table1(
# id INT PRIMARY KEY,
# name VARCHAR(255),
# age INT
# )
# """
# cursor.execute(create_table_query)

# insert_data_query ="""
# INSERT INTO table1(id,name,age)
# VALUES(%s,%s,%s)
# """

# data_to_insert =[
#     (101,"john",30),
#     (102,"bear",32),
#     (103,"grils",33),
#     (104,"gordan",20),
# ]

# cursor.executemany(insert_data_query,data_to_insert)

# connection.commit()
# cursor.close()
# connection.close()

'''import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code ==200:
    data = response.json()
    fp = open("data.csv","w", newline='')
    csv_writer = csv.writer(fp)
    if len(data)>0:
        header = data[0].keys()
        csv_writer.writerow(header)

        for item in data:
            csv_writer.writerow(item.values())
    fp.close()
    print("API has been written",data)
else:
    print("Api request failed",response.status_code)'''


'''
API URL: https://dummyjson.com/products/1
Method Type:GET
AccessType:Public 
Requied filed: None
'''
# #invokie Rest api and print user names
# import requests 
# import json 

# response=requests.get('https://jsonplaceholder.typicode.com/users')

# users=response.json()
# print(type(users))
# print(users)

# for user in users:
#     #print(type(user))
#     print(user['name'])

#invoke rest api and write into new json file
#invoke rest api and write into new json file
# '''import random 

# name = input("What is your name? ")
# print("Good Luck ",name,"!")

# words = ["apple","hello","hi"]
# word = random.choice(words)

# guesses = " "

# turns=10
# while turns>0:
#     failed=0

#     for char in word:
#         if char in guesses:
#             print(char,end="")

#         else:
#             print("_",end=" ")
#             failed+=1
        
#     if failed ==0:
#         print("\n\'you win\' ")
#         print("The word is ",word)
#         break

#     print()

#     guess = input("Enter the character: ")
#     guesses +=guess
#     guess = guess.lower()

#     if guess not in word:
#         turns-=1
#         print("Wrong")
#         print("You have ",turns,"more turns")

#         if turns ==0:
#             print("You loose!")
#             print("The correct word is: ",word)'''

import random
from collections import Counter

someWords = '''
apple banana mango strawberry
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon
'''

someWords = someWords.split()
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: The word is a name of a fruit')

    for i in word:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while chances != 0 and flag == 0:  # Flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guessed letter is added as many times as it occurs

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif Counter(letterGuessed) == Counter(word):
                    # The game ends, even if chances remain
                    print("The word is:", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                    break  # To break out of the while loop
                else:
                    print('_', end=' ')

        # If user has used all of their chances
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')


        