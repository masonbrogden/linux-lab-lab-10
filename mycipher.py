import sys

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shifted = ord(char.upper()) + shift - ord('A')  # Shift the character
            encrypted_char = chr((shifted % 26) + ord('A'))  # Ensure it wraps around if needed
            encrypted_message += encrypted_char
    return encrypted_message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift_amount>")
        sys.exit(1)

    shift_amount = int(sys.argv[1])

    for line in sys.stdin:
        message = line.strip().upper()  # Read and convert the message to uppercase
        encrypted_message = caesar_cipher(message, shift_amount)
        # Print the encrypted message in blocks of five letters
        for i in range(0, len(encrypted_message), 5):
            print(encrypted_message[i:i+5], end=" ")
        print()
