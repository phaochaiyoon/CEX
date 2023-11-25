import tkinter
from math import *

count = 0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

window=tkinter.Tk()
window.title("sj")
window.geometry("640x400+100+100")
window.resizable(False,False)


label = tkinter.Label(window, text="CEX.")
label.pack()


button = tkinter.Button(window,overrelief="solid",width=15,command=countUP,repeatdelay=1000,repeatinterval=100)
button.pack()

def calc(event):
    label4.config(text = "결과 = "+str(eval(entry.get())))

entry = tkiner.Entry(window)
entry.bind("<Return>",calc)
entry.pcak()




window.mainloop()
