from MorseTranslator import MORSE_CODE_DICT

morse_dict = MORSE_CODE_DICT

enter = input("Enter your input:\n")
out=""
with open("output.txt","w") as file:
    for char in enter:
        convert = char.upper()
        file.write(morse_dict[convert])

