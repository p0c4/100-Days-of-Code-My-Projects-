import pandas


data = pandas.read_csv("2018_Report.csv")

black_squirrels = data[data["Primary Fur Color"] == "Black"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]

gray = len(grey_squirrels)
cinnamon = len(cinnamon_squirrels)
black = len(black_squirrels)

my_dict = {"Fur color" : ["gray", "cinnamon", "Black"], "Count" : [gray, cinnamon, black]}

dict = pandas.DataFrame(my_dict)
dict.to_csv("color_data.csv")

print(dict)
