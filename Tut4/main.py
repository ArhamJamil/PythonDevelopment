'''

In Python, the if...else statement is used for conditional execution. It allows you to execute 
certain blocks of code based on whether a given condition is true or false. 
Here's the basic syntax:

    if condition:
        # Code to execute if the condition is true
    else:
        # Code to execute if the condition is false


You can also extend this structure with additional elif (short for "else if") blocks to handle multiple conditions.

# Conditional Operator : 
    * == (equals to)
    * != (not equals to)
    * >
    * <
    * >=
    * <=



# AND | OR | NOT operators: 

 In Python, the and, or, and not operators are used for combining and negating conditions within logical expressions. 
 These operators are often used in conjunction with if statements to create more complex conditionals.
 
    * AND Operator:
        The and operator is used to combine multiple conditions, and it returns True if 
        all conditions are true, otherwise, it returns False.

    * OR Operator:
        the or operator is used to combine multiple conditions, and it returns True if 
        at least one of the conditions is true, otherwise, it returns False.

    * NOT Operator :
        The not operator is used to negate a condition, flipping its truth value. If a condition is True, 
        NOT makes it False, and if a condition is False, NOT makes it True.


'''

condition1 = True
condition2 = False

result1 = condition1 and condition2
result2 = condition1 or condition2
result3 = (not condition1) and (not condition2)
print(result1)  # Output: False
print(result2)  # Output: True
print(result3)  # Output: False



# Example: Checking the value of a variable
print("Example: Checking the value of a variable\n")
x = int(input("Enter an Integer Number ? "))
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


print("Example: Combining these operators with if statements\n")
#Combining these operators with if statements can lead to more intricate conditionals.
age = int(input("Enter your age ? "))
is_student = input("Are you student (Y/N) ? ")
Value = False
if (is_student == 'Y') or (is_student == 'y'):
    Value = True
else:
    Value = False

if age >= 18 and (Value == False):
    print("You're eligible to vote.")
elif age >= 18 and (Value == True):
    print("You can register to vote, but you might be a student.")
else:
    print("You're not eligible to vote.")


# Example: Nested if...else statements
print("Example: Nested if...else statements\n")
age = 25

if age >= 18:
    if age < 21:
        print("You're an adult, but not old enough to drink.")
    else:
        print("You're an adult and can legally drink.")
else:
    print("You're a minor.")

