from tkinter import *

root = Tk()
root.geometry('500x550')
root.title("Calculator")
root.config(bg='grey')


display_label = Label(root, width=65, height=8)
display_label.place(x=20, y=15)

btn_7 = Button(root, text='7', width=6, height=3, font=("monaco", 15, "bold"))
btn_7.place(x=20, y=120)
btn_8 = Button(root, text='8', width=6, height=3, font=("monaco", 15, "bold"))
btn_8.place(x=140, y=120)
btn_9 = Button(root, text='9', width=6, height=3, font=("monaco", 15, "bold"))
btn_9.place(x=260, y=120)
btn_plus = Button(root, text='+', width=6, height=3, font=("monaco", 15, "bold"))
btn_plus.place(x=380, y=120)

btn_4 = Button(root, text='4', width=6, height=3, font=("monaco", 15, "bold"))
btn_4.place(x=20, y=220)
btn_5 = Button(root, text='5', width=6, height=3, font=("monaco", 15, "bold"))
btn_5.place(x=140, y=220)
btn_6 = Button(root, text='6', width=6, height=3, font=("monaco", 15, "bold"))
btn_6.place(x=260, y=220)
btn_min = Button(root, text='-', width=6, height=3, font=("monaco", 15, "bold"))
btn_min.place(x=380, y=220)

btn_1 = Button(root, text='1', width=6, height=3, font=("monaco", 15, "bold"))
btn_1.place(x=20, y=320)
btn_2 = Button(root, text='2', width=6, height=3, font=("monaco", 15, "bold"))
btn_2.place(x=140, y=320)
btn_3 = Button(root, text='3', width=6, height=3, font=("monaco", 15, "bold"))
btn_3.place(x=260, y=320)
btn_dot = Button(root, text='.', width=6, height=3, font=("monaco", 15, "bold"))
btn_dot.place(x=380, y=320)

btn_mul = Button(root, text='x', width=6, height=3, font=("monaco", 15, "bold"))
btn_mul.place(x=20, y=420)
btn_0 = Button(root, text='0', width=6, height=3, font=("monaco", 15, "bold"))
btn_0.place(x=140, y=420)
btn_div = Button(root, text='/', width=6, height=3, font=("monaco", 15, "bold"))
btn_div.place(x=260, y=420)
btn_equal = Button(root, text='=', width=6, height=3, font=("monaco", 15, "bold"))
btn_equal.place(x=380, y=420)


root.mainloop()
