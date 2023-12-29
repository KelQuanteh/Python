# Original text and shift value
text = 'where are you now'
shift = 7

# Function to perform Caesar cipher encryption
def caesar(message, offset):
    # Define the alphabet for encryption
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Initialize an empty string to store the encrypted text
    encrypted_text = ''

    # Iterate through each character in the input message
    for char in message.lower():
        # Check if the character is a space
        if char == ' ':
            # If it is a space, append it to the encrypted text as is
            encrypted_text += char
        else:
            # If it is not a space, find the index of the character in the alphabet
            index = alphabet.find(char)
            
            # Calculate the new index after applying the Caesar cipher shift
            new_index = (index + offset) % len(alphabet)
            
            # Append the encrypted character to the encrypted text
            encrypted_text += alphabet[new_index]

    # Print the original and encrypted texts
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Call the caesar function with the provided text and shift
caesar(text, shift)
