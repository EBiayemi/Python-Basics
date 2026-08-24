def calculate_change(amount_paid, price):
    return amount_paid - price
price = 1.50
money_instered = 0
print("Welcome to the Snack Vending Machine")
print("The snack costs $1.50.")
while money_instered < price:
    coin = float(input("Insert a coin: $"))
    if coin == 0.25 or coin == 0.50 or coin == 1.00:
        money_instered += coin
        print("Accepted")
        print("Money inserted: $", round(money_instered, 2))
    else:
        print("Invalid coin. Please insert $0.25, $0.50, or $1.00.")
change = calculate_change(money_instered, price)
print("Enough money inserted")
print("Enjoy your snack")
if change > 0:
    print("Your change is $", round(change, 2))
else:
    print("No change is owed")
print("Thank You")