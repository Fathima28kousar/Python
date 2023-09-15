import random

fruits = [
    "apple", "banana", "mango", "pineapple", "strawberry",
    "watermelon", "papaya", "grapes", "orange", "lemon",
    "coconut", "muskmelon", "peach", "apricot"
]

word = random.choice(fruits)

if __name__ == '__main__':
    print("Guess the word! Hint: The word is a name of a fruit")

    guessed_letters = ""
    chances = len(word) + 2
    flag = False

    while chances > 0 and not flag:
        print("\nChances are:", chances)
        print("You guessed-",guessed_letters)
        chances -= 1

        guess = input("Enter a letter to guess: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print('Please enter a single letter.')
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters += guess

        if guess in word:
            for char in word:
                if char in guessed_letters:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
            if set(word) == set(guessed_letters):
                print("\nThe word is:", word)
                flag = True
                print("Congratulations! You won!")
        else:
            print("Incorrect guess. Try again.")

    if not flag:
        print('\nYou ran out of chances.')
        print('The word was:', word)
