import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title('convert')
style = ttk.Style()
style.theme_names()
style.theme_use('clam')


def convert():
    kg = float(e1.get())
    t2.configure(text = str(kg * 1000) + ' Grams')
    t3.configure(text = str(kg * 2.20462) + ' Pounds')
    t4.configure(text = str(kg * 35.274) + ' Ounces')
 


e1 = ttk.Entry(window, width=20)
b1 = ttk.Button(window, text='CONVERT', command=convert)

t1 = ttk.Label(window, text='Input kg', width=15)
t2 = ttk.Label(window, text='Grams        ')
t3 = ttk.Label(window, text='Pounds        ')
t4 = ttk.Label(window, text='Ounces        ')

filler = tkinter.Label(window, text=' ', width = 5)

t1.grid(row=0, column=2)
t2.grid(row=0, column=3)
t3.grid(row=1, column=3)
t4.grid(row=2, column=3)
e1.grid(row=1, column=2)
b1.grid(row=2, column=2)

filler.grid(row=3, column=0)







window.mainloop()