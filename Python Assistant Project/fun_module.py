import random
def guess_number():
    messages = []
    number = random.randint(1, 20)
    attempts = 0
    messages.append("I have picked a number between 1 and 20. Try to guess it!")

    while attempts < 3:
        guess = input("Your guess: ")
        if not guess.isdigit():
            messages.append("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1
        if guess < number:
            messages.append("Too low! Try again.")
        elif guess > number:
            messages.append("Too high! Try again.")
        else:
            messages.append(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    else:
        messages.append(f"Sorry! The number was {number}.")

    return messages
def rock_paper_scissors():
    messages = []
    options = ["rock", "paper", "scissors"]
    messages.append("Let's play Rock Paper Scissors! Type your choice:")
    user_choice = input("Your choice: ").lower()
    if user_choice not in options:
        messages.append("Invalid choice. Please choose rock, paper, or scissors.")
        return messages

    comp_choice = random.choice(options)
    messages.append(f"I chose {comp_choice}.")

    if user_choice == comp_choice:
        messages.append("It's a tie!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "rock") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        messages.append("You win!")
    else:
        messages.append("I win!")
    return messages
def roll_dice():
    dice = random.randint(1, 6)
    return [f"You rolled a {dice}."]
def coin_toss():
    result = random.choice(["Heads", "Tails"])
    return [f"The coin shows {result}."]

