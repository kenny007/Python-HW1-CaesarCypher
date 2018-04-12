# This script used caesars cipher to encrypts or decrypts the content of a text file (shifted by 5)
# Adebayo Kehinde Omotola
# Python Assignment 1


import string
import sys
# Still needs some reduction in cipher and decipher functions
# Also ciphers space character, which is located at 26th index
letters = (string.ascii_lowercase + ' ') * 2


def caesar_cipher(cipher_file):
    with open(cipher_file, 'r+') as c:
        file_content = c.read()
        c.seek(0)
        c.truncate()
        c.write(''.join([letters[letters.index(i) + 5] for i in list(file_content.lower())]))
    return


def decipher(ciphered_file):
    with open(ciphered_file, 'r+') as c:
        file_content = c.read()
        c.seek(0)
        c.truncate()
        c.write(''.join([letters[letters.index(i) - 5] for i in list(file_content.lower())]))
    return


def cipher_decipher():
    try:
        filename = input('Please enter filename(case sensitive): \n')
        with open(filename, 'r+') as f:
            print('e. Encrypt')
            print('d. Decrypt')
            user_input = input("Please choose what you would like to with this file: \n")
            if user_input == 'e':
                caesar_cipher(filename)
                print('File successfully encrypted')
            elif user_input == 'd':
                decipher(filename)
                print('File successfully descrypted')
            else:
                print('Try again.')
                cipher_decipher()
    except FileNotFoundError:
        print('Please make sure that your file is in the same directory with this program.')
        cipher_decipher()
    answer = input('Do you want to continue? Y or N \n')
    if answer == 'Y':
        cipher_decipher()
    elif answer == 'N':
        print('Exiting...')
        sys.exit()
    return


cipher_decipher()
