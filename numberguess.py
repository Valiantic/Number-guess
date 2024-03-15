import random

# level 1
def numberguess1():
    ranum = random.randint(1, 10)
    num_guesses = 0
    
    while True:
        try:
            level1 = int(input("Guess a number between 1 and 10: "))
            num_guesses += 1

            if level1 < ranum:
                print("Too low! Try again.")
            elif level1 > ranum:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {num_guesses} attempts.")
                if num_guesses == 1:
                    print("Your a mind reader!")
                elif num_guesses >= 2 and num_guesses <= 4:
                    print("Most impressive.")
                elif num_guesses >= 3 and num_guesses <= 6:
                    print("You can do better than that.")
                elif num_guesses >= 7:
                    print("Better luck next time.")
                break  

        except:
            print("Invalid input. Please enter a number between 1 and 10.")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == 'y':
        numberguess1()  
    else:
        print("Thanks for playing!")

# level 2
def numberguess2():
    ranum2 = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        try:
            level2 = int(input("Guess a number between 1 and 100: "))
            num_guesses += 1

            if level2 < ranum2:
                print("Too low! Try again.")
            elif level2 > ranum2:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {num_guesses} attempts.")
                if num_guesses == 1:
                    print("Your a mind reader!")
                elif num_guesses >= 2 and num_guesses <= 4:
                    print("Most impressive.")
                elif num_guesses >= 3 and num_guesses <= 6:
                    print("You can do better than that.")
                elif num_guesses >= 7:
                    print("Better luck next time.")
                break  

        except:
            print("Invalid input. Please enter a number between 1 and 100.")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == 'y':
                numberguess2()  
    else:
                print("Thanks for playing!")
        
#level 3
def numberguess3():     
    ranum3 = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        try:
            level2 = int(input("Guess a number between 1 and 1000: "))
            num_guesses += 1

            if level2 < ranum3:
                print("Too low! Try again.")
            elif level2 > ranum3:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {num_guesses} attempts.")
                if num_guesses == 1:
                    print("Your a mind reader!")
                elif num_guesses >= 2 and num_guesses <= 4:
                    print("Most impressive.")
                elif num_guesses >= 3 and num_guesses <= 6:
                    print("You can do better than that.")
                elif num_guesses >= 7:
                    print("Better luck next time.")
                break  

        except:
            print("Invalid input. Please enter a number between 1 and 1000.")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == 'y':
                numberguess3()  
    else:
                print("Thanks for playing!")


# start of the game
print("Number Guessing!")
difficulty = int(input("Pick a difficulty level 1, 2, or 3: "))


if difficulty == 1:
    numberguess1()
elif difficulty == 2:
    numberguess2()
elif difficulty == 3: 
    numberguess3()
else:
    print("Invalid input")