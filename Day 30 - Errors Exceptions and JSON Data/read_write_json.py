import json


def read_data():
    website = ""
    email = ""
    password = ""
    website = input("Enter Website name")
    email = input("Enter email")
    password = input("Enter password")
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    try:
        with open("./Day 30 - Errors Exceptions and JSON Data/data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        with open("./Day 30 - Errors Exceptions and JSON Data/data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
            # Updating old data
            data.update(new_data)
            with open("./Day 30 - Errors Exceptions and JSON Data/data.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)
    # finally:
    #     website_entry.delete(0, END)
    #     password_entry.delete(0, END)
def find_password(website):
    try:
        with open("./Day 30 - Errors Exceptions and JSON Data/data.json") as data_file:
                # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        print("No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            return f"{email} : {password}"
        else:
            print("No details found for this {website}")
    

            # for (key, value) in data.items():
            #     print(f"{key.email}")
            # messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}"")
# read_data()
print(find_password("Ebay"))