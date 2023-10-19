from cryptography.fernet import Fernet
from time import sleep
import sys,os
makeDefault = 'n'
decode = True
uDefaultKey = 'y'
r = 'y'
writePath = os.getcwd()
writePath = writePath.replace('\\program_files', '')
print(writePath)
while True:
    try:
        x = input("Enter [d] to Decrypt, [e] to Encrypt, or [q] to quit: ")
        if(x == ''):
            decode = False
            raise Exception("You didn't enter [e] or [d]")
        if (x == 'q'):
            sys.exit(0)
        if (x == 'd'):
            decode = True
            uDefaultKey = input("Would you like to use your default key? y/n")
            if(uDefaultKey == 'n'):
                key = open(f"{writePath}/secret.key", "rb").read()
            elif(uDefaultKey == 'y'):
                 key = open(f"{writePath}/my.key", "rb").read()
            else:
                raise Exception("You didn't enter 'y' or 'n'")
            filename =input("Enter the message's file name: ")
            token = open(f'{writePath}/{filename}.encryptedmsg', 'rb').read()
        elif(x == 'e'):
            decode = False

        elif(x == 'c'):
            raise Exception("Code cracking is not currently available")
            # os.system('crack.py')
        else:
            raise Exception("You didn't enter [e] or [d]")
        if decode:
            f = Fernet(key)
            answer = f.decrypt(token)
            print("Decryption Sucessfull")
            sleep(0.1)
            answer = str(answer,'utf-8')
            answer.replace("b","")
            answer.replace("'","")
            answer.replace("'","")
            print("Decrypted Message: "+answer)
            if(not uDefaultKey):
                makeDefault = input("Would you like to make this temporary key your default key? y/n")
                if(makeDefault):
                    with open(f'{writePath}/my.key','wb') as mKeyF:
                        mKeyF.write(key)
                    sleep(0.1)
                    print("Key successfully saved as default")
                    continue

        else:
            ptoken = ''
            pkey = ''
            print("Would you like to encode this message using your default key or should a new one be generated?")
            r = input("Type 'g' to generate a new key or 'd' to use your default key")
            if (r == 'g'):
                key = Fernet.generate_key()
            elif(r == 'd'):
                key = open(f"{writePath}/my.key", "rb").read()
                sleep(0.1)
            else:
                raise Exception("You didn't enter 'g' or 'd'")
            if(key == '' or key == None):
                raise Exception("Key error. Please retry or generate new key. Default key may not exist.")
            pkey = str(key,'utf-8')
            f = Fernet(key)
            textIn = input("Enter Message: ")
            textIn = bytes(textIn,'utf-8')
            token = f.encrypt(textIn)
            #print("Encryption Successful")
            ptoken = str(token,'utf-8')
            sleep(0.1)

            print('Encoded Text: '+ptoken+'   ')
            print('Key: '+pkey)
            sleep(0.04)
            print('')
            key = bytes(key)
            sLocation = writePath
            sLocation += input("What filename should this encrypted message be saved as?")
            sLocation += '.encryptedmsg'
            file = open(sLocation,'wb')
            file.write(token)
            sleep(0.5)
            file.close()

            if(r == 'g'):
                with open(f"{writePath}/secret.key", "wb") as key_file:
                    key_file.write(key)
                makeDefault = input("Would you like to make this key your default key? y/n")
                if(makeDefault == 'n'):
                    continue
                elif(makeDefault == 'y'):
                    with open(f"{writePath}/my.key",'wb')as dKeyF:
                        dKeyF.write(key)
                    sleep(0.1)
                    print("Key sucessfully saved as default")
                    continue
                else:
                    raise Exception("You didn't enter 'n' or 'y'")

    except SystemExit:
        print("Shutting down...")
        sleep(0.1)
        sys.exit(0)
        sleep(0.1)
        raise SystemExit(0)
        break

    except Exception as e:
        print(e)
        continue
