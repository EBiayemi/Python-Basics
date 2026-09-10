import random
playing = True
number = str(random.randint(0,9))
print("I will generate a number from 0 to 9, and guess the number.")
print("The game ends when you get it right")
while playing:
    guess = input("Give me a guess")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess is not right")
#Activity 2
import math 
print("The floor and ceiling value of 23.56 are: " + str(math.ceil(23.56)) + ", " + str(math.floor(23.56)))
x = 10
y = -15
print("The value of x after copying the sign from y is: " + str(math.copysign(x, y)))
print("Absolute value of -96 and 96 are: " + str(math.fabs(-96)) + "," + str(math.fabs(96)))
print("The GCD of 24 and 56 is: " + str(math.gcd(24, 56)))
#Activity 3
import random
chocies = ["rock", "paper", "sicssors"]
while True:
    user_choice = input("Choose rock, paper, or sicssors,")
    computer_choice = random.choice(chocies)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        print("It is a tie")
    elif user_choice == "rock" and computer_choice == "sicissors":
        print("You win")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif user_choice == "sicssors" and computer_choice == "paper":
        print("You win")
    else:
        print("Computer wins")
    again = input("Do you want to play again? yes/no:")
    if again == "no":
        print("Game over")
        break