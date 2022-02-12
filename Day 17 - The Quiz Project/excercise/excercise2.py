class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "Arvind")
print(user_1.username)
print(user_1.id)

"""
Constructor
============
class Car:
    def __init__(self):
        #initialise attributes



## Attribute ##has

class Car:
    def __init__(self, seats):
        self.seats = seats

## Method is something which does something
    def enter_race_mode():
        seats = 2
"""
