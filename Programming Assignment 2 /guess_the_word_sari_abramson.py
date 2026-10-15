#Word lists, game counts:
animals = ['dog', 'cat', 'wolf', 'bird', 'lion', 'zebra','horse', 'tiger','flamingo','monkey']
supplies = ['pencil', 'pen', 'paper', 'scissors', 'glue','binder','tape','crayons','eraser','folder']
colors = ['red','orange','blue','pink','teal','silver','gold','peach','gray','violet']
fruits = ['plum','grapes', 'melon','orange', 'mango','lemon','pear','peach', 'kiwi','lime' ]
wins = 0
losses = 0

while True:

#getting word category
    while True:
        category = input("Pick a category for your word (animals, school supplies, colors, or fruits): ").strip().lower()
        if not(category == "animals" or category =="school supplies" or category == "colors" or category =="fruits"):
            print(f" {category} is not one of the category options. Check spelling and try again.")
            continue
        else:
            break
    #Matching input to the correct list
    if category =="animals":
        category = animals
    elif category =="school supplies":
        category = supplies
    elif category =="colors":
        category = colors
    else:
        category = fruits

    #getting difficulty level
    while True:
        difficulty = input("Choose a difficulty level, 6/8/10 tries (enter 6, 8, or 10): ").strip()
        try:
            difficulty = int(difficulty)
            if not(difficulty == 6 or difficulty == 8 or difficulty == 10):
                raise ValueError("Not a difficulty option. ")
        except ValueError as e:
            print("Invalid input, try again." , e)
            continue
        else:
            break

    import random
    word_chosen = random.choice(category)
    wrong_guesses = 0
    letters = []
    guessed=list(len(word_chosen)* '-')

    print(f"Try to guess the word! you have {difficulty} mistakes allowed. ")

    print("".join(guessed))


    while wrong_guesses < difficulty:
        print()
        guess = input("Guess a letter: ").strip().lower()
        if len(guess)!=1:
            print("Invalid input, guess one letter at a time.")
            continue
        elif not(guess.isalpha()):
            print("Only letters, try again.")
            continue


        if (guess in letters) == True:
            print("already guessed that letter. ")
            print("".join(guessed))
            continue
        elif (guess in word_chosen) == True:
            letter_index = word_chosen.index(guess)
            guessed[letter_index]=(guess)
            print("".join(guessed))
            letters.append(guess)

        else:
            print("nope, not in this word. ")
            letters.append(guess)
            wrong_guesses +=1
            print(f"You have {difficulty - wrong_guesses} guesses left")
            letters.sort()
            print(f"Guessed letters: {letters}")
            print("".join(guessed))


        if wrong_guesses == difficulty:
            print(f"Sorry, you didn't guess the correct word within {difficulty} tries.")
            print(f"The word was {word_chosen}.")
            losses +=1


        if "".join(guessed) == word_chosen:
            print(f"You got it! The word was {word_chosen}!")
            print(f"You guessed with {difficulty -wrong_guesses} guesses to go!")
            wins += 1
            break
    print(f"Total scores:")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    while True:
        play = input("Do you want to play again? (y/n): ").strip().lower()
        if not(play == "y" or play =="n"):
            print("Not a valid answer. Enter y/n: ")
            continue
        else:
            break
    if play == "y":
        print("Playing again!")
        continue
    elif play == "n":
        print("Thanks for playing!")
        break
