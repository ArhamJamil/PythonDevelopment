'''

What Are STRINGS ?

    In Python, a string is a sequence of characters or array of textual data enclosed within either 
    single ('') or double ("") quotation marks. Strings are used to represent text data and can 
    contain letters, numbers, symbols, and spaces.

    Python provides a wide range of built-in string methods that allow you to manipulate and modify
    strings. You can perform operations like converting cases, splitting, joining, replacing, 
    and more using these methods.

    Keep in mind that strings are immutable in Python, which means you cannot change a single character 
    within a string directly. Instead, you create new strings with modifications.


'''

# Creating strings
single_quoted_string = 'Hello, World!'
double_quoted_string = "Python Programming"

# Printing strings
print(single_quoted_string)   # Output: Hello, World!
print(double_quoted_string)   # Output: Python Programming

# Concatenating strings
concatenated_string = single_quoted_string + ' ' + double_quoted_string
print(concatenated_string)    # Output: Hello, World! Python Programming

# Accessing characters in a string
first_character = single_quoted_string[0]  # Indexing starts from 0
print(first_character)        # Output: H

# Slicing strings
substring = double_quoted_string[0:6]  # Slicing from index 0 to 5 (6-1)
print(substring)              # Output: Python

# String length
length = len(single_quoted_string)
print(length)                # Output: 13

# String methods
uppercase_string = single_quoted_string.upper()
print(uppercase_string)      # Output: HELLO, WORLD!

lowercase_string = double_quoted_string.lower()
print(lowercase_string)      # Output: python programming

# Checking if a substring is present in a string
contains_world = single_quoted_string.__contains__('World')
print(contains_world)        # Output: True

# Looping through String
for character in double_quoted_string: {
    print(character)
    # the loop iterate and access each character one by one until the end of string
}


