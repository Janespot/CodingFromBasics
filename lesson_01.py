import math 

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
binary = "11011000"

b_length = len(binary) - 1

print(b_length)

decimal = 0

for b in binary:

    power = 2 ** b_length
    decimal += int(b) * power
    b_length -= 1

print("Binary: ", binary, ", Decimal: ", decimal)

# Decimal to binary converter
decimal = 25
original_decimal = decimal

binary = "" 

while decimal > 0:
    remainder = decimal % 2

    binary += str(remainder)
    # print("decimal: ", decimal, ", remainder: ", remainder, ", binary: ", binary)

    decimal  = math.floor(decimal / 2)

binary = binary[::-1]

print("Decimal: ", original_decimal, ", Binary: ", binary)