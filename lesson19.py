try:
    num = int(input("Emter a mumber: "))
    print("You entered:", num)
except ValueError:
    print("That's not a valid number:")
#Activity 2
try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter another number: "))
    print(num1 / num2)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("You cannot divide by zero")
finally:
    print("Program finshed")
#Activity 3
value = False
while not value:
    try:
        number = int(input("Enter a number: "))
        while number % 2 == 0:
            print("Bye")
        value = True
    except ValueError:
        print("Invalid")