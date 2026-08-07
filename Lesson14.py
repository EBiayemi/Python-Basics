#Activity 1
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#Activity 2
rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#Activity 3
rows = 3
#Top half
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end= " ")
    for j in range(1, 2 * i):
        print(j, end= " ")
    print(" ")
#Bottom half 
for i in range(rows -1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for j in range(1, 2 * i):
        print(j, end=" ")
    print("")