import hangman_art
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
    print("Great, you chose Food and Beverage\n\n\n")
elif category == 2:
    word_pool = hangman_words.animal_pool
    print("Great, you chose Animals")

word_index = random.randint(0,len(word_pool)-1)

secret_word = word_pool[word_index].upper()

# print(secret_word)
word_l = list(secret_word)

letter_count = len(word_l)

word_display_l =[]

for num in range (letter_count):
    word_display_l.append("_")
word_display = " ".join(word_display_l)
print(word_display)
# print(word_l)
turns_left = 7
# letter_bank = "A B C D E F G H I J K L M\nN O P Q R S T U V W X Y Z"
# print(letter_bank)
letter_l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# print(letter_l)

used_letters = []

win = False
while turns_left > 0:
    if "".join(word_display_l) == secret_word.upper():
        print(f"\n\n\n   ***      YOU WON! THE WORD WAS {secret_word.upper()}      ***")
        win = True
        break
    while True:
        try:
            word_display = " ".join(word_display_l)
            print(f"\n\n                      {word_display}\n")
            print(" ".join(letter_l))
            player_guess = str(input("\n\nCHOOSE A LETTER:\n\n")).upper()
            cursor = -1
            match_count = 0
            for letter in word_l:
                cursor = int(cursor) + 1
                if player_guess.upper() == letter:
                    word_display_l.pop(cursor)
                    word_display_l.insert(cursor,player_guess)
                    match_count = match_count + 1
                    print("match")
                else:
                    print("No")
            if match_count < 1:
                turns_left = int(turns_left) - 1
                print(f"\n\n\n      NO {player_guess}s found!\n\n                            ▄██████████████▄▐█▄▄▄▄█▌
                ██████▌▄▌▄▐▐▌███▌▀▀██▀▀
                ████▄█▌▄▌▄▐▐▌▀███▄▄█▌
                ▄▄▄▄▄██████████████")
                print(f"       {hangman_art.stages[turns_left]}\n\n")
            else: print(f"\n\n             BRAVO!")    
            used_letters.append(player_guess)
            letter_l.remove(player_guess)
            # print(f"\n\n\nyou have {turns_left} guesses remaining!")
            break        
        except ValueError:
            print("\n\n\nInvalid Input. Try again")

if win == False:
    print(f"\n\n               SORRY! GAME OVER :(\n\nThe word was {secret_word}\n\n\n            {hangman_art.stages[0]}")
    print(hangman_art.lose[0])

