# Caesar Cipher
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
stop_program = 0


def encrypt(encrypting, mod):

    modified_word = ''

    for letter in encrypting:
        if letter in alphabet:
            list_index.append(int(alphabet.index(letter)))
        else:
            list_index.append(letter)

    for n in list_index:
        if type(n) == int:
            if n + mod > 25:
                modified_index.append(n + mod - 26)
            else:
                modified_index.append(n + mod)
        else:
            modified_index.append(n)

    for o in modified_index:
        if type(o) == int:
            modified_word += alphabet[o]
        else:
            modified_word += o

    print(modified_word+'\n')


def decrypt(encrypting, mod):

    modified_word = ''

    for letter in encrypting:
        if letter in alphabet:
            list_index.append(int(alphabet.index(letter)))
        else:
            list_index.append(letter)

    for n in list_index:
        if type(n) == int:
            if n - mod < 0:
                modified_index.append(n - mod + 26)
            else:
                modified_index.append(n - mod)
        else:
            modified_index.append(n)

    for o in modified_index:
        if type(o) == int:
            modified_word += alphabet[o]
        else:
            modified_word += o

    print(modified_word+'\n')


def clearconsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


while stop_program == 0:
    shift = 0
    text = ''
    accepted_shift = 0
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit' to stop:\n")
    if direction == 'exit':
        stop_program = 1
        break
    while direction.lower() != 'encode' and direction.lower() != 'decode' and direction.lower() != 'exit':
        direction = input("Invalid input, chose either 'encode', 'decode' or 'exit':\n")
    if direction == 'exit':
        stop_program = 1
        break

    text = input("Type your message:\n").lower()

    while accepted_shift == 0:
        shift_input = input("Type the shift number (0-25):\n")
        try:
            shift = int(shift_input)
            if 0 <= shift < 26:
                accepted_shift += 1
            else:
                shift_input = input("Value must be integer from 0 to 25.\n")
        except ValueError:
            print("Value must be integer from 0 to 25.\n")

    clearconsole()

    list_index = []
    modified_index = []

    if direction.lower() == 'encode':
        encrypt(text, shift)

    elif direction.lower() == 'decode':
        decrypt(text, shift)
    elif direction.lower() == 'exit':
        stop_program = 1
        break
