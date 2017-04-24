from tkinter import*

root=Tk()
root.title('Calculator')
root.geometry('800x500')

def plus(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1+x2
    v.set(s)

def minus(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1-x2
    v.set(s)

def umnog(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1*x2
    v.set(s)

def dele(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1/x2
    v.set(s)

def clear(event):
    e1.delete(0,END)
    e2.delete(0,END)
    s=''
    v.set(s)

def srt(event):
    x1=float(e1.get())
    s=x1**(1/2)
    v.set(s)

def drob(event):
    x1=float(e1.get())
    s=1/x1
    v.set(s)

def kvadrat(event):
    x1=float(e1.get())
    s=x1*x1
    v.set(s)


def kvadratn(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1**x2
    v.set(s)

def srtn(event):
    x1=float(e1.get())
    x2=float(e2.get())
    s=x1**(1/x2)
    v.set(s)

f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
f5=Frame(root)
f6=Frame(root)
f7=Frame(root)
f8=Frame(root)
f9=Frame(root)
f10=Frame(root)
f11=Frame(root)
f12=Frame(root)
f13=Frame(root)
f14=Frame(root)

t1=Label(f1,text='Введите число')
t1.pack()

e1=Entry(f1)
e1.pack()

t2=Label(f2,text='Введите второе число,n')
t2.pack()


e2=Entry(f2)
e2.pack()

btn1=Button(f3,text='Сложить',font='Arial 14')
btn1.pack(pady=5)
btn1.bind('<Button-1>',plus)

v=IntVar()

t4=Label(f6,text='Результат:',font='Arial 10')
t4.pack()

t3=Label(f5,textvariable=v,font='Arial 20')
t3.pack()

btn2=Button(f4,text='Вычесть',font='Arial 14')
btn2.pack(pady=5)
btn2.bind('<Button-1>',minus)

btn3=Button(f7,text='Умножить',font='Arial 14')
btn3.pack(pady=5)
btn3.bind('<Button-1>',umnog)

btn4=Button(f8,text='Деление',font='Arial 14')
btn4.pack(pady=5)
btn4.bind('<Button-1>',dele)

btn5=Button(f9,text='Очистка',font='Arial 14')
btn5.pack(pady=5)
btn5.bind('<Button-1>',clear)

btn6=Button(f10,text='Корень квадратный',font='Arial 14')
btn6.pack(pady=5)
btn6.bind('<Button-1>',srt)

btn7=Button(f11,text='1/n',font='Arial 14')
btn7.pack(pady=5)
btn7.bind('<Button-1>',drob)

btn8=Button(f12,text='Х^2',font='Arial 14')
btn8.pack(pady=5)
btn8.bind('<Button-1>',kvadrat)

btn9=Button(f12,text='Х^n',font='Arial 14')
btn9.pack(pady=5)
btn9.bind('<Button-1>',kvadratn)

btn10=Button(f12,text='Корень n',font='Arial 14')
btn10.pack(pady=5)
btn10.bind('<Button-1>',srtn)

f1.grid(padx=5)
f2.grid(pady=5,column=1,padx=5,row=0)
f3.grid(row=1,padx=5,pady=5)
f4.grid(row=2,padx=5,pady=5)
f5.grid(row=0,column=3,padx=5,pady=5)
f6.grid(row=0,column=2,padx=5,pady=5)
f7.grid(row=1,column=1,padx=5,pady=5)
f8.grid(row=2,column=1,padx=5,pady=5)
f9.grid(row=1,column=2,padx=5,pady=5)
f10.grid(row=3,column=0,padx=5,pady=5)
f11.grid(row=3,column=1,padx=5,pady=5)
f12.grid(row=2,column=2,padx=5,pady=5)
f13.grid(row=2,column=3,padx=5,pady=5)
f14.grid(row=3,column=3,padx=5,pady=5)

root.mainloop()
