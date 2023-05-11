# function to generate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# function to generate random prime number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_prime():
    while True:
        p = random.randint(2**15, 2**16)
        if is_prime(p):
            return p

# function to generate public and private keys
def generate_keypair(p, q, e):
    n = p * q
    phi = (p-1) * (q-1)

    # choose a random prime number e such that gcd(phi, e) = 1
    while gcd(phi, e) != 1:
        e = generate_prime()

    # calculate d, the modular inverse of e
    d = pow(e, -1, phi)

    return (n, e), (n, d)

# function to encrypt message
def encrypt(public_key, message):
    n, e = public_key
    encrypted_message = pow(message, e, n)
    return encrypted_message

# function to decrypt message
def decrypt(private_key, message):
    n, d = private_key
    decrypted_message = pow(message, d, n)
    return decrypted_message

# main function
if __name__ == '__main__':
    p = int(input("Enter first prime number: "))
    q = int(input("Enter other prime number: "))
    e = int(input("Enter value of e: "))
    message = int(input("Enter plaintext (as number): "))

    #public_key, private_key = generate_keypair(p, q, e)
    #print("Possible values of e and d are:")
    #print(public_key[1], "\t", private_key[1])

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)









"""
Enter first prime number: 53
Enter other prime number: 61
Enter value of e: 17
Enter plaintext (as number): 1234


Input 1:

p = 23
q = 29
e = 11
message = 77
Input 2:

p = 37
q = 41
e = 17
message = 123
"""



"""
RSA is a public-key cryptographic algorithm that was invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977. It is widely used for secure data transmission over the internet and has become an industry standard for encryption.

The RSA algorithm is based on the difficulty of factoring large integers into their prime factors. The security of RSA relies on the fact that it is easy to multiply two large prime numbers, but difficult to factor their product back into the original primes.
"""

"""
The steps of RSA algorithm are as follows:

Select two large prime numbers, p and q.

Calculate the modulus n = p * q.

Calculate the totient of n, phi(n) = (p-1) * (q-1).

Choose a small odd integer e such that e is coprime to phi(n), i.e., gcd(e, phi(n)) = 1.

Calculate the multiplicative inverse of e modulo phi(n), which is a number d such that (d * e) mod phi(n) = 1. The value of d is the private key.

Publish the public key (n, e) and keep the private key (n, d) secret.

To encrypt a message, convert each character into a number using a standard scheme (e.g., ASCII or Unicode) and treat the resulting sequence of numbers as a single large integer. Let M be the message (as a number).

Compute the ciphertext C = M^e mod n.

To decrypt the ciphertext, compute the plaintext P = C^d mod n.

Convert the resulting number back into characters using the same scheme used in step 7.
"""
    
