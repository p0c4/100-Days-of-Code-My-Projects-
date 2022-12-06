weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def convert(celcius):
    fahrenheit = celcius * 9 / 5 + 32
    return fahrenheit

weather_f = {day:convert(celcius) for (day, celcius) in weather_c.items()}




print(weather_f)
