'''
# WHILE LOOPS in python:

 In Python, a while loop is used to repeatedly execute a block of code as long as a certain condition 
 is true. The loop continues running until the condition becomes false. 

 The basic syntax of a while loop in Python is as follows:

    while condition:
        # Code to be executed as long as the condition is true

    Here's a breakdown of the components:

        * while: The keyword that starts the loop.
        * condition: A boolean expression that determines whether the loop should continue running.
        * : A colon to indicate the start of the loop block.
        * Indented code block: This is where you put the code that will be executed as long as the condition is true.


'''

# Example :

count = 0
while count < 5:
    print(count)
    count += 1

# while loop to take input from the user until a specific condition is met:

password = "secret"
input_password = input("Enter the password: ")

while input_password != password:
    print("Incorrect password. Try again.")
    input_password = input("Enter the password: ")

print("Access granted!")

