#Activity 1
number = int(input("Enter a number: ")) 
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else: 
    print("The number is zero")
#Activity 2
buying_price = 100
selling_price = 120
if selling_price > buying_price:
    profit = selling_price - buying_price
    print("Profit:", profit)
else:
    print("No profit, no loss")
#Activity 3
num = int(input("Enter a number: "))
if num > 15:
    print("The number is greater than 15")
else:
    print("The number is less than 15")
#Activity 4
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")