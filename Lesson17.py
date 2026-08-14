def total_calc(bill_amount, tip_perc):
    tip = bill_amount * (tip_perc / 100)
    total = bill_amount + tip
    total = round(total, 2)
    print("Final total: $", total)
total_calc (150, 20)
#Activity 2
def cube(number):
    return number * number * number
def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
print(by_three(9))
print(by_three(4))
#Activty 3
def f(x):
    """Calculates the f of a number using recursion."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * f(x - 1)
print(f.__doc__)
print(f(0))
print(f(1))
print(f(2))
print(f(5))
print(f(10))