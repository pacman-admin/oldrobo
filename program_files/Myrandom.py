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
import random
import sys, os
from time import sleep

print("Welcome To The Electronic Dice Program")
mode = 'Classic'
sleep(0.3)

def randNum(a, b):
    num = random.randint(a,b)
    num = round(num)
    return num
def askQuestions():
    global mode
    sy = input("\nPress [a] to abort, [r] to return to robo, or [Enter] to continue")
    if(sy == 'a'):
        print("Shutting down...")
        sys.exit(0)
    sleep(0.1)

    if(sy == 'r'):
        try:
            sys.exit(0)
        except:
            print("An error occurred while opening robo")

    elif(sy != ''):
        sleep(5)

    ans = input("Would you like to use Clasic View [y/n]")
    if ans == 'n':
        mode = "Num"
    elif ans == 'y':
        mode = "Classic"
    
    if(ans != 'y' and ans != 'n' and ans != 'Y' and ans != 'N'):
        raise Exception("You did not provide a valid answer")






askQuestions()
while(True):
    try:
        cont = input("\nPress [ENTER] to roll the dice or [o] for more options")
        if(cont == 'o'):
            askQuestions()
        else:
            answer = randNum(0, 6)
            if(mode == "Classic"):
                if(answer == 1):
                    print('⚀')
                elif(answer == 2):
                        print('⚁')
                elif(answer == 3):
                        print('⚂')
                elif(answer == 4):
                        print('⚃')
                elif(answer == 5):
                        print('⚄')
                else:
                        print('⚅')
            if(mode == "Num"):
                if(answer > 6):
                      answer = 6
                print(answer)


    except Exception as e:
        print("An error has occured")
        print("Error Type: ",e)
        

