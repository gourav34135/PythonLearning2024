#python program to convert decimal to binary or from binary to decimal


def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b", "")
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def main():
    choice = input("Enter 'D' to convert Decimal to Binary or 'B' to convert Binary to Decimal: ").upper()

    if choice == 'D':
        decimal = int(input("Enter a decimal number: "))
        binary = decimal_to_binary(decimal)
        print("Binary equivalent:", binary)
    elif choice == 'B':
        binary = input("Enter a binary number: ")
        decimal = binary_to_decimal(binary)
        print("Decimal equivalent:", decimal)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
