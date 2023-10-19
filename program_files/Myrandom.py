#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        

