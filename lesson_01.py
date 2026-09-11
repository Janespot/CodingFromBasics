# Binary to decimal converter for any length binary number
def binary_to_decimal(binary):
    if binary == "":
        raise ValueError("Please enter a binary value")
    
    for b in binary:
        if b != "0" and b != "1":
            raise ValueError("Error! Please enter a valid binary")
        
    b_length = len(binary) - 1

    decimal = 0

    for b in binary:
        power = 2 ** b_length
        decimal += int(b) * power
        b_length -= 1

    return decimal

# Decimal to binary converter
def decimal_to_binary(decimal):
    try:
        decimal = int(decimal)
    except ValueError:
        raise ValueError("Please enter a valid integer")

    original_decimal = decimal

    binary = "" 

    if decimal == 0:
        binary = "0"

    if decimal < 0:
        decimal = abs(decimal)

    while decimal != 0:

        remainder = decimal % 2

        binary += str(remainder)

        decimal  = decimal // 2

    binary = binary[::-1]

    if original_decimal < 0:
        binary = "-" + binary

    return binary

selection = input("Please select: Do you want to convert " \
"\n 1. Binary to Decimal " \
"\n 2. Decimal to Binary " \
"\nEnter 1 or 2 then press 'Enter' to continue: ")

while selection != "1" and selection != "2":
    selection = input("Invalid choice. Please enter 1 or 2: ")

value_to_convert = input("Please enter a value to convert: ")

if selection == "1":
    try:
        print(binary_to_decimal(value_to_convert))
    except ValueError as e:
        print(e)

elif selection == "2":
    try:
        print(decimal_to_binary(value_to_convert))
    except ValueError as e:
        print(e)
