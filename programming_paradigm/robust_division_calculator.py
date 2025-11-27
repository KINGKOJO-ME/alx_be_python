def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        # convert to float for division
        numerator = float(numerator)
        denominator = float(denominator)

            #try to perform division
        result = numerator / denominator
        print(f"The result of the division is: {result}")

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid input. Please enter numbers."
    
        