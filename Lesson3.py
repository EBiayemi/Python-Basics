#Farm Harvest Calculator
f1 , f2 , f3 , f4 , f5 = 120, 150, 100, 180, 130
total_harvest = f1 + f2 + f3 + f4 + f5
print("Total harvest:", total_harvest)
average= total_harvest / 5
print ("Average harvest:", average)
bags = total_harvest // 25
print ("Total bags of harvest:", bags)
leftover = total_harvest % 25 
print ("Leftover harvest:", leftover)