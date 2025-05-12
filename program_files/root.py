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
import os
import sys
from time import sleep,time as millis
print('Welcome to the square root finder')

writePath = os.getcwd()
writePath = writePath.replace('program_files', '') + '/'

startMillis = millis()
endMillis = millis()
backSlash = '\\'
spinCursor = ['-', backSlash, '|', '/']
useInt = False
keepGoing = 'n'
c = True
run = 1000000
expnent = 2
if sys.platform == 'darwin':
    interval = 2048
else:
    interval = 256
saveRoot = 'n'
while(1):
    try:
        larNM = False
        sy = input ('Press [q] To Quit, [l] for large number mode or [Enter] to continue:')
        if sy == 'q' or sy == 'Q':
            sys.exit(0)
        elif(sy == 'r'):
            print('Returning to Robo...')
            os.system('python robo.py')
        elif(sy == 'l'):
            print('Large Number Mode Enabled')
            larNM = True
        if c :
            num = input("Enter number or type 'f' to read file")
            if(num == 'f'):
                with open(f'{writePath}root.txt') as numF:
                    num = numF.readline()
                    print(num)
                    num.replace('b', '')
                    num.replace("'", '')
                    num.replace("'", '')


            num = int(num)

        if(num > 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368):
            print('Number too large for float value.\nInteger value can be used at the expense of precision')
            useInt = input('Use integer value? y/n')
            if useInt == 'y':
                useInt = True
                larNM = True
            else:
                useInt = False
                continue


        if (larNM == True):
            print('Large Number Mode Enabled')
            if(num < 3351951982485648902752079410200733570616051816489776755366513689023594143395404763713153060481989113912689999099675945603027408294703540516892378400817152):
                larNM = False
                guess = num / 2
            else:
                #guess = num // 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368
                guess = num

        else:
            guess = num / 2

        answer = 0
        done = False

        bestP = False
        i = 0


        lastGuess = 0
        if(done == False):
            #print(guess)
            sys.stdout.write('   Calculating root...')
            startMillis = millis()
            if (useInt == True):

                while(1):
                    cursor = spinCursor[round(i/1024)%4]
                    sys.stdout.write('\r{}'.format(cursor))
                    sys.stdout.flush()
                    #one microsecond delay to help the computer
                    sleep(0.000001)
                    guess = (guess+num//guess) // 2
                    if(guess == lastGuess):
                        bestP = True
                        answer = guess
                        done = True
                        break

                    i += 1
                    if(i % run == 0):
                        done = True
                        keepGoing = input('Program has run one billion times. Continue? y/n')
                        if(keepGoing == 'n'):
                            print('Operation canceled')
                            break
                        else:
                            done = False     
                    #print(guess)
                    lastGuess = guess
            else:
                while(1):


                    cursor = spinCursor[round(i/1024)%4]
                    sys.stdout.write('\r{}'.format(cursor))
                    sys.stdout.flush()
                    #one microsecond delay to help the computer
                    sleep(0.000001)
                    guess = (guess + num / guess) / 2
                    #print(guess)
                    if(guess == lastGuess):
                        bestP = True
                        answer = guess
                        done = True
                        break
                    i += 1
                    if(i > run):
                        done = True
                        raise Exception('Program loop limit exceeded')
                        break
                    lastGuess = guess
        endMillis = millis()
        if(useInt == True):
            answer = int(answer)
        else:
            answer = float(answer)
        if(done):
            print('\n\n\n')
            if(guess ** expnent == num):
                print('A Perfect Answer Was Created')
                answer = guess
            elif bestP:
                print('The Best Possible Root Was created')
            print(answer)
            print('The program looped',i,'times and ran for',round((endMillis-startMillis)*1000)/1000,'seconds.')
            saveRoot = input('Would you like to save this root in sqRoot.txt?(y/n)')
            if saveRoot == 'y':
                with open(f'{writePath}sqRootAns.txt','w')as sqRootF:
                    sqRootF.write(str(answer))
            elif(saveRoot == 'n'):
                pass
        print('\n\n\n============RESTART============\n')

    except Exception as e:
        print('An error has occured')
        print('Error Type: ',e)
        print('\n')
    finally:
        print("Closed Successfully")
