'''file = open("file.txt","w")
age =input("Enter your age :")
file.write("Your age is :")
file.write(age)
file.close()
'''
'''f = open("data.txt","w")
f.writelines(["Amit\n","anita\n","ajay\n"])
f.close()'''

'''f = open("data1.txt","w")
f.write("Welcome to  \n")
f.write("my website\n")
f.write("www.csilearning.com")
f.close()'''

'''f= open("data2.txt","w")
f.writelines(["Welcome to  \n","my website\n","www.csilearning.com"])
f.close()'''

'''f= open("data2.txt","w")
f.write("Hello world\n")
f.close()'''

# file = open("roll.txt","w")
# roll_number =input("Enter  roll_number :")
# marks =input("Enter  marks :")
# file.write("Your marks are\t\t")
# file.write(marks)
# file.write("Your roll_number is\t\t")
# file.write(roll_number)
# file.close()
'''
f = open("data.txt","r")
d = f.read()
f.close()

f = open("data.txt","a+")
f.write("\n subscribe to my site\n")
f.write("Text file handling in python\n")
f.write("its a topic or sub- topic\n")
f.close()
'''
'''f = open("data1.txt","a")
f.write("Roll number\t\t")
f.write("Name\n")
f.write("Rahul\t\t")
f.write("2\t\t")
f.write("Rahul\t\t")
f.write("2\t\t")
f.write("Rahul\t\t")
f.write("2\t\t")
'''

# Open the file in read mode
file = open("data.txt", "r") 
content = file.read()
file.close()

# Initialize counters
vowel_count = 0
space_count = 0
word_count = len(content.split())  # Split the content into words
a_frequency = 0
text_frequency = 0

# Loop through the content character by character
for char in content:
    if char.lower() in "aeiou":
        vowel_count += 1
    elif char == ' ':
        space_count += 1
    if char.lower() == 'a':
        a_frequency += 1

# Split the content into words and count the frequency of 'Text'
words = content.lower().split()
text_frequency = words.count("text")

# Print the results
print("Number of vowels:", vowel_count)
print("Number of spaces:", space_count)
print("Number of words:", word_count)
print("Frequency of 'a':", a_frequency)
print("Frequency of 'Text':", text_frequency)
