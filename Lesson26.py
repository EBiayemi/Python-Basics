from array import array
basket1 = {"apple", "banna", "orange", "grape"}
basket2 = {"banna", "orange", "watermelon", "grape"}
shared_fruits = basket1.intersection(basket2)
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Fruits in both baskets:", shared_fruits)
fruits = (["apple", "banna", "orange", "banna", "grape", "apple"])
print("Original fruit array:", fruits)
fruit_counts = {}
for fruit in fruits:
    if fruit in fruit_counts:
        fruit_counts[fruit] += 1
    else:
        fruit_counts[fruit] = 1
print("Fruit counts:", fruit_counts)
fruits.append("watermelon")
print("Updated fruit array:", fruits)
fruits.reverse()
print("Reversed fruit array:", fruits)