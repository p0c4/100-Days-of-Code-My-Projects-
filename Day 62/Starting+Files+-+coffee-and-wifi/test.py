import pandas
import csv


# data = pandas.read_csv("cafe-data.csv")

# cafe_dict = data.to_dict(orient="records")

# print(cafe_dict)

with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row)

print(list_of_rows)


list_of_rows = [['Cafe Name', 'Location', 'Open', 'Close', 'Coffee', 'Wifi', 'Power'], ['Lighthaus', 'https://goo.gl/maps/2EvhB4oq4gyUXKXx9', '11AM', ' 3:30PM', '☕☕☕☕️', '💪💪', '🔌🔌🔌'],
['Esters', 'https://goo.gl/maps/13Tjc36HuPWLELaSA', '8AM', '3PM', '☕☕☕☕', '💪💪💪', '🔌'], ['Ginger & White', 'https://goo.gl/maps/DqMx2g5LiAqv3pJQ9', '7:30AM', '5:30PM', '☕☕☕', '✘', '🔌'],
['Mare Street Market', 'https://goo.gl/maps/ALR8iBiNN6tVfuAA8', '8AM', '1PM', '☕☕', '💪💪💪', '🔌🔌🔌']]