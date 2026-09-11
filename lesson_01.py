# import math 

#Intro to binary and decimal conversions
decimal = 11
print("decimal: ", decimal)

binary = 1011
print("binary: ", binary)

# Binary to decimal converter
binary = "1011"

decimal = (
    int(binary[0]) * 8 +
    int(binary[1]) * 4 +
    int(binary[2]) * 2 +
    int(binary[3]) * 1
)

print("Binary: ", binary, ", Decimal: ", decimal)


# Binary to decimal converter for any length binary number
def binary_to_decimal(binary):
    b_length = len(binary) - 1

    decimal = 0

    for b in binary:

        power = 2 ** b_length
        decimal += int(b) * power
        b_length -= 1

    return decimal

print(binary_to_decimal("1101"))
print(binary_to_decimal("101"))
print(binary_to_decimal("0"))

# Decimal to binary converter
def decimal_to_binary(decimal):
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


print(decimal_to_binary(25))
print(decimal_to_binary(-20))
print(decimal_to_binary(0))