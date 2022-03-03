## Unlimited Arguments

from symtable import Class


def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5,4,6,8,9))

"""
def calculate(**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    print(kwargs["add"])


calculate(add=5, multiply=8)

"""
def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(4, add=5, multiply=8)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")#kw["make"]
        self.model = kw.get("model")#kw["model"]
        self.color = kw.get("color")

# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)
# print(my_car.make)

my_car = Car(color="red")
print(my_car.color)

my_dict = {
    "name" : "Arvind",
    "profession": "Engineer"
}

print(my_dict.get("name"))