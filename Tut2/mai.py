'''
What are variables ?

    ->  Variables is like a container that holds data , similar as containers in our kitchen holding 
        Salt, Masala , Pepper etc ... Creating a variable is like creating Placeholder in memory and
        assigning it a value.

What is DataType ?

    ->  Datatype specifies the type of value a variable hold. This is required in programming to do 
        various task/operations without causing an error.

        1. Numeric data: int, float, complex :
        
            int: 3, -8, 0
            float: 7.349, -9.0, 0.0000001
            complex: 6 + 2i

        2. Text data: str :

            str: "Hello World!!!", "Python Programming"

        3. Boolean data :

            Boolean data consists of values True or False.

        4. Sequenced data: list, tuple : 

            List : A list is an ordered collection of data with elements separated by a comma and 
            enclosed within square brackets. Lists are mutable and can be modified after creation.

            Tuple : A tuple is an ordered collection of data with elements separated by a comma and 
            enclosed within parentheses. Tuples are immutable and can not be modified after creation.

        5. Mapped data: dict :

            dict : A dictionary is an unordered collection of data containing a key:value pair. 
            The key:value pairs are enclosed within curly brackets.


'''

var_1 = "arham"
var_2 = 27
var_3 = True
var_4 = None
var_5 = [8, 2.3, [-4, 5], ["apple", "banana"]]
var_6 = (("parrot", "sparrow"), ("Lion", "Tiger"))
var_7 = {

    "name":"Sakshi", 
    "age":20,
    "canVote":True
}


print(var_1, "The type of var_1 is: ", type(var_1))
print(var_2, "The type of var_2 is: ", type(var_2))
print(var_3, "The type of var_3 is: ", type(var_3))
print(var_4, "The type of var_4 is: ", type(var_4))
print(var_5, "The type of var_5 is: ", type(var_5))
print(var_6, "The type of var_6 is: ", type(var_6))
print(var_7, "The type of var_7 is: ", type(var_7))
