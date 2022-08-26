path = "c:\PyLearning\projects\Day 24 - Mail automation"
list_of_names = []

with open (path + "/Input/Names/invited_names.txt") as file:
    for line in file:
        list_of_names.append(line.strip())

for name in list_of_names:
    with open (path + "/Input/Letters/starting_letter.txt") as file:
        letter = file.read()
    letter = letter.replace("[name]", name)

    with open (f"{path}/Output/ReadyToSend/{name}.txt", mode="w") as new_file:
        new_file.write(letter)
        new_file.close()