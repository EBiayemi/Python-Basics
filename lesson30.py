#Activity 1
class IOString:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a string: ")
    def print_string(self):
        print(self.str1.upper())
my_string = IOString()
my_string.get_string()
my_string.print_string()
#Activity 2
class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Employee deleted")
def employee_function():
    emp = Employee()
    del emp
employee_function()
#Activity 3
class PairElements:
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num + num2 == target:
                    return i, j
value = int(input("Enter sum: "))
numbers = (10, 20, 30, 40, 50, 60, 70)
pair = PairElements()
print(pair.twoSum(numbers, value))