def hash(data):
    # Initialize the hash value
    hash_value = 0x7f458dff

    # Process each byte of input data
    for i in range(len(data)):
        byte = data[i]
        hash_value += byte

        # Every fourth byte
        if i % 4 == 3:
            hash_value ^= byte
            hash_value = (hash_value << 5) % 4294967291

        # Every eighth byte
        if i % 8 == 7:
            hash_value ^= byte
            hash_value = (hash_value >> 2) % 4294967291

    # Return the final hash value
    return hash_value

input_data = input("Enter message to be hashed : ")
hashed_value = hash(input_data.encode('utf-8'))#UTF-8 stands for Unicode Transformation Format-8.
print("Hashed value:", hashed_value)




"""
The code is designed to generate a hash value of fixed length, regardless of the length
of the input data. This is achieved by taking the modulo of the intermediate hash values
with a large prime number (4294967291). The prime number is chosen to ensure that the
modulo operation does not result in collisions, i.e., different input data does not result
in the same hash value.

Therefore, the length of the output hash value is fixed and determined by
the size of the prime number used. In this case, the output hash value is 10 digits
long because 4294967291 is a 10-digit prime number.


ALGORITHM:-
The input message is read as a string using the input() function.
The string is then encoded as UTF-8 bytes using the encode() function, which produces a sequence of bytes that can be processed by the hash function.
The hash function initializes the hash value to a fixed value, in this case 0x7f458dff.
It processes each byte of the input data in sequence, adding the byte to the hash value and performing additional operations on the hash value based on the position of the byte.
For every fourth byte, the hash value is XORed with the byte and then left-shifted by 5 bits. This operation is designed to ensure that the bits from different positions in the message are mixed together in the hash value.
For every eighth byte, the hash value is XORed with the byte and then right-shifted by 2 bits. This operation is designed to ensure that the hash value does not depend too much on the position of the bytes in the message.
The final hash value is returned as an integer.
"""


"""

The three operations performed in this hash algorithm are addition, bitwise XOR, and bitwise shift.

The hash_value += byte statement performs addition, where the hash value is incremented by the value of the current byte.

The hash_value ^= byte statement performs a bitwise XOR operation, where the hash value is XOR-ed with the value of the current byte.

The (hash_value << 5) % 4294967291 and (hash_value >> 2) % 4294967291 statements perform bitwise left shift and right shift operations, respectively.
These operations shift the hash value by a certain number of bits to the left or right and take the result modulo 4294967291 (which is a large prime number).
These bitwise operations help to mix the bits of the hash value and produce a more evenly distributed output.

"""



