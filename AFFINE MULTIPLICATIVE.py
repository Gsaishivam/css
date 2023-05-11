# Function to find modular inverse of a number
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1
 
 
# Function to encrypt the plaintext using the Affine Cipher
def encrypt(plaintext, key):
    # Unpack the key into its components
    a, b = key
 
    # Convert the plaintext to uppercase and remove any spaces
    plaintext = plaintext.upper().replace(" ", "")
 
    # Initialize the ciphertext to an empty string
    ciphertext = ""
 
    # Iterate over each character in the plaintext
    for char in plaintext:
        # Apply the encryption formula
        ciphertext += chr(((ord(char) - 65) * a + b) % 26 + 65)
 
    return ciphertext
 
 
# Function to decrypt the ciphertext using the Affine Cipher
def decrypt(ciphertext, key):
    # Unpack the key into its components
    a, b = key
 
    # Find the modular inverse of a
    a_inv = mod_inverse(a, 26)
 
    # Initialize the plaintext to an empty string
    plaintext = ""
 
    # Iterate over each character in the ciphertext
    for char in ciphertext:
        # Apply the decryption formula
        plaintext += chr(((ord(char) - 65 - b) * a_inv) % 26 + 65)
 
    return plaintext
 
 
# Get user input for the plaintext and key values
plaintext = input("Enter the plaintext: ")
a = int(input("Enter the value of K1 (should be coprime with 26): "))
b = int(input("Enter the value of K2: "))
key = (a, b)
 
# Encrypt the plaintext using the Affine Cipher
ciphertext = encrypt(plaintext, key)
 
# Decrypt the ciphertext using the same key
decrypted_text = decrypt(ciphertext, key)
 
# Print the results
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext)
print("Decrypted Text: " + decrypted_text)
