from Art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a',
            'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

continue_game = True


def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ''
    if shift_amount > 44:
        shifts_modulus = shift_amount * 26
        shifts_modulus += shift_amount
        print(shift_amount)
    if cipher_direction == 'decode':
        shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
    elif cipher_direction == 'encode':
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
    print(end_text)


while continue_game is not False:
    direction = str(input("type Decode decrypt or type Encode to encrypt: ")).lower()
    text = input('type letter: ').lower()
    shift = int(input('the amount of shifts: '))
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    enter_continue = input('Do you still want to continue yes/no: ')
    if enter_continue == 'no':
        continue_game = False
    else:
        pass
