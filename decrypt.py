import sys

# Define the Vigenère square as a 2D array
vigenere_square = [[chr((i+j)%26 + ord('A')) for i in range(26)] for j in range(26)]

# Check that the correct number of arguments have been provided
if len(sys.argv) != 3:
    print('Usage: python decrypt.py keyword input_file')
    sys.exit()

# Get the keyword and ciphertext from the command line arguments
keyword = sys.argv[1].upper()
input_file = sys.argv[2]

# Read the ciphertext from the input file
with open(input_file, 'r') as file:
    ciphertext = file.read()

# Function to decrypt a message with the Vigenère cipher
def decrypt(message, key):
    decrypted_message = ''
    key_index = 0
    for char in message:
        if char.isalpha():
            # Calculate the row index in the Vigenère square
            row = ord(key[key_index % len(key)].upper()) - ord('A')
            # Find the column index in the Vigenère square
            for i in range(26):
                if vigenere_square[row][i] == char.upper():
                    column = i
                    break
            # Decrypt the character using the Vigenère square
            decrypted_char = chr(column + ord('A'))
            # Append the decrypted character to the decrypted message
            decrypted_message += decrypted_char
            key_index += 1
        else:
            # Append non-alphabetic characters as-is
            decrypted_message += char
    return decrypted_message

# Decrypt the ciphertext with the Vigenère cipher and print the result
plaintext = decrypt(ciphertext, keyword)
print(plaintext)

