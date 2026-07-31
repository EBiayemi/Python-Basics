n = int(input("Entera number: "))
sum = 0
for i in range (1, n + 1):
    sum = sum + i
print("Sum =", sum)
#Activity 2
text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
print(reverse)
#Activity 3
s = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)