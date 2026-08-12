def greet_custmer(name):
    return "Welcome to the lemonade stand,"
def calculate_total(price, cups):
    return price * cups
def calculate_change(payment, total):
    return payment - total
def thank_you_message(name):
    return "Thank you for visting the lemonade stand"
print(greet_custmer)
price = float(input("What is the price per cup"))
cups = int(input("How many cups would you like "))
total = calculate_total(price,cups)
total = round(total, 2)
print("Your total is: $", total)
payment = float(input("How much money are you paying"))
change = calculate_change(payment,total)
change = round(change, 2)
message = thank_you_message
print("LEMONADE STAND RECPIT")
print("Customer")
print("Price per cup $", price)
print("Number of cups:", cups)
print("Total cost: $", total)
print("Payment: $", payment)
print("Change due: $", change)