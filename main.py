# choice = int(input('1) Encrypt\n2) Decrypt\nChoice: '))
# Ternary
# user_string = input(f'What would you like to {"encrypt" if choice == 1 else "decrypt"}: ')
# shift_amount = int(input('How much to shift by?: '))

choice = 1
user_string = 'hello andrew'
new_string = ''
shift_amount = 7

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z']

if choice == 1:
    for letter in user_string:
        new_string += chr(((ord(letter) - 65 + shift_amount) % 26) + 65)
        # letter_num = ord(letter) - 65
        # letter_num += shift_amount
        #
        # print(letter_num % 26)
        # # while letter_num > 25:
        # #     letter_num -= 26
        #
        # print(letter_num)
        #
        # new_string += chr(letter_num + 65)

elif choice == 2:
    # do decrypt stuff
    pass

print(f'Given:    {user_string}')
print('Expected: OLSV HUKYLD')
print(f'Got:      {new_string}')
