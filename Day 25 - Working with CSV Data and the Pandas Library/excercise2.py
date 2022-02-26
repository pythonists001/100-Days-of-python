import pandas as pd
data = pd.read_csv("Day 25 - Working with CSV Data and the Pandas Library/weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(type(temp_list))
# avg_tmp = sum(temp_list)/len(temp_list)
# print(avg_tmp)

# print(data["temp"].mean())

# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)

#Get data in coloumns 
# print(data[data.day == "Monday"])
# # Get row where temp is max
# print(data[data.temp == data["temp"].max()])

## get a value from a row
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9/5 + 32 )

## create a dataframe from scratch
data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

data = pd.DataFrame(data_dict)
print(data)
#data.to_csv("abc.csv")


