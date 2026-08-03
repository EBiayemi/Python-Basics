chores= ["Make Bed", "Wash Dishes", "Take Out Trash", "Sweep the floor"]
while len(chores) > 0:
    print("Chores left:"len(chores)()
    chores = chores.remove(chores ["wash dishes"])
    answer = input("Did you complete Y(yes or no):")
    if answer.lower() == "yes":
        completed=chores
print("Today's Chhore Summary")
if len(completed) == 0:
    print("No chores were done today")
else:
    for chore in completed:
        print("-",chore)
print("total chores done", len(completed))
