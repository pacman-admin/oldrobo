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
import tkinter
from time import sleep
running = True
window = tkinter.Tk()
window.title("Robo")
wDir = os.getcwd()
class Button:
    def __init__(self, text='error'):
        self.text = text
        self.obj = tkinter.Button(window,text=text, width=40)
        #print("Button created")
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
        os.system('python3 program_files/oldcal.py')
    except:
        print("Cannot open application")

def CalS(event=None):
    window.title("Starting Calculator...{wDir}")
    sleep(1)
    try:
        os.system('pause')
    except:
        print("Cannot open application")

def RootS(event=None):
    window.title("Starting Root Calculator...")
    sleep(1)
    try:
        os.system('python3 program_files/root.py')
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
        os.system('python3 program_files/Myrandom.py')
    except:
        print("Cannot open application")

def Morse(event=None):
    window.title("Starting Morse Code Translator...")
    sleep(1)
    try:
        os.system('python3 program_files/morse.py')
    except:
        print("Cannot open application")

def EnDecode(event=None):
    window.title("Starting Message Encoder/Decoder...")
    sleep(1)
    try:
        os.system('python3 program_files/EncodeDecode.py')
    except:
        print("Cannot open application")

def sudoku(event=None):
    window.title("Sudoku!!!")
    try:
        os.system('python3 program_files/sudoku.py')
    except FileNotFoundError:
        print("Sudoku program not found")
    except:
        print("Error opening Sudoku program")

buttonCa.link(CalS)
buttonR.link(RootS)
buttonExit.link(Close)
buttonCl.link(Random)
buttonMo.link(Morse)
buttonEnDe.link(EnDecode)
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
