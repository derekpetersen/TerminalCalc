import os

# Uses OS module to clear terminal
def clear_console():
  os.system('cls')

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

# Divide
def div(n1, n2):
    return n1 / n2


# Determine the operator and perform operation
def operations(num1, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return sub(num1, num2)
    elif operator == "*":
        return mul(num1, num2)
    elif operator == "/":
        return div(num1, num2)
    else:
        return "Enter a valid operator, please"

# ~~~Global variables~~~
# Starting state of the calculator


# Main calculator function
def calculator():
#Needs to be able to access the 'operator' function within this function
    global operator
    active = True
    cal_num = 1
    calculations = {}
    while active == True:
        if cal_num <= 1:
            first_number = int(input("Enter the first number: "))
        operator = input("Select the operator(+, -, *, /): ")
        second_number = int(input("Enter the second number: "))
        sum = operations(first_number,second_number)
        calculations[cal_num] = sum
        print(calculations[cal_num])
        cal_num += 1
        another = input("Do you want to continue this calculation? y or n: ")
        if another == "n":
            calculations = {}
            cal_num = 1
            clear_console()
            end = input("Do you want to end this session and exit? y or n: ")
            if end == "y":
                clear_console()
                active = False
            else:
                clear_console()
        else:
            first_number = sum
            print(f"Running total: {first_number}")

calculator()
