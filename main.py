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

print(word_l)

player_guess = input("Choose a letter:")

for letter in word_l:
    if player_guess.casefold() == letter:
        print("match")
    else:
        print("No")
            

