

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names = (invited_names.readlines())

for name in names:
    nana = name.strip()
    x = letter.replace("[name],", f"{nana},")
    with open(f"./Output/ReadyToSend/Letter for {nana}", mode="w") as n_letter:
        n_letter.write(x)
