def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase then encrypt it accordingly 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

plaintext = input("ENTER STRING TO ENCRYPT : ")
n = int(input("Enter key : "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext,n))

def decrypt_text(ciphertext, n):
    ans = ""
    # iterate over the given text
    for i in range(len(ciphertext)):
        ch = ciphertext[i]

        # check if space is there then simply add space
        if ch == " ":
            ans += " "
        # check if a character is uppercase then decrypt it accordingly 
        elif ch.isupper():
            ans += chr((ord(ch) - n - 65) % 26 + 65)
        # check if a character is lowercase then decrypt it accordingly 
        else:
            ans += chr((ord(ch) - n - 97) % 26 + 97)

    return ans

ciphertext = input("ENTER STRING TO DECRYPT : ")
print("Cipher Text is : " + ciphertext)
print("Shift pattern is : " + str(n))
print("Plain Text is : " + decrypt_text(ciphertext,n))
