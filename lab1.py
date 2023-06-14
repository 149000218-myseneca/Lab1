
def helloWorld():
    print('Hello World')
    
helloWorld()


import datetime

def calculate_age():
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = 2023  # You can update this with the current year
        age = current_year - birth_year
        print("Your age is:", age)
    except ValueError:
        print("Please enter a valid integer for the birth year.")


if __name__ == "__main__":
    calculate_age()