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

f1=Frame(root)
f2=Frame(root)
f3=Frame(root)
f4=Frame(root)
f5=Frame(root)
f6=Frame(root)
f7=Frame(root)
f8=Frame(root)
f9=Frame(root)

t1=Label(f1,text='Введите число')
t1.pack()

e1=Entry(f1)
e1.pack()

t2=Label(f2,text='Введите второе число')
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

f1.grid(padx=5)
f2.grid(pady=5,column=1,padx=5,row=0)
f3.grid(row=1,padx=5,pady=5)
f4.grid(row=2,padx=5,pady=5)
f5.grid(row=0,column=3,padx=5,pady=5)
f6.grid(row=0,column=2,padx=5,pady=5)
f7.grid(row=1,column=1,padx=5,pady=5)
f8.grid(row=2,column=1,padx=5,pady=5)
f9.grid(row=1,column=2,padx=5,pady=5)

root.mainloop()
