import pandas as pd

data = pd.read_csv("Day 25 - Working with CSV Data and the Pandas Library/Squirrel_Data.csv")
# grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels)
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pd.DataFrame(data_dict)
df.to_csv("squirell_count.csv")
