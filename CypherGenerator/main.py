import resources

print(resources.logo)


def encode(message, shift):
    coded_text = ""
    for char in message:
        if char in resources.alphabet:
            position = resources.alphabet.index(char)
            new_posi = position + shift
            shifted_char = resources.alphabet[new_posi]
            coded_text += shifted_char
        else:
            coded_text += char
    print(f"Your encoded text is : {coded_text}")


def decode(message, shift):
    original_text = ""
    for char in message:
        if char in resources.alphabet:
            position = resources.alphabet.index(char)
            new_posi = position - shift
            shifted_char = resources.alphabet[new_posi]
            original_text += shifted_char
        else:
            original_text += char
    print(f"Your decoded text is : {original_text}")


action = input("Type 'Decode' to decrypt or 'Encode' to encrypt the data: ")
message = input("Type your message:\n")
input_shift = int(input("Enter the shift digit:\n"))
shift = input_shift % 26

if action == "Decode":
    decode(message, shift)
elif action == "Encode":
    encode(message, shift)
else:
    print("Invalid Instruction!")
