import sys

# Define the Vigenère square as a 2D array
vigenere_square = [[chr((i+j)%26 + ord('A')) for i in range(26)] for j in range(26)]

# Check that the correct number of arguments have been provided
if len(sys.argv) != 3:
    print('Usage: python encrypt.py keyword input_file')
    sys.exit()

# Get the keyword and plaintext from the command line arguments
keyword = sys.argv[1].upper()
input_file = sys.argv[2]

# Read the plaintext from the input file
with open(input_file, 'r') as file:
    plaintext = file.read()

# Function to encrypt a message with the Vigenère cipher
def encrypt(message, key):
    encrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():
            # Calculate the row and column indices in the Vigenère square
            row = ord(key[key_index % len(key)].upper()) - ord('A')
            column = ord(char.upper()) - ord('A')
            # Encrypt the character using the Vigenère square
            encrypted_char = vigenere_square[row][column]
            # Append the encrypted character to the encrypted message
            encrypted_message += encrypted_char
            key_index += 1
        else:
            # Append non-alphabetic characters as-is
            encrypted_message += char
    return encrypted_message

# Encrypt the plaintext with the Vigenère cipher and print the result
ciphertext = encrypt(plaintext, keyword)
print(ciphertext)

