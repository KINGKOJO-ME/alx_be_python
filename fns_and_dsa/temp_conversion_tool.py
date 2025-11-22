FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

Temperature_Conversions = input("Enter the temperature to convert: ")
if Temperature_Conversions == 0:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
Unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if Unit == 'C':
    converted_temp = convert_to_fahrenheit(float(Temperature_Conversions))
    print(f"{Temperature_Conversions}°C is {converted_temp:}°F")
elif Unit == 'F':
    converted_temp = convert_to_celsius(float(Temperature_Conversions))
    print(f"{Temperature_Conversions}°F is {converted_temp:}°C")
else:
    print("Invalid unit provided. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
Temperature_Conversions = float(Temperature_Conversions)
