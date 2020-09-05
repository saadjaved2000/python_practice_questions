import tkinter as tk
window=tk.Tk()
window.title("Calculator")

def btn_click(items):
    global expression
    expression = expression + str(items)
    input_text.set(expression)

expression=""
input_text=tk.StringVar()

frame_a=tk.Frame()
entry=tk.Entry(master=frame_a,bg="black",fg="white",width=21,font=('arial',20), justify="right",textvariable=input_text)
entry.pack()
frame_a.pack()

frame_b=tk.Frame()
number1=tk.Button(master=frame_b,text="1",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(1))
number1.grid(row=4, column=0)
number2=tk.Button(master=frame_b,text="2",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(2))
number2.grid(row=4, column=1)
number3=tk.Button(master=frame_b,text="3",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(3))
number3.grid(row=4, column=2)
number4=tk.Button(master=frame_b,text="4",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(4))
number4.grid(row=3, column=0)
number5=tk.Button(master=frame_b,text="5",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(5))
number5.grid(row=3, column=1)
number6=tk.Button(master=frame_b,text="6",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(6))
number6.grid(row=3, column=2)
number7=tk.Button(master=frame_b,text="7",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(7))
number7.grid(row=2, column=0)
number8=tk.Button(master=frame_b,text="8",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(8))
number8.grid(row=2, column=1)
number9=tk.Button(master=frame_b,text="9",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(9))
number9.grid(row=2, column=2)
number0=tk.Button(master=frame_b,text="0",bg="grey",fg="black",height=5,width=10,command=lambda:btn_click(0))
number0.grid(row=5, column=0)
add=tk.Button(master=frame_b,text="+",bg="blue",fg="white",height=5,width=10,command=lambda:btn_click("+"))
add.grid(row=3, column=3)
substract=tk.Button(master=frame_b,text="-",bg="blue",fg="white",height=5,width=10,command=lambda:btn_click("-"))
substract.grid(row=4, column=3)

def btn_equal():
    try:
        global expression
        result= str(eval(expression))
        input_text.set(result)
        expression=""
    except:
        print("you did not use any of the operations, try again")

equal=tk.Button(master=frame_b,text="=",bg="blue",fg="white",height=5,width=10,command=lambda:btn_equal())
equal.grid(row=5, column=3)


def btn_clear():
    global expression
    expression= ""
    input_text.set(expression)

clear=tk.Button(master=frame_b,text="AC",bg="yellow",fg="green",height=5,width=10,command=lambda:btn_clear())
clear.grid(row=1, column=0)




delete=tk.Button(master=frame_b,text="Del",bg="yellow",fg="green",height=5,width=10)
delete.grid(row=1, column=1)
multiply=tk.Button(master=frame_b,text="x",bg="blue",fg="white",height=5,width=10)
multiply.grid(row=1, column=3)
divide=tk.Button(master=frame_b,text="/",bg="blue",fg="white",height=5,width=10)
divide.grid(row=2, column=3)
power=tk.Button(master=frame_b,text="^",bg="blue",fg="white",height=5,width=10)
power.grid(row=1, column=2)
ans=tk.Button(master=frame_b,text="ans",bg="blue",fg="white",height=5,width=10)
ans.grid(row=5, column=2)
decimal=tk.Button(master=frame_b,text=".",bg="grey",fg="black",height=5,width=10)
decimal.grid(row=5, column=1)
frame_b.pack()









"""l=tk.Label(text='Hello, welcome to calculator',foreground='red', background='blue',height=5, width=25)
l.pack()

b=tk.Button(text='+', width= 25, height=2, foreground='red',background='blue')
b.pack()

e=tk.Entry()
e.pack()

frame_a=tk.Frame()
label_a=tk.Label(master=frame_a,text='Hello 123')
label_a.pack()
frame_a.pack()

effect={"hello":tk.FLAT,"Hi":tk.SUNKEN,"GOOD MORNING":tk.RAISED,"AMIGO":tk.GROOVE,"BYE":tk.RIDGE}

for a,b in effect.items():
    frame=tk.Frame(master=window,relief=b,borderwidth=10)
    frame.pack(side=tk.TOP)
    label=tk.Label(master=frame,text=a)
    label.pack()"""
