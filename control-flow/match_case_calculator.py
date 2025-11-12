num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print(f"The result is {num1 + num2}.")
    case "-":
        print(f"The result is {num1 - num2}.")
    case "*":
        print(f"The result is {num1 * num2}.")
    case "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The result is {num1 / num2}.")
    case _:
        print("Error: Invalid operation selected. Please choose from +, -, *, /.")