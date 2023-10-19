#!/usr/bin/env python # -*- coding: utf-8 -*-
import sys, os

print("Welcome to the morse code translator")
curOS = sys.platform
cont = 'n'

if curOS == 'darwin':
    print("You are using MacOS. Some things may be broken.")
while True:
    try:

        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                            'C':'-.-.', 'D':'-..', 'E':'.',
                            'F':'..-.', 'G':'--.', 'H':'....',
                            'I':'..', 'J':'.---', 'K':'-.-',
                            'L':'.-..', 'M':'--', 'N':'-.',
                            'O':'---', 'P':'.--.', 'Q':'--.-',
                            'R':'.-.', 'S':'...', 'T':'-',
                            'U':'..-', 'V':'...-', 'W':'.--',
                            'X':'-..-', 'Y':'-.--', 'Z':'--..',
                            '1':'.----', '2':'..---', '3':'...--',
                            '4':'....-', '5':'.....', '6':'-....',
                            '7':'--...', '8':'---..', '9':'----.',
                            '0':'-----', ', ':'--..--', '.':'.-.-.-',
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-'}
         
        def encrypt(message):
            cipher = ''
            for letter in message:
                if letter != ' ':

                    cipher += MORSE_CODE_DICT[letter] + ' '
                else:

                    cipher += ' '
         
            return cipher
         
        def decrypt(message):

            message += ' '
         
            decipher = ''
            citext = ''
            for letter in message:
                if (letter != ' '):
                    i = 0
                    citext += letter

                else:
                    i += 1
                    if i == 2 :
                        decipher += ' '
                    else:
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                        .values()).index(citext)]
                        citext = ''
         
            return decipher
         

        def main():
            while (True):
                message = input("Enter Code or 'q' to quit:")
                if message == 'q' or message == 'q\n' or message == 'q ':
                    print("Shutting down...")
                    sys.exit(0)
                result = decrypt(message)
                print('')
                print("===========Result===========\n")
                print("( {} )".format(result))
                print("===========Restart==========")
         

        if __name__ == '__main__':
            main()
    except SystemExit as errorcode:
        sys.exit(errorcode)
    except:
        print("ERROR")
        
    finally:
        print("Closed Successfully")
        
