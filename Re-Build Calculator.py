from tkinter import *
from tkinter.messagebox import *
#some variables
operator=""
font=("Verdana" , 22 , "bold")
#functions
def all_clear():
    textField.delete( 0 ,END)

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)
    if text == 'x':
        ex=textField.insert( END ,'*')
        return ;

    if text == '=':
        try:
            ex = textField.get()
            anser = eval(ex)
            textField.delete(0, END)
            textField.insert(0, anser)
        except ZeroDivisionError   as e:
            print("Error")
            showerror("Divison", "Can't Divide With Zero")
            textField.delete(0, END)
            return

        except SyntaxError as e:
            print("Error")
            showerror("Syntax Error", "Invalid Syntax")
            textField.delete(0, END)
            return


    textField.insert(END,text)

#Creating a Window

window = Tk()
#Sets The Title
window.title("Calculator")
#Sets The Icon
window.wm_iconbitmap("pyicon.ico")


#Sets The Height And Width
window.geometry("600x410")
window.resizable(50,0)
textField = Entry (window,font=font,justify=CENTER)
textField.pack(side=TOP,fill=X)

#Buttons
buttonFrame = Frame(window)
buttonFrame.pack()

#Adding Buttons
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp) , font=font,width=8 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
        btn.grid(row=i , column=j , padx=3 , pady=3)
        temp = temp + 1
        btn.bind('<Button-1>' , click_btn_function)
#zerobtn
zeroBtn = Button(buttonFrame,text=0 , font=font, width=8 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
zeroBtn.grid(row=3, column=0, padx=3 , pady=3)

dotBtn = Button(buttonFrame,text=".", font=font, width=8 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
dotBtn.grid(row=3, column=1, padx=3 , pady=3)

#equal btn
equalBtn = Button(buttonFrame,text="=", font=font, width=8 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
equalBtn.grid(row=3, column=2, padx=3 , pady=3)

PlusBtn = Button(buttonFrame,text="+", font=font, width=3 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
PlusBtn.grid(row=0, column=4, padx=3 , pady=3)

minusBtn = Button(buttonFrame,text="-", font=font, width=3 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
minusBtn.grid(row=1, column=4, padx=3 , pady=3)

MultBtn = Button(buttonFrame,text="x", font=font, width=3 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
MultBtn.grid(row=2, column=4, padx=3 , pady=3)

divideBtn = Button(buttonFrame,text="/", font=font, width=3 , relief="ridge" ,activebackground="orange" ,activeforeground="white")
divideBtn.grid(row=3, column=4, padx=3 , pady=3)

ClearBtn = Button(buttonFrame,text="AC", font=font, width=3 , relief="ridge" ,activebackground="orange" ,activeforeground="white", command=all_clear)
ClearBtn.grid(row=4, column=1, padx=3 , pady=3)



#binding button
equalBtn.bind('<Button-1>' , click_btn_function)
PlusBtn.bind('<Button-1>' , click_btn_function)
minusBtn.bind('<Button-1>' , click_btn_function)
divideBtn.bind('<Button-1>' , click_btn_function)
MultBtn.bind('<Button-1>' , click_btn_function)
dotBtn.bind('<Button-1>' , click_btn_function)
zeroBtn.bind('<Button-1>' , click_btn_function)

window.mainloop()