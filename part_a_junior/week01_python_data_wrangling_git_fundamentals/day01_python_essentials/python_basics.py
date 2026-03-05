# ==========================================
# DAY 1 - PYTHON BASICS FOR ML ENGINEER
# ==========================================

# ------------------------------------------
# 1. Variables & Data Types
# ------------------------------------------

print("----- Variables & Data Types -----")

name = "Mudakir"
age = 24
height = 5.8
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# ------------------------------------------
# 2. Strings
# ------------------------------------------

print("\n----- Strings -----")

name = "Mudakir"

print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])

age = 24
print(f"My name is {name} and I am {age} years old")


# ------------------------------------------
# 3. Lists
# ------------------------------------------

print("\n----- Lists -----")

numbers = [10, 20, 30, 40]

print(numbers[0])
print(numbers[-1])

numbers.append(50)
numbers.remove(20)
numbers.pop()

print("Updated List:", numbers)
print("Length:", len(numbers))

print("Looping through list:")
for num in numbers:
    print(num)


# ------------------------------------------
# 4. Dictionaries
# ------------------------------------------

print("\n----- Dictionaries -----")

student = {
    "name": "Mudakir",
    "age": 24,
    "skills": ["Python", "ML"]
}

print(student["name"])
print(student["skills"])

student["city"] = "Peshawar"

print("Loop dictionary:")
for key, value in student.items():
    print(key, value)


# ------------------------------------------
# 5. Conditions
# ------------------------------------------

print("\n----- Conditions -----")

age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")


# ------------------------------------------
# 6. Loops
# ------------------------------------------

print("\n----- For Loop -----")

for i in range(5):
    print(i)

print("\n----- While Loop -----")

count = 0
while count < 5:
    print(count)
    count += 1


# ------------------------------------------
# 7. Functions
# ------------------------------------------

print("\n----- Functions -----")

def greet():
    print("Hello Mudakir")

greet()

def greet_user(name):
    print(f"Hello {name}")

greet_user("Mudakir")

def add(a, b):
    return a + b

result = add(5, 3)
print("Addition:", result)

def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

def calculate(a, b):
    sum_value = a + b
    multiply_value = a * b
    return sum_value, multiply_value

s, m = calculate(3, 4)
print("Sum:", s, "Multiply:", m)

square = lambda x: x * x
print("Square:", square(5))


# ------------------------------------------
# 8. List Comprehension
# ------------------------------------------

print("\n----- List Comprehension -----")

numbers = [1, 2, 3, 4]

squared = [n * n for n in numbers]
print("Squared:", squared)

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)


# ------------------------------------------
# 9. Exception Handling
# ------------------------------------------

print("\n----- Exception Handling -----")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input")


# ------------------------------------------
# 10. OOP Basics
# ------------------------------------------

print("\n----- OOP Basics -----")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

s1 = Student("Mudakir", 24)
print(s1.name)
s1.greet()


class Model:
    def __init__(self, name):
        self.name = name

    def train(self, data):
        print(f"Training {self.name} model")

    def predict(self, input_data):
        print("Making prediction")
        return 0.95

model = Model("Logistic Regression")
model.train("dataset.csv")
prediction = model.predict([1, 2, 3])
print("Prediction:", prediction)


# ------------------------------------------
# 11. Practice Tasks
# ------------------------------------------

print("\n----- Practice Tasks -----")

# Task 1: Function to calculate average

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print("Average:", calculate_average([10, 20, 30, 40]))


# Task 2: Car Class

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def drive(self):
        print(f"{self.brand} car is driving")

car1 = Car("Toyota", 2022)
car1.drive()


# Task 3: List comprehension (squares 1–20 only even numbers)

squares_even = [x * x for x in range(1, 21) if x % 2 == 0]
print("Squares of Even Numbers 1-20:", squares_even)


# Task 4: Even or Odd Checker

try:
    number = int(input("Enter number to check even/odd: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input")


print("\n===== END OF DAY 1 =====")