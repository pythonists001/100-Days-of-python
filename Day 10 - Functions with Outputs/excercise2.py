## Multiple return values
def format_name(f_name, l_name):
    '''
    This function takes in two parameters, f_name and l_name, and returns a formatted string
    
    :param f_name: first name, l_name: last name
    :param l_name: The last name of the person to be formatted
    :return: the string "Invalid input."
    '''
    if f_name == "" or l_name == "":
        return f"Invalid input."
    formatted_fname = f_name.title()
    formatted_lname = l_name.title()
    return f"Result: {formatted_fname} {formatted_lname}"


print(format_name(input("Enter first name : "),
                  input("Enter last name: ")))
