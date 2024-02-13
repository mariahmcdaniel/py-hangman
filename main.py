import hangman_words
import random

while True:
    try:
        category = int(input("\n\n                Choose A Category!\n\n1:Food & Beverage \n2:Animals\n\n"))
        if category == 1 or category == 2:
            break
    except ValueError:
        print("\n\n\nInvalid Input. Try again")
    else:
        print("\n           Please enter either 1 or 2!")

if category == 1:
    word_pool = hangman_words.food_pool
    print("Great, you chose Food and Beverage")
elif category == 2:
    word_pool = hangman_words.animal_pool
    print("Great, you chose Animals")

word_index = random.randint(0,len(word_pool)-1)

secret_word = word_pool[word_index]

# print(secret_word)
word_l = list(secret_word)

letter_count = len(word_l)

# print(word_l)
turns_left = 10
letter_bank = "A B C D E F G H I J K L M\nN O P Q R S T U V W X Y Z"
print(letter_bank)
letter_l = letter_bank.split()
print(letter_l)
while turns_left >= 0:
    while True:
        try:
            player_guess = str(input("Choose A Letter:"))
            for letter in word_l:
                if player_guess.casefold() == letter:
                    print("match")
                else:
                    print("No")
            turns_left = int(turns_left) - 1
            break        
        except ValueError:
            print("\n\n\nInvalid Input. Try again")



