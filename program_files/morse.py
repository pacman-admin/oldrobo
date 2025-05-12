'''
Copyright (c) 2020-2025 Langdon Staab, 2020-2022 Edison Wang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
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
        
