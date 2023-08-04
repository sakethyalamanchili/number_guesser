import random

def get_hint(random_number, user_guess):
    if user_guess > random_number:
        return "Hint: Your guess is above the number."
    else:
        return "Hint: Your guess is below the number."

def quirky_response():
    responses = ["Hmm... You're getting closer!", "Keep trying, you're doing great!", 
                 "Almost there, but not quite!", "You're one step away from the answer!", 
                 "I sense a master guesser in you!"]
    return random.choice(responses)

print("Welcome to the Number Guessing Game!")
top_of_range = input("Think of a number range, from 1 to: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please choose a number larger than 0.")
        quit()
else:
    print("Please enter a valid number.")
    quit()

random_number = random.randint(1, top_of_range)
chances = 5  # Set the number of chances

print("Let's play a guessing game! I've picked a number between 1 and", top_of_range, ". Can you guess it?")
print("You have", chances, "chances to make your guess. Good luck!")

for attempt in range(1, chances+1):
    user_guess = input("Attempt " + str(attempt) + ": Make a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a valid number next time.')
        continue

    if user_guess == random_number:
        print("Congratulations! You guessed the number", random_number, "correctly in", attempt, "attempts!")
        break
    else:
        if attempt == chances:
            print("Oops, that's not the number. You're out of chances.")
        else:
            print(quirky_response())
            print(get_hint(random_number, user_guess))

print("Thanks for playing! Better luck next time.")