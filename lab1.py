
def helloWorld():
    print('Hello World')
    
helloWorld()


import datetime

def calculate_age():
    current_year = datetime.datetime.now().year
    birth_year = input("Enter your birth year: ")
    birth_year = int(birth_year)
    age = current_year - birth_year
    print("Your age is:", age)


# Call the function
calculate_age()

