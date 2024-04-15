
# binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# binary to octal
def binary_to_octal(binary):
    return oct(int(binary, 2))[2:]

# binary to hexadecimal
def binary_to_hexadecimal(binary):
    return hex(int(binary, 2))[2:].upper()

# decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# decimal to octal
def decimal_to_octal(decimal):
    return oct(decimal)[2:]

# decimal to hexadecimal
def decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:].upper()

# octal to binary
def octal_to_binary(octal):
    return bin(int(octal, 8))[2:]

# octal to decimal
def octal_to_decimal(octal):
    return int(octal, 8)

# octal to hexadecimal
def octal_to_hexadecimal(octal):
    return hex(int(octal, 8))[2:].upper()

# hexadecimal to binary
def hexadecimal_to_binary(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

# hexadecimal to decimal
def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

# hexadecimal to octal
def hexadecimal_to_octal(hexadecimal):
    return oct(int(hexadecimal, 16))[2:]

def convert_number():
    number = input("Enter a number: ")
    from_base = input("Enter the base of the input number (binary, octal, decimal, hexadecimal): ").lower()
    to_base = input("Enter the base to convert to (binary, octal, decimal, hexadecimal): ").lower()
    if from_base == 'binary':
        converted_number = binary_to_decimal(number) if to_base == 'decimal' else \
                           binary_to_octal(number) if to_base == 'octal' else \
                           binary_to_hexadecimal(number) if to_base == 'hexadecimal' else \
                           "Invalid conversion"
    elif from_base == 'octal':
        converted_number = octal_to_binary(number) if to_base == 'binary' else \
                           octal_to_decimal(number) if to_base == 'decimal' else \
                           octal_to_hexadecimal(number) if to_base == 'hexadecimal' else \
                           "Invalid conversion"
    elif from_base == 'decimal':
        converted_number = decimal_to_binary(int(number)) if to_base == 'binary' else \
                           decimal_to_octal(int(number)) if to_base == 'octal' else \
                           decimal_to_hexadecimal(int(number)) if to_base == 'hexadecimal' else \
                           "Invalid conversion"
    elif from_base == 'hexadecimal':
        converted_number = hexadecimal_to_binary(number) if to_base == 'binary' else \
                           hexadecimal_to_octal(number) if to_base == 'octal' else \
                           hexadecimal_to_decimal(number) if to_base == 'decimal' else \
                           "Invalid conversion"
    else:
        converted_number = "Invalid base for input number"
    print(f"{number} ({from_base}) converted to {converted_number} ({to_base})")
convert_number()

