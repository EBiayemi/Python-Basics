a = 5
b = 5
c = 5.0
print (a is b) #True
print (a is c)
print (a is not c) #False
#2
a = 5
print (a << 1) # Left shift 
print (a >> 1) # Right shift
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))
sub3 = int(input("Enter marks for subject 3: "))
sub4 = int(input("Enter marks for subject 4: "))
sub5 = int(input("Enter marks for subject 5: "))
average = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
print("Average marks:", average)
if average >= 91 and average <= 100:
    print("Grade: A")
elif average >= 81 and average <= 90:
    print("Grade: B")
elif average >= 71 and average <= 80:
    print("Grade: C")
