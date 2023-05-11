import math

def encrypt(message):
    # Determine the size of the grid based on the length of the message
    size = math.ceil(math.sqrt(len(message)))
    
    # Pad the message with spaces as needed to fill the grid
    message += ' ' * (size**2 - len(message))
    
    # Create the grid and fill it with the message
    grid = []
    for i in range(size):
        row = message[i*size : (i+1)*size]
        grid.append(row)
    
    # Transpose the grid to create the ciphertext
    ciphertext = ''
    for i in range(size):
        for j in range(size):
            ciphertext += grid[j][i]
    
    return ciphertext

def decrypt(ciphertext):
    # Determine the size of the grid based on the length of the ciphertext
    size = math.ceil(math.sqrt(len(ciphertext)))
    
    # Create the grid and fill it with the ciphertext
    grid = []
    for i in range(size):
        row = ciphertext[i*size : (i+1)*size]
        grid.append(row)
    
    # Transpose the grid to recover the plaintext
    plaintext = ''
    for i in range(size):
        for j in range(size):
            plaintext += grid[j][i]
    
    # Remove any trailing spaces that were added during encryption
    plaintext = plaintext.rstrip()
    
    return plaintext



message = input("Enter Message : ")
ciphertext = encrypt(message)
print(ciphertext)

plaintext = decrypt(ciphertext)
print("\nDecrypted message : \n",plaintext)

