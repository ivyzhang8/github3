# f-Strings
name = "Ivy" 
age = 16 
print(f"Hello, {name}. You are {age} years old.") 

product = "banana"
price = 2.99
print(f"The price of the {product} is ${price}.")

day = 3
month = 5
year = 2025
print(f"The date is {day:02}/{month:02}/{year}.")

floating_number = 3.556
print(f"Formatted number: {floating_number:.2f}")

# task 2
str_to_int = int("123")
print(str_to_int)

str_to_float = float("45.67")
print(str_to_float)

int_to_str = str(89)
print(int_to_str)

str_to_bool = bool("True")
print(str_to_bool)

# User Inputs
name_input = input("Enter your name: ")
print(f"Hello, {name_input}!")

age_input = input("Enter your age: ")
print(f"You are {age_input} years old.")

user_number = int(input("Enter a number: "))
print(f"Double the number: {user_number * 2}")

# Combining Casting and User Inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"The sum is: {num1 + num2}")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

bool_value = bool(input("Enter True or False: ")=="True")
print(f"Opposite value: {not bool_value}")

