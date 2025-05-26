
import time

# countdown

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)  
        seconds -= 1
    print("Time's up!")

# Problem 2: Asking for the Number 7

def ask_for_seven():
    while True:
        try:
            num = int(input("Enter the number 7: "))
            if num == 7:
                print("Correct!")
                break
            else:
                print("Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Problem 3: Shopping List

def shopping_list():
    items = "milk, eggs, bread, butter"
    for item in items.split(", "):
        print(item)

# Problem 4: Calculating Average Grade

def calculate_average_grade():
    grades = input("Enter all your grades separated by spaces: ").split()
    total = 0
    count = 0
    for grade in grades:
        try:
            total += float(grade)
            count += 1
        except ValueError:
            print(f"Invalid input ignored: {grade}")
    if count > 0:
        average = total / count
        print(f"Your average grade is: {average:.2f}")
   


def main():
    countdown_timer(5)  
    ask_for_seven()
    shopping_list()
    calculate_average_grade()

if __name__ == "__main__":
    main()