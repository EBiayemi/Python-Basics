my_list = []
print(my_list)
numbers = [1, 2, 3, 4, 5]
print(numbers)
new_list = numbers * 2
print(new_list)
list2 = numbers[::-1]
print (list2)
#Activty 2
words = ["aba", "hello", "cat", "121"]
count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print(count)
#Activity 3
Num =[10, 20, 30, 40, 50]
total = sum(Num)
average = total / len(Num)
print("Sum:", total)
print("Average:", average)
print("Largest:", max(Num))
print("Smallest:", min(Num))