import sys, os
import tkinter
from time import sleep

running = True
window = tkinter.Tk()
window.title("Robo")
wDir = os.getcwd()

class Button:
    def __init__(self, text='error'):
        self.text = text
        self.obj = tkinter.Button(window, text=text, width=40)
        # print("Button created")

    def draw(self):
        self.obj.pack(padx=10, pady=10)

    def link(self, task):
        self.obj.bind("<ButtonRelease-1>", task)


buttonOCal = Button("Open Command Line Calculator")
buttonR = Button("Open Square Root Calculator")
buttonCa = Button("Open Calculator")
buttonMo = Button("Open Morse Code Translator")
buttonEnDe = Button("Open Encrypted Message Encoder/Decoder")
buttonSu = Button("Open Sudoku Generator")
buttonCl = Button("Open Random Dice")
buttonExit = Button("Exit")
buttonR.draw()
buttonCa.draw()
buttonOCal.draw()
buttonMo.draw()
buttonEnDe.draw()
buttonSu.draw()
buttonCl.draw()
buttonExit.draw()


def oldCalS(event=None):
    window.title("Starting Calculator...")
    sleep(1)
    # window.destroy()
    try:
        os.system('python program_files/oldcal.py')
    except:
        print("Cannot open application")


def CalS(event=None):
    window.title(f"Starting Calculator...{wDir}")
    sleep(1)
    try:
        os.system(f'"{wDir}/program_files/CALC.EXE"')
    except:
        print("Cannot open application")


def RootS(event=None):
    window.title("Starting Root Calculator...")
    sleep(1)
    try:
        os.system('python program_files/root.py')
    except:
        print("Cannot open application")


def Close(event=None):
    running = False
    print("Shutting down...")
    sleep(0.5)
    try:
        window.destroy()
    except:
        print("Error closing window")
    sleep(1)
    sys.exit(0)
    running = False
    while 'normal' == window.state():
        print("Error while exiting")
        sys.exit("Error while exiting")
        sleep(0.1)
        print("Error while exiting")
        window.destroy()
        os.exit(1)


def Random(event=None):
    window.title("Starting Random Number Generator...")
    sleep(1)
    try:
        os.system('python program_files/Myrandom.py')
    except:
        print("Cannot open application")


def Morse(event=None):
    window.title("Starting Morse Code Translator...")
    sleep(1)
    try:
        os.system('python program_files/morse.py')
    except:
        print("Cannot open application")


def encodeDecode(event=None):
    window.title("Starting Message Encoder/Decoder...")
    sleep(1)
    try:
        os.system('python program_files/EncodeDecode.py')
    except:
        print("Cannot open application")


def sudoku(event=None):
    window.title("Sudoku!!!")
    try:
        os.system('python program_files/sudoku.py')
    except FileNotFoundError:
        print("Sudoku program not found")
    except:
        print("Error opening Sudoku program")


buttonCa.link(CalS)
buttonR.link(RootS)
buttonExit.link(Close)
buttonCl.link(Random)
buttonMo.link(Morse)
buttonEnDe.link(encodeDecode)
buttonSu.link(sudoku)
buttonOCal.link(oldCalS)

window.mainloop()
try:
    if running:
        window.protocol("WM_CLOSE_WINDOW", Close)
except SystemExit as errorCode:
    Close()
finally:
    Close()
    sleep(0.01)
    sys.exit(errorCode)
