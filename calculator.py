from tkinter import *

root = Tk()
root.geometry('500x570')
root.title("Calculator")
root.config(bg='grey')

display_label = Label(root, width=45, height=4, font=("monaco", 15, "bold"))  # width=65, height=8
display_label.place(x=20, y=15)

display_val = ''


def press_7():
    global display_val
    display_val += '7'
    display_label.config(text=display_val, anchor='e')


def press_8():
    global display_val
    display_val += '8'
    display_label.config(text=display_val, anchor='e')


def press_9():
    global display_val
    display_val += '9'
    display_label.config(text=display_val, anchor='e')


def press_plus():
    global display_val
    display_val += '+'
    display_label.config(text=display_val, anchor='e')


def press_4():
    global display_val
    display_val += '4'
    display_label.config(text=display_val, anchor='e')


def press_5():
    global display_val
    display_val += '5'
    display_label.config(text=display_val, anchor='e')


def press_6():
    global display_val
    display_val += '6'
    display_label.config(text=display_val, anchor='e')


def press_min():
    global display_val
    display_val += '-'
    display_label.config(text=display_val, anchor='e')


def press_1():
    global display_val
    display_val += '1'
    display_label.config(text=display_val, anchor='e')


def press_2():
    global display_val
    display_val += '2'
    display_label.config(text=display_val, anchor='e')


def press_3():
    global display_val
    display_val += '3'
    display_label.config(text=display_val, anchor='e')


def press_dot():
    global display_val
    display_val += '.'
    display_label.config(text=display_val, anchor='e')


def press_mul():
    global display_val
    display_val += '*'
    display_label.config(text=display_val, anchor='e')


def press_0():
    global display_val
    display_val += '0'
    display_label.config(text=display_val, anchor='e')


def press_div():
    global display_val
    display_val += '/'
    display_label.config(text=display_val, anchor='e')


def press_equal():
    global display_val
    try:
        result = eval(display_val)
        display_val = str(result)
        display_label.config(text=result, anchor='e')
    except Exception as e:
        display_label.config(text=e, anchor='e')


def press_clear():
    global display_val
    display_val = ''
    display_label.config(text=display_val, anchor='e')


class ButtonsCreate:
    def __init__(self, x, y, text, command, width=6, height=3):
        Button(root, text=text, width=width, height=height, font=('monaco', 15, 'bold'), command=command).place(x=x, y=y)


btn_7 = ButtonsCreate(20, 120, '7', press_7)

btn_8 = ButtonsCreate(140, 120, '8', press_8)

btn_9 = ButtonsCreate(260, 120, '9', press_9)

btn_plus = ButtonsCreate(380, 120, '+', press_plus)

btn_4 = ButtonsCreate(20, 220, '4', press_4)

btn_5 = ButtonsCreate(140, 220, '5', press_5)

btn_6 = ButtonsCreate(260, 220, '6', press_6)

btn_min = ButtonsCreate(380, 220, '-', press_min)

btn_1 = ButtonsCreate(20, 320, '1', press_1)

btn_2 = ButtonsCreate(140, 320, '2', press_2)

btn_3 = ButtonsCreate(260, 320, '3', press_3)

btn_dot = ButtonsCreate(380, 320, '.', press_dot)

btn_mul = ButtonsCreate(20, 420, 'x', press_mul)

btn_0 = ButtonsCreate(140, 420, '0', press_0)

btn_div = ButtonsCreate(260, 420, '/', press_div)

btn_equal = ButtonsCreate(380, 420, '=', press_equal)

btn_clear = ButtonsCreate(20, 493, 'C', press_clear, width=42, height=2)


root.mainloop()
