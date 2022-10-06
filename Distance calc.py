import tkinter
window = tkinter.Tk()
window.title('convert')


def ToMiles():
    kilo = float(e1.get())
    answer = kilo / 1.60934
    t1.configure(text = str(answer) + ' miles')
    
def ToKilo():
    miles = float(e1.get())
    answer = miles * 1.60934
    t1.configure(text = str(answer) + ' kilometers')

e1 = tkinter.Entry(window, width=20)
b1 = tkinter.Button(window, text='CONVERT TO MILES', bg='orange', command=ToMiles)
b2 = tkinter.Button(window, text='CONVERT TO KILOMETER', bg='orange', command=ToKilo)
t1 = tkinter.Label(window, text=' ', width=20)
t2 = tkinter.Label(window, text='Input either km or mile value', width=25)

t2.grid(row=0, column=0)
e1.grid(row=1, column=0)
b1.grid(row=1, column=1)
b2.grid(row=2, column=1)
t1.grid(row=2, column=0)








window.mainloop()
