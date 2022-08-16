from art import logo

def caesar(text, shift, direction):
    new_text = ""
    if direction == "decode":
        shift *= -1
    for character in text:        
        if character not in alphabet:
            new_text += character
        else:
            position = alphabet.index(character)
            new_position = position + shift
            if new_position > 25 or new_position < 0:
                new_position %= 26
            new_text += alphabet[new_position]
                
    print (f"Your {direction}d text is {new_text}.\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print (logo)
replay = "yes"

while replay == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    replay = input("Would you like to go again? Type \"yes\" or \"no\": ").lower()