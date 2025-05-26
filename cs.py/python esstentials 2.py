# creating tuples
fruits = ('apple', 'banana', 'cherry', 'date')  
numbers = (1, 2, 3, 4, 5)  
empty = ()  

#accessing tubule elements
print(f"{fruits[0]}")  
print(f"{fruits[-1]}")  
print(f"{numbers[1]}")  
print(f"{numbers[3]}") 

#tuple Operations
concatenated_tuple = fruits + numbers  
print(f"{concatenated_tuple}")

repeated_numbers = numbers * 3 
print(f"{repeated_numbers}")

#tuple Methods
colors = ('red', 'blue', 'green', 'blue', 'yellow') 

blue_count = colors.count('blue')  
print(f"{blue_count}")

green_index = colors.index('green')  
print(f"{green_index}")

# immutability (error)
try:
    fruits[0] = 'avocado' 
except TypeError as e:
    print(f"Error: {e}")

# use Cases for Tuples
def get_student_info():
    """Returns a tuple containing a student's name, age, and grade."""
    return ("Joe", 20, "C")

student_info = get_student_info()  
print(f"Student Info: {student_info}")  

# advanced Tuple Operations
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'))  

print(f"{nested_tuple[0][1]}")  
print(f"{nested_tuple[1][2]}")  
