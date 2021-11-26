from tkinter import *
from math import *


def command(arg):
    eq = {'v': '/', 'm': '*', 'a': '+', 's': '-', 'e': '=', 'o': '(', 'l': ')', 'pi': 'π',
          'p': '.'}  # map name buttons to file name
    if arg in eq:
        arg = eq[arg]

    def helper():
        if arg == '=':
            try:
                result = eval(display.get())
                display.delete(0, END)
                display.insert(0, result)
            except ZeroDivisionError:
                display.delete(0, END)
                display.insert('end', 'Divide by zero is not possible')
            except (SyntaxError, TypeError):
                display.delete(0, END)
                display.insert('end', 'Press C then insert correct form')
        elif arg == 'C':
            display.delete(0, END)
        elif arg == 'D':
            display.delete(len(display.get()) - 1, END)
        else:
            display.insert(END, arg)

    return helper


π = pi
root = Tk()

layout = [
    ['C', 'D', 'o', 'l', 'sin'],
    ['7', '8', '9', 'v', 'cos'],
    ['4', '5', '6', 's', 'tan'],
    ['1', '2', '3', 'm', 'log'],
    ['p', '0', 'e', 'a', 'pi']
]

config = {'bd': -20}
display = Entry()
display.grid(row=0, column=0, columnspan=4, sticky=W + E)
images = [[PhotoImage(file=item + '.gif') for j, item in enumerate(row)] for i, row in enumerate(layout)]
# images = []
# for i, row in enumerate(layout):
#     for j, item in enumerate(row):
#         images.append(PhotoImage(file = item + '.gif'))

for i, row in enumerate(layout):
    for j, item in enumerate(row):
        Button(text=item, command=command(item), image=images[i][j], **config).grid(row=i + 1, column=j)

root.mainloop()
