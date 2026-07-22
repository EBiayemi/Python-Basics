a = 8
b = 4
c = 2
d = 5
result = (a + b) * c - d
print("The value of (a + b) * c - d is:", result)
#Ac 2
number = int(input("Enter a number: "))
divisor = int(input("Enter a divisor :"))
if number % divisor == 0:
    print(number, "is divisible by", divisor)
else:
    print(number, "is not divisible by", divisor)
#AC 3
mean = 38
numbers = 40
worng_sum = mean * numbers
correct_sum = worng_sum - 36 + 56
correct_mean = correct_sum / numbers 
print("correct mean is:", correct_mean)
#Ac 4
speed1 = 10 
speed2 = 20
speed3 = 30
average = (speed1 + speed2 + speed3) / 3
print("Average speed is:", average, "km/h")
if speed1 < average:
    print("Cyclist 1 is slower than the average.")
elif speed2 < average:
    print("Cyclist 2 is slower than the average.")
elif speed3 < average:
    print("Cyclist 3 is slower than the average.")
