import os
print("Welcome to the Calculator!")
#print(os.getcwd())
#os.system("pause")
os.system(f'"{os.getcwd()}/program_files/calc.exe"')
os.system("pause")


'''
import sys
import tkinter as tk
from time import sleep
master = tk.Tk()
master.title("Calculator")
num = None
num2 = None
oper = None
answer = None
TextD = None
Text = tk.StringVar()
def close():
    print("Shutting down...")
    sleep(0.08)
    master.destroy()
    sleep(0.02)
    sys.exit(0)
def cal():
    global num
    global num2
    global oper
    global answer
    if (oper == "^"):
        answer = num ** num2
    elif (oper == "/"):
        answer = num // num2
    elif (oper == "*"):
        answer = num * num2
    elif (oper == "+"):
        answer = num + num2
    elif (oper == "-"):
        answer = num - num2
    else:
        print ("ERROR")
        num = Infinity
        num2 = Infinity
        answer = "ERROR"

def show_entry_fields():
    global num
    global num2
    global oper
    global answer
    global Text
    num = numE1.get()
    num2 = numE2.get()
    oper = operE.get()
    num = float(num)
    num2 = float(num2)
    cal()
    answer = str(answer)
    Text.set("Answer: " + answer)
    master.clipboard_clear()
    master.clipboard_append(str(answer))

tk.Label(master, text="Number1").grid(row=0)
tk.Label(master, text="Number2").grid(row=2)
tk.Label(master, text="Operation").grid(row=1)
TextD = tk.Label(master, textvariable=Text)
TextD.grid(row = 4, column = 1)
numE1 = tk.Entry(master)
numE2 = tk.Entry(master)
operE = tk.Entry(master)
numE1.grid(row=0, column=1)
numE2.grid(row=2, column=1)
operE.grid(row=1, column=1)
tk.Button(master, text='Quit', command=close).grid(row=3, column=0,  sticky=tk.W, pady=4)   
tk.Button(master, text='Calculate', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.mainloop()
print("Balony!")
'''