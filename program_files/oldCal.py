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
    


