

# problem 1: age classification
age = int(input("Enter your age: ")) 

if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# problem 2: number classification
number = float(input("\nEnter a number: "))  

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# problem 3: exam grade 
score = int(input("\nEnter your exam score (0-100): "))  

if 90 <= score <= 100:
    print("Your grade is: A")
elif 80 <= score < 90:
    print("Your grade is: B")
elif 70 <= score < 80:
    print("Your grade is: C")
elif 60 <= score < 70:
    print("Your grade is: D")
else:
    print("Your grade is: F")

# problem 4: temperature check
temperature = float(input("\nEnter the current temperature in Celsius: "))  

if temperature < 10:
    print("It is cold.")
elif 10 <= temperature < 25:
    print("It is warm.")
else:
    print("It is hot.")
