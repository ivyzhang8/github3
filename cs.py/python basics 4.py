# Relational Operators
print(15 > 10) 
print(7 == 7)  
print( 5 != 3) 
print(8 <= 8)  
print(12 < 20)  
print(25 >= 25) 

# Logical Operators
print("True and False:", True and False) 
print("True or False:", True or False)  
print(not True)
print((5 > 3) and (8 < 10))
print((5 > 10) or (8 < 10))
print("not (7 == 7):", not (7 == 7)) 

# relational and operational logical operators
n = 15
print(10 <= n <= 20) 

age = 20
citizen = True  # Added citizen status check
print("Is person eligible to vote?", (age >= 18) and citizen)

x = 3
print((x < 5) or (x > 15)) 

temperature = 22
print("Is (20-25) celcius a comfortable range?", 20 <= temperature <= 25) 

score = 55
attendance = 80
print("Has the student passed?", (score >= 50) and (attendance > 75))  
