import random, math
# O(n) time/ O(log2) space

def main():
    
    # Minimum number of guesses = log2(upper - lower + 1)
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))

    computer_num = random.randint(lower, upper)
    max_num_guesses = math.log(upper - lower + 1, 2) # second arg for log base
    print(f"\n\tYou've only {round(max_num_guesses)} chances to guess the number!\n")

    guess = 0
    while guess < max_num_guesses:

        guess_num = int(input('Guess a number: '))
        guess +=1
        
        if computer_num == guess_num:
            print(f"Congratulations you did it in {guess} try")
            break
        
        elif computer_num > guess_num:
            print("You guess too small!")
            
        elif computer_num < guess_num:
            print("You guess too high!")

    if guess >= max_num_guesses:
        print(f"\nThe number is {computer_num}")
        print("\tBetter Luck Next Time!")
    
if __name__ == "__main__":
    main()