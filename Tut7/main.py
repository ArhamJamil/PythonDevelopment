"""
# BITWISE Operators:
 
    In Python, bitwise operators are used to perform operations on individual bits of integers. 
    These operators are commonly used in low-level programming, hardware manipulation, 
    and certain algorithmic optimizations.

    Python supports several bitwise operators:

   * Bitwise AND (&): Performs a bitwise AND operation on corresponding bits of two integers. 
                     If both bits are 1, the result bit is 1; otherwise, it's 0.

   * Bitwise OR (|): Performs a bitwise OR operation on corresponding bits of two integers. 
                    If either of the bits is 1, the result bit is 1.

   * Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation on corresponding bits of two integers. 
                     If the bits are different, the result bit is 1; otherwise, it's 0.

   * Bitwise NOT (~): Flips the bits of an integer, changing 0s to 1s and 1s to 0s. It also has the effect 
                     of negating the integer and subtracting 1.

   * Left Shift (<<): Shifts the bits of an integer to the left by a specified number of positions, 
                     filling the vacated positions with zeros.

   * Right Shift (>>): Shifts the bits of an integer to the right by a specified number of positions, 
                      filling the vacated positions with zeros.


"""

# Bitwise AND :

a = 5  # 101 in binary
b = 3  # 011 in binary
result = a & b  # 001 (1 in decimal)
print("a & b :", result)

# Bitwise OR:
 
a = 5  # 101 in binary
b = 3  # 011 in binary
result = a | b  # 111 (7 in decimal)
print("a | b :", result)


# Bitwise XOR :

a = 5  # 101 in binary
b = 3  # 011 in binary
result = a ^ b  # 110 (6 in decimal)
print("a ^ b :", result)

# Bitwise NOT :

a = 5   # 101 in binary
result = ~a  # -6 (complement of 101 is 010, which is 6, and then negate)
print("~a :", result)

# Bitwise LEFT SHIFT :

a = 5       # 101 in binary
shifted = a << 2  # 10100, which is 20 in decimal
print("a << 2 :", shifted)


# Bitwise RIGHT SHIFT:

a = 20      # 10100 in binary
shifted = a >> 2  # 00101, which is 5 in decimal
print("a >> 2 :", shifted)