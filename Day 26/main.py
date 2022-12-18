# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# squared_numbers = [x for x in numbers if x % 2 == 0]
#
# print(squared_numbers)
#
# string = "\n456\n"
#
# print(int(string))
#
# passed_students = {key:value for (key, value) in students_scores.items() if value >= 60}

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

my_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(my_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
pno = input("Please write a word:\n").upper()

my_list = [my_dictionary[letter] for letter in pno]

print(my_list)

