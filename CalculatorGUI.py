from tkinter import *
obj=Tk()

obj.title("Calculator")

obj.geometry("300x450+500+100")

obj.config(background="black")

l1=Label(text="CALCULATOR",font=('chiller',34,'bold'),bg="red")
l1.place(x=0,y=0)
a=" "




def press(num):
    global a

    a=a + str(num)

    equation.set(a)


def equal():
     try:
         global a

         total= str(eval(a))
         equation.set(total)
         a=""
     except:
         equation.set(" Syntax Error ")
         a=""




def clear():
    global a
    a=""
    equation.set("")

def square():
    v1=e1.get()
    i=float(v1)
    sq=i*i
    equation.set(sq)

def sqrt():
    v1 = e1.get()
    i = float(v1)
    sq = i**(1/2)
    equation.set(sq)

def reverse():
    v1 = e1.get()
    i = float(v1)
    sq = 1/i
    equation.set(sq)

def back():
    global a
    v1=e1.get()
    c=len(v1)
    e1.delete(c-1,c)
    a=e1.get()
    equation.set(a)

def fact():
    fac=1
    v1 = e1.get()
    i = int(v1)
    for j in range(1,i+1):
        fac=fac*j

    equation.set(fac)

def power():
    v1 = e1.get()
    i = float(v1)
    sq = 10**i
    equation.set(sq)




equation=StringVar()

e1= Entry(obj,font=('chiller',32,'bold'),textvariable=equation,bg="red")
e1.place(x=0,y=150)

equation.set("Enter your expression")

plus=Button(text="+",width=7,height=2,font=50,command=lambda: press('+'),fg='light green',bg='black')
plus.place(x=165,y=300)

minus=Button(text="-",width=7,height=2,font=50,command=lambda :press('-'),fg='light green',bg='black')
minus.place(x=230,y=300)

multiple=Button(text="*",width=7,height=2,font=50,command=lambda :press('*'),fg='light green',bg='black')
multiple.place(x=165,y=350)

divide=Button(text="/",width=7,height=2,font=50,command=lambda :press('/'),fg='light green',bg='black')
divide.place(x=230,y=350)

equal=Button(text="=",width=7,height=2,font=50,command=equal,fg='light green',bg='black')
equal.place(x=230,y=400)

dot=Button(text=".",width=7,height=2,font=50,command=lambda: press('.'),fg='light green',bg='black')
dot.place(x=165,y=400)

button0=Button(text="0",width=12,height=2,font=50,command=lambda: press('0'),fg='light green',bg='black')
button0.place(x=0,y=400)

button_clear=Button(text="C",width=7,height=2,font=50,command=clear,fg='light green',bg='black')
button_clear.place(x=165,y=250)

button9=Button(text="9",width=5,height=2,font=50,command=lambda: press('9'),fg='light green',bg='black')
button9.place(x=110,y=250)

button8=Button(text="8",width=6,height=2,font=50,command=lambda: press('8'),fg='light green',bg='black')
button8.place(x=50,y=250)

button7=Button(text="7",width=5,height=2,font=50,command=lambda: press('7'),fg='light green',bg='black')
button7.place(x=0,y=250)

button6=Button(text="6",width=5,height=2,font=50,command=lambda: press('6'),fg='light green',bg='black')
button6.place(x=110,y=300)

button5=Button(text="5",width=6,height=2,font=50,command=lambda: press('5'),fg='light green',bg='black')
button5.place(x=50,y=300)

button4=Button(text="4",width=5,height=2,font=50,command=lambda: press('4'),fg='light green',bg='black')
button4.place(x=0,y=300)

button3=Button(text="3",width=5,height=2,font=50,command=lambda: press('3'),fg='light green',bg='black')
button3.place(x=110,y=350)

button2=Button(text="2",width=6,height=2,font=50, command=lambda: press('2'),fg='light green',bg='black')
button2.place(x=50,y=350)

button1=Button(text="1",width=5,height=2,font=50,command=lambda: press('1'),fg='light green',bg='black')
button1.place(x=0,y=350)

buttonsqrt=Button(text="Sqrt",width=6,height=2,font=50,command=sqrt,fg='light green',bg='black')
buttonsqrt.place(x=110,y=400)

button_back=Button(text="<-",width=7,height=2,font=50,command=back,fg='light green',bg='black')
button_back.place(x=230,y=250)

button_plus_minus=Button(text="%",width=6,height=2,font=50,command=lambda :press('%'),fg='light green',bg='black')
button_plus_minus.place(x=0,y=200)

button_square=Button(text="X^2",width=6,height=2,font=50,command=square,fg='light green',bg='black')
button_square.place(x=60,y=200)

button=Button(text="1/X",width=6,height=2,font=50,command=reverse,fg='light green',bg='black')
button.place(x=120,y=200)

button_fact=Button(text="N!",width=6,height=2,font=50,command=fact,fg='light green',bg='black')
button_fact.place(x=180,y=200)

button_10=Button(text="10^X",width=6,height=2,font=50,command=power,fg='light green',bg='black')
button_10.place(x=240,y=200)



obj.mainloop()