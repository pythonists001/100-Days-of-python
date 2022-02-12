import math


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        return is_prime


for i in range(2, 101):
    if prime_checker(i):
        print(i)
