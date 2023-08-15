'''
# FOR LOOP in python :

-> In Python, a for loop is used to iterate over a sequence (like a list, tuple, string, or range) 
   and execute a set of statements for each item in the sequence. 

   The basic syntax of a for loop in Python is as follows:

        for variable in sequence:{
            # Code to be executed for each item in the sequence
        }

    Here's a breakdown of the components:

        * for: The keyword that starts the loop.
        * variable: A variable that takes on the value of each item in the sequence during each iteration.
        * sequence: The collection of items over which you want to iterate.
        * : A colon to indicate the start of the loop block.
        * Indented code block: This is where you put the code that will be executed for each item in the sequence.

    You can also use the built-in range() function to generate a sequence of numbers and 
    iterate over them :

        for i in range(5):{
            print(i)
        } 

        # This loop will print the numbers from 0 to 4.(n-1) here => 5-1 = 4



'''

fruit = "Mango"
for character in fruit:{
    print(character)
}
    
# Example : Iterating FOR loop over a list
'''
 In this example, the loop iterates through the list fruits and assigns each fruit 
 to the variable fruit, then the print(fruit) statement is executed for each fruit in the list. 

 You can also use the "enumerate()" function to iterate over a sequence along with its index:
    The "enumerate()" function in Python is used to iterate over a sequence (like a list, tuple, or string) while keeping 
    track of the index of the current item. It returns a tuple containing both the index and the value 
    of each item during iteration. This can be particularly useful when you want to access both the 
    index and the value of each item within a loop.

 
'''

fruitsList = ["apple", "banana", "cherry"]

for fruit in fruitsList:
    print(fruit)

for index, fruit in enumerate(fruitsList):
    print(f"Index: {index}, Fruit: {fruit}")


# count controlled for loop
'''
    for variable in range(start, stop, step):
        # Code to be executed for each iteration

    * start: The starting value of the range (inclusive). If not provided, it defaults to 0.
    * stop: The stopping value of the range (exclusive). The loop will iterate until one less than this value.
    * step: The increment value between successive numbers in the range. If not provided, it defaults to 1.

'''
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)


# Looping with an index:
'''
 While using enumerate() is usually preferred, sometimes you might need to loop with an index. In such cases, 
 you can use range(len(sequence)) to iterate over indices and access items in the sequence.

'''

fruitsList2 = ["apple", "banana", "cherry"]
for i in range(len(fruitsList2)):
    print(fruitsList2[i])
