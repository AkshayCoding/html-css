from tkinter import *

val =""
A = 0
operator =""


def btn_1_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_2_isclicked():
        global val
        val = val + "8"
        data.set(val)


def btn_3_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator ="/"
    val = val + "/"
    data.set(val)


def btn_5_isclicked():
    global val
    val = val + "4"
    data.set(val)


def btn_6_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_mult_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator ="*"
    val = val + "*"
    data.set(val)


def btn_9_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_10_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_11_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_min_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator ="-"
    val = val + "-"
    data.set(val)

def btn_13_isclicked():
    global val
    val = val + "0"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator =="+":
        x=int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val= str(C)
    elif operator =="-":
        x = int((val2.split("-")[1]))
        C = A  - x
        data.set(C)
        val = str(C)
    elif operator =="*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)

    elif operator =="/":
        x = int((val2.split("/")[1]))
        C = A  / x
        data.set(C)
        val = str(C)

def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator ="+"
    val = val + "+"
    data.set(val)
def dot (self):
root = Tk()
root.geometry("444x500")
root.title("Calculator")

data=StringVar()
lbl = Label(root,text = "Label" , textvariable=data, background="#ffffff" , fg ="#000000", font="Verdana 22", anchor=SE)
lbl.pack(expand = True , fill="both" , )
root.wm_iconbitmap("pyicon.ico")
root.resizable(0,0)


btn2row = Frame(root)
btn2row.pack(expand = True , fill="both")

btn3row = Frame(root)
btn3row.pack(expand = True , fill="both")

btn4row = Frame(root)
btn4row.pack(expand = True , fill="both")

btn5row = Frame(root)
btn5row.pack(expand = True , fill="both")

btn1 = Button(btn2row , text="7", font="Verdana 22" , command = btn_1_isclicked , relief=GROOVE)
btn1.pack( side= LEFT ,  expand = True , fill="both" ,)

btn2 = Button(btn2row , text="8", font="Verdana 22", command = btn_2_isclicked, relief=GROOVE)
btn2.pack( side= LEFT , expand = True , fill="both" ,)

btn3 = Button(btn2row , text="9", font="Verdana 22" , command = btn_3_isclicked,relief=GROOVE)
btn3.pack(side= LEFT , expand = True , fill="both"  ,)

btn4 = Button(btn2row , text="/" , font="Verdana 22", command = btn_div_clicked , relief=GROOVE)
btn4.pack(side= LEFT ,expand = True , fill ="both" , )

btn5 = Button(btn3row , text="4", font="Verdana 22", command = btn_5_isclicked , relief=GROOVE)
btn5.pack(side= LEFT , expand = True , fill="both")

btn6 = Button(btn3row , text="5", font="Verdana 22", command = btn_6_isclicked ,relief=GROOVE)
btn6.pack(side= LEFT , expand = True , fill="both")

btn7 = Button(btn3row , text="6", font="Verdana 22", command = btn_7_isclicked,relief=GROOVE)
btn7.pack(side= LEFT , expand = True , fill="both")

btn8 = Button(btn3row , text="*" , font="Verdana 22" , command =btn_mult_clicked,relief=GROOVE)
btn8.pack(side= LEFT ,expand = True , fill ="both")

btn9 = Button(btn4row , text="1", font="Verdana 22" , command =btn_9_isclicked,relief=GROOVE)
btn9.pack(side= LEFT , expand = True , fill="both")

btn10 = Button(btn4row , text="2", font="Verdana 22" , command =btn_10_isclicked,relief=GROOVE)
btn10.pack(side= LEFT , expand = True , fill="both")

btn11 = Button(btn4row , text="3", font="Verdana 22" , command=btn_11_isclicked,relief=GROOVE)
btn11.pack(side= LEFT , expand = True , fill="both")

btn12 = Button(btn4row , text="-" , font="Verdana 22" , command=btn_min_clicked,relief=GROOVE)
btn12.pack(side= LEFT ,expand = True , fill ="both")


btn13 = Button(btn5row , text="0", font="Verdana 22", command=btn_13_isclicked,relief=GROOVE)
btn13.pack(side= LEFT , expand = True , fill="both")

btn14 = Button(btn5row , text="C", font="Verdana 22" , command=c_pressed,relief=GROOVE)
btn14.pack(side= LEFT , expand = True , fill="both" ,)

btn15 = Button(btn5row , text="=", font="Verdana 22 " , command=result,relief=GROOVE)
btn15.pack(side= LEFT , expand = True , fill="both")

btn16 = Button(btn5row , text="+" , font="Verdana" , command=btn_plus_clicked,relief=GROOVE)
btn16.pack(side= LEFT ,expand = True , fill ="both")

btn17 = Button(btn5row , text="." , font="Verdana" , relief=GROOVE)
btn17.pack(side= LEFT ,expand = True , fill ="both")


root.mainloop()