# with open("Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv") as f:
#     contents = f.readlines()
#     print(contents)
#     for _ in contents:
#         print(_.strip())

# import csv
# with open("Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd
data = pd.read_csv("Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# # print(f"avg={round(sum(temp_list)/len(temp_list),2)}")
# print(data["temp"].mean())
# print(data["temp"].max())

## Get data in row
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])

## pull row data where temperature is max
print(data[data.temp == data.temp.max()])

#getting a specific value from a row
monday = data[data.day == "Monday"]
print(monday.condition)
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)


# Create a dataframe from scratch
data_dict = {
    "students" : ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")