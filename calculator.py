import tkinter
from tkinter import *
window = Tk()
window.geometry("312x324")
window.title("Calculator")
photo = PhotoImage(file = "C:/Users/gaura/Downloads/ios-calculator-4.png")
window.iconphoto(False, photo)
exp = " "
text = tkinter.StringVar()
def press(num):
    global exp
    exp +=str(num)
    text.set(exp)
def clear():
    global exp
    exp = ""
    text.set(exp)
def equal():
    global exp
    total = str(eval(exp))
    text.set(total)
t1 = Entry(window,justify=RIGHT , textvariable=text)
t1.grid(columnspan=3,sticky="nsew")

bdot = Button(window, text=".", bg="black" , fg="white" , height=2, width=11 ,font=("ArialBold",12) , command=lambda:press("."))
b0 = Button(window, text="0" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("0"))
b1 = Button(window, text="1" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("1"))
b2 = Button(window, text="2" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("2"))
b3 = Button(window, text="3" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("3"))
b4 = Button(window, text="4" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("4"))
b5 = Button(window, text="5" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("5"))
b6 = Button(window, text="6" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("6"))
b7 = Button(window, text="7" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("7"))
b8 = Button(window, text="8" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("8"))
b9 = Button(window, text="9" , bg="black" , fg="white" , height=2, width=10 ,font=("ArialBold",12), command=lambda:press("9"))
ba = Button(window, text="+" , bg="black" , fg="white" , height=2, width=11 ,font=("ArialBold",12), command=lambda:press("+"))
bs = Button(window, text="-" , bg="black" , fg="white" , height=2, width=11 ,font=("ArialBold",12), command=lambda:press("-"))
bm = Button(window, text="*" , bg="black" , fg="white" , height=2, width=11 ,font=("ArialBold",12), command=lambda:press("*"))
bd = Button(window, text="/" , bg="black" , fg="white" , height=2, width=11,font=("ArialBold",12), command=lambda:press("/"))
be = Button(window, text="=" , bg="brown" , fg="white" , height=2, width=11 ,font=("ArialBold",12), command=equal)
bp = Button(window, text="%" , bg="black" , fg="white" , height=2, width=10,font=("ArialBold",12), command=lambda:press("."))
bc = Button(window, text="C" , bg="black" , fg="white" , height=2, width=10,font=("ArialBold",12), command=clear)

bdot.grid(row=6,column=2)
b0.grid(row=6,column=0)
b1.grid(row=6,column=1)
b2.grid(row=5,column=0)
b3.grid(row=5,column=1)
b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=3,column=0)
b7.grid(row=3,column=1)
b8.grid(row=2,column=0)
b9.grid(row=2,column=1)
ba.grid(row=3,column=2)
bs.grid(row=5,column=2)
bm.grid(row=4,column=2)
bd.grid(row=2,column=2)
be.grid(row=1,column=2)
bc.grid(row=1,column=1)
bp.grid(row=1,column=0)
window.mainloop()
