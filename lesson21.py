def add(a,b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
try:
    opreation = input("Choose a opreation(t, -, *, /): ")
    numm1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if opreation == "+":
        result = add(numm1, num2)
    elif opreation == "-":
        result = subtract(numm1, num2)
    elif opreation == "*":
        result = multiply(numm1, num2)
    elif opreation == "/":
        result = divide(numm1, num2)
    else:
        print("Invalid opreation")
        result = None
    if result is not None:
        print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter numbers only")