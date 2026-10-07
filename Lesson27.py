items = ["Notebook", "Pencil", "Backpack", "Earser", "Calculator"]
stock = [10, 0, 5, 15, 0]
inventory = dict(zip(items, stock))
print("Inventory:", inventory)
in_stock_items = [item for item in items if inventory[item] > 0]
print("Items In Stock:", in_stock_items)
chosen_item = input("Which item do you want to buy")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock Stopping it")
    exit()
prices = [10, 5, 40, 15, 20]
markup = int(input("Enter the markup amount to add every price: "))
marked_up_prices = list(map(lambda p: p + markup))
print("Marked up prices:", marked_up_prices)
item_index = items.index(chosen_item)
print("price of", chosen_item, ":", marked_up_prices[item_index])