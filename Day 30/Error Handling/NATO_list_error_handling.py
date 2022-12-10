import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

my_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(my_dictionary)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    pno = input("Please enter a word:\n").upper()
    try:
        my_list = [my_dictionary[letter] for letter in pno]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(my_list)


generate_phonetic()
