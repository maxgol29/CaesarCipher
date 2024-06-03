def encode(text1, replace1):
    output = []
    for letter in text1:
        number_char = ord(letter)
        if letter is None:
            output.append(letter)
        elif number_char >= 97 and number_char <= 122:
            number_char = ord(letter) + replace1
            if number_char > 122:
                number_char -= 25
        output.append(chr(number_char))
    return output
def decode(text2, replace2):
    output = []
    for letter in text2:
        number_char = ord(letter)
        if letter is None:
            output.append(letter)
        elif number_char >= 97 and number_char <= 122:
            number_char = ord(letter) - replace2
            if number_char < 97:
                number_char += 25
        output.append(chr(number_char))
    return output
def ceasar(type_of_cipher, text, replace):
    if type_of_cipher == 'encode':
        return encode(text1=text, replace1= replace)
    elif type_of_cipher == 'decode':
        return decode(text2=text, replace2=replace)
    else:
        return 'Incorrect decision, try again.'
def game():
    answer = 'yes'
    while answer == 'yes':
        decision = input("type 'encode' to encrypt, type 'decode' to decrypt: \n")
        message = input("Type your message: \t").lower()
        shift = int(input("Type the shift number: \t"))
        print(''.join(ceasar(type_of_cipher=decision, text=message, replace=shift)).capitalize())
        answer = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
game()
