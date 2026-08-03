chores = ["Make Bed", "Wash Dishes", "Take Out Trash", "Sweep the Floor"]
completed = []
while len(chores) > 0:
    print("Chores left:", chores)
    chore = chores.pop(0)
    answer = input("Did you complete (yes/no:)")
    if answer.lower() == "yes":
        completed.append(chore)
print("Today's Chore Summary")
if len (completed) == 0:
    print("No chores were done today.")
else:
    for chore in completed:
        print(chore)
print("Total chores done:",)
len(completed)