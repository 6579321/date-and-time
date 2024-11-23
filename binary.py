# Function to convert decimal to binary using bin()
def decimal_to_binary(decimal):
    return bin(decimal)[2:]  # Remove the '0b' prefix

# Example usage
decimal_number = 10
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")
