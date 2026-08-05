customers = int(input("Enter number of customers: "))
total500 = 0
total200 = 0
total100 = 0
for customer in range(1, customers + 1): #Outer loop
    print("Customer", customer)
    amount = int(input("Enter withdral amount: "))
    if amount <= 0 or amount % 100 != 0:
        print("Invalid amount Try next customer")
        continue
    for note in (500, 200, 100 ): #Inner loop
        count = amount //note
        if count > 0:
            print(note, "x", count)
            if note == 500:
                total500 += count
            elif note == 200:
                total200 += count
            else:
                total100 += count
            amount %= note
print("500 notes:", total500)
print("200 notes:", total200)
print("100 notes:", total100)