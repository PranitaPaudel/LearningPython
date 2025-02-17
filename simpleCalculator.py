def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1, num2):
    if(num2 == 0):
        print("Error! division by 0 not possible")
    else:
        return num1 / num2

while(True):
    print("Select operation from the menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")

    operator = int(input("Enter your choice:"))

    if operator in [1, 2, 3, 4]:
        num1 = float(input("Enter 1st number:"))
        num2 = float(input("Enter 2nd number:"))

        if operator == 1:
            result = add(num1, num2)
        elif operator == 2:
            result = subtract(num1, num2)
        elif operator == 3:
            result = multiply(num1, num2)
        elif operator == 4:
                result = divide(num1, num2)
        print(f"The answer is {result}")
    else:
        print("Invalid choice! Select a number from the menu")
        continue
    
    selection = input("Do you want to perform another calculation? (y/n):")
    if selection.lower() != 'y':
        print("Bye Bye!")
        break