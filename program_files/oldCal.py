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
from time import sleep
print("Welcome To The Calculator")

writePath = os.getcwd()
writePath = writePath.replace('program files', '') + '/'

sleep(0.2)
print()
while(True):
    try:
        sy = input("Press [a] To Abort, [l] for large number mode, [Enter] to continue, or [r] to return to robo:")

        if(sy == 'a'):
            sys.exit(0)

        sleep(0.3)

        if(sy == 'r'):
            #print("Sorry, The Action You Requested Is Not Currently Available")
                        
            sys.exit(0)
            sy = ''

        if(sy != '' and sy != 'l'):
            raise Exception("Incorrect Answer")

        print("\n")
        num = input("Enter Number: ")
        sleep(0.1)
        operation = input("Enter Operator: ")
        sleep(0.1)
        num2 = input("Enter Second Number: ")

        if(sy != 'l'):
            num = float(num)
            num2 = float(num2)

        sleep(0.1)

        if(sy == 'l'):
            num = float(num)
            num2 = float(num2)

            print(num)
            # num = int(num)

        if(operation == "^"):
            answer = num ** num2
        elif(operation == "/"):

            answer = num // num2
            # answer = num / num2
        elif(operation == "*"):
            answer = num * num2
        elif(operation == "+"):
            answer = num + num2
        elif(operation == "-"):
            answer = num - num2

        else:
            print("ERROR")
            num = "ERROR"
            num2 = "ERROR"
            answer = "ERROR"
            print(answer)

        if(answer != "ERROR"):
            i = 0
            print(answer)
            with open(f'{writePath}calanswer.txt','w') as f:
                                    f.write(str(answer))
            #print("The Power Of COOCHIE MAN Has Granted You The Answer")
            print("=========RESTART=========")
            print()

    except Exception as error:
        print(error)
    


