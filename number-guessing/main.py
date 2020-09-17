import random

guesses = 0

selected_range = input("Range min-max: ").split()
selected_range.sort()

computer_num = random.randint(int(selected_range[0]), int(selected_range[1]))

print(computer_num)
while True:
    
    guess_num = int(input('What is your number: '))

    if guess_num != computer_num and guess_num > computer_num:
        guesses += 1
        print("Try Again! You guessed too high")
    elif guess_num != computer_num and guess_num < computer_num:
        guesses += 1
        print("Try Again! You guessed too small")
    else:
        guesses += 1
        print(f"You win with {guesses} guesses")
        break
