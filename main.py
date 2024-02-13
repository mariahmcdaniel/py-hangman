import hangman_words

category = int(input("choose a category!\n\n1:Food & Beverage \n2:Animals"))

if int(category) == 1:
    word_pool = hangman_words.food_pool
