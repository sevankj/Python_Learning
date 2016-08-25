import random

# generate a random number between 1 and 10

secret_num = random.randint(1, 4)
guesses = []

while len(guesses) < 5:
    try:
        user_input = int(raw_input("Enter a number to Guess: "))
    except ValueError:
        print("Thats not a numnber !")
    else:
        if user_input == secret_num:
            print "HIT"
            break
        else:
            print "MISS"
        guesses.append(user_input)
