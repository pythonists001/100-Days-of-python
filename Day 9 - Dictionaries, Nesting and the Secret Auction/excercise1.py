programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    }

print(programming_dictionary["Function"])

## adding data to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

## an empty list
list1 = []
## an empty dictionary
dict1 = {}

## wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


## Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

## Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
# prints the below i.e only keys are retrieved.
"""
Bug
Function
Loop 
"""


## to get both keys and value
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
## Prints the below.. i.e with key and value
"""
Bug
A moth in your computer.
Function
A piece of code that you can easily call over and over again.
Loop
The action of doing something over and over again 
"""
