from tkinter import *
from tkinter import messagebox
def button_1(text = '+'):
    messagebox.showerror('Результат', int(a.get()) + int(b.get()))
def button_2(text = '-'):
    messagebox.showinfo('Результат', int(a.get()) - int(b.get()))
def button_3(text = '*'):
    messagebox.showinfo('Результат', int(a .get()) * int(b.get()))
def button_4(text = '/'):
    messagebox.showinfo('Результат', int(a.get()) / int(b.get()))
root=Tk()
root.title('калькулятор')
root.geometry('1000x600')
a=Entry(root, width=10,  bg='gray', fg='white', font='consolas')
b=Entry(root, width=10,  bg='gray', fg='white', font='consolas')
a.pack()
b.pack()
Button(root, text='+', width=10, height=2, bg='cyan', command=button_1).pack()
Button(root, text='-', width=10, height=2, bg='cyan', command=button_2).pack()
Button(root, text='*', width=10, height=2, bg='cyan', command=button_3).pack()
Button(root, text='/', width=10, height=2, bg='cyan', command=button_4).pack()
root.mainloop()