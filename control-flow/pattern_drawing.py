# prompt user to enter a positive integer
size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    # Use the for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing all asterisks in the current row
    row += 1