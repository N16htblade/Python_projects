import pandas

path = R"C:\PyLearning\projects\Day 26 - NATO Alphabet\nato_phonetic_alphabet.csv"

nato = pandas.read_csv(path)
df = pandas.DataFrame(nato)

nato_dic = {row.letter:row.code for (index, row) in nato.iterrows()}


def generate():
    user = input("What is  your name?: ").upper()
    try:
        nato_code = [nato_dic[letter] for letter in user]
    except KeyError:
        print("Sorry, only letters please")
        generate()
    else:        
        print (nato_code)

generate()