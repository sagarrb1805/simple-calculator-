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


btn_7 = Button(root, text='7', width=6, height=3, font=("monaco", 15, "bold"), command=press_7)
btn_7.place(x=20, y=120)
btn_8 = Button(root, text='8', width=6, height=3, font=("monaco", 15, "bold"), command=press_8)
btn_8.place(x=140, y=120)
btn_9 = Button(root, text='9', width=6, height=3, font=("monaco", 15, "bold"), command=press_9)
btn_9.place(x=260, y=120)
btn_plus = Button(root, text='+', width=6, height=3, font=("monaco", 15, "bold"), command=press_plus)
btn_plus.place(x=380, y=120)


btn_4 = Button(root, text='4', width=6, height=3, font=("monaco", 15, "bold"), command=press_4)
btn_4.place(x=20, y=220)
btn_5 = Button(root, text='5', width=6, height=3, font=("monaco", 15, "bold"), command=press_5)
btn_5.place(x=140, y=220)
btn_6 = Button(root, text='6', width=6, height=3, font=("monaco", 15, "bold"), command=press_6)
btn_6.place(x=260, y=220)
btn_min = Button(root, text='-', width=6, height=3, font=("monaco", 15, "bold"), command=press_min)
btn_min.place(x=380, y=220)


btn_1 = Button(root, text='1', width=6, height=3, font=("monaco", 15, "bold"), command=press_1)
btn_1.place(x=20, y=320)
btn_2 = Button(root, text='2', width=6, height=3, font=("monaco", 15, "bold"), command=press_2)
btn_2.place(x=140, y=320)
btn_3 = Button(root, text='3', width=6, height=3, font=("monaco", 15, "bold"), command=press_3)
btn_3.place(x=260, y=320)
btn_dot = Button(root, text='.', width=6, height=3, font=("monaco", 15, "bold"), command=press_dot)
btn_dot.place(x=380, y=320)


btn_mul = Button(root, text='x', width=6, height=3, font=("monaco", 15, "bold"), command=press_mul)
btn_mul.place(x=20, y=420)
btn_0 = Button(root, text='0', width=6, height=3, font=("monaco", 15, "bold"), command=press_0)
btn_0.place(x=140, y=420)
btn_div = Button(root, text='/', width=6, height=3, font=("monaco", 15, "bold"), command=press_div)
btn_div.place(x=260, y=420)
btn_equal = Button(root, text='=', width=6, height=3, font=("monaco", 15, "bold"), command=press_equal)
btn_equal.place(x=380, y=420)

btn_clear = Button(root, text='C', width=42, height=2, font=("monaco", 15, "bold"), command=press_clear)
btn_clear.place(x=20, y=493)


root.mainloop()
