def is_leap(year):
    """
    it returns True or False on based on the input of year
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print(is_leap(2021))
