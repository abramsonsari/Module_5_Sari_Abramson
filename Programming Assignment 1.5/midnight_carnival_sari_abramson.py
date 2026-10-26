
visitors = 0
admission = 0
ticket_money = 0
total_points = 0
while True:

    name = input("Name: (Enter done to end): ").strip().lower()
    if name == "done":
        print("Carnival is closing.")
        break
    age = input("Age: ")
    vip = input("Do you have VIP access (yes or no): ").lower().strip()
    charge = 0
    points = 0

    try:
        age = int(age)
    except ValueError:
        print("Not a valid input for age.")
        continue  # Loops back to the start if age isn't a number
    else:
        # If age is valid:
        if age < 8:
            print("Visitors younger than 8 must be accompanied by an adult.")
            print(f"Come again in {8-age} years!")
            print()
            print("Next guest.")
            print()
            continue
        else:
            visitors += 1
        if vip == "yes":
            print("Welcome to the carnival! You have free entry")
        elif age <= 17:
            print("Welcome to the carnival! Cost is $5")
            admission += 5
        else:
            print("Welcome to the carnival! Cost is $10")
            admission  += 10

        print("Tickets for the carnival games cost $2")

        # Loop to ask for ticket number and reprompt on bad input
    while True:
        tickets = input("How many tickets are you purchasing? (1-20): ")
        try:
            tickets = int(tickets)
            if tickets < 1 or tickets > 20:
                raise ValueError("Tickets amount must be between 1 and 20.")
        except ValueError as e:
            print("Invalid input for tickets.", e)
            continue
        else:
            print(f"{tickets} tickets purchased.")
            print(f"Ticket cost: ${tickets * 2}")
            print()
            ticket_money += tickets * 2
            break # ends ticket loop

        #lucky number
    while True:
        game = input("Do you want to play lucky number? Cost is 1 ticket. (yes/no): ").strip().lower()

        if game != "yes" and game != "no":
            print("Please answer yes or no.")
            continue #continues prompting to play game until valid input
        if game == "no":
            print("Ok, maybe later!")
            break
        elif tickets < 1:
            print("Not enough tickets to play. ")
            break

        else:
            print("playing")
            tickets -= 1
        guess = int(input("guess a whole number between 1-5: "))
        if guess == 3:
            print("You guessed the lucky number! You get 10 points!")
            print()
            total_points += 10
        elif 1<= guess <=5:
            print("Not the lucky number. You get 2 points!")
            total_points += 2
            print()
        else:
            print("Sorry, no prize points.")
        print()

    print("The mystery prize board: ")
    rows = 0
    while rows < 5:
        cols = 0
        while cols < 5:
            if (rows == cols ) or (rows == 0 and cols == 4) or (rows == 1 and cols == 3) or (rows == 3 and cols == 1) or (rows == 4 and cols == 0):
                print("*", end = " ")
            else:
                print("-", end = " ")
            cols +=1
        print()
        rows +=1
    print("The inner loop examines 25 positions. ")

    print()
    print("Next guest.")
    print()

print("End of night totals:")
print(f" Total visitor count is {visitors}")
print(f" Total admissions revenue is ${admission}")
print(f" Total ticket revenue is ${ticket_money}")
print(f" Total prize points awarded is {total_points}")


'''
I performed tests using different ages, different ticket amounts, improper input for all things we needed to check the input for, and tested yes/no results for each option. All worked as expected.
I tried a denied visitor, loop went on to next visitor not counting anything.
I tried a VIP visitor, visitor number was increased but no charge was added.
I tried an invalid ticket quantity and it reasked for quantity.
I tried a non-numeric ticket entry, a value error was displayed and the user was asked again.
I also tested that the program worked through multiple visitors and ended on "done".
'''
