import random
secret = random.randint(1,50)
attempts = 0
won = False
while attempts < 5 and not won:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts = attempts + 1
    if guess == secret:
        print("🎉 You got it")
        won = True
    else:
        difference = abs(secret - guess)
        if difference >= 20:
            print("🧊 Ice cold")
        elif difference >= 10:
            print("🥶 Cold")
        elif difference >= 5:
            print("🌡️ Warm")
        else:
            print("🔥 Hot")
        print ("Remaing lives: ", end="")
        for i in range(5 - attempts):
            print("❤️", end="")
        print()
if not won:
    print("You ran out of attempts")
    print("The sercet number was", secret)