def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        # convert to float for division
        numerator = float(numerator)
        denominator = float(denominator)

            #try to perform division
        result = numerator / denominator
        print(f"The result of the division is {result}")

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
        