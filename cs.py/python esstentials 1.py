#basic function
def greet():
    print("Hello! Welcome")

# Calling the function
greet()

# Function with Parameters
def multiply(a, b):
    return a * b

print(multiply(1, 2)) 
print(multiply(1, 3))

# Function with Return Value
def square(num):
    return num ** 2

# calling and printing the function
print(square(6)) 

# Default Parameters

def introduce(name, age=30):
    print(f"My name is {name} and I am {age} years old.")

introduce("Bob")     

# Keyword Arguments
def order(item, quantity, price):
    total_cost = quantity * price
    print(f"You ordered {quantity} {item}(s). Total cost: ${total_cost:.2f}")

# Calling the function using keyword arguments
order(item="banana", quantity=2, price=3)
order(quantity=1, item="apples", price=2)

# Documenting Functions
def calculate_area(radius):
    return 3.14159 * radius ** 2

#calling and printing the function
print(calculate_area(3))  
