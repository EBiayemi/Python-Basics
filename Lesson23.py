tuplex = ("Eli", 15, 3.5, True)
print(tuplex)
tuple1 = (2, 4, 6, 8, 4)
print(tuple1)
tuple1 = tuple1 + (9,)
print(tuple1.count(4))
slice = tuple1[1:4]
print(slice)
#Activity 2
numbers = (1, 2, 3, 3, 2, 1)
i = 0
palindrome = True
while i < len(numbers) // 2:
    if numbers[i] != numbers[-i - 1]:
        palindrome = False
        break
    i += 1
if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
#Activity 3
weather = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0
for i in weather:
    if i == 1:
        rainy += 1
    else:
        sunny += 1
if rainy > sunny:
    print("Rainy")
else:
    print("Sunny")