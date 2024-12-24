from tkinter import *

window = Tk()
window.geometry('1000x1000')

ent = Entry(window, bg = 'light green', fg = 'red', bd = 10)
ent.grid(row= 1, column=1, columnspan=4)

def btn_click(number):
    ent.insert(END, str(number))

def btn_c():
    ent.delete(0, END)

def btn_result():
    res = ent.get() 
    result = eval(res)
    ent.delete(0, END)
    ent.insert(0, result)


btn = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 1, command=lambda:btn_click(1))
btn.grid(row = 2, column = 1)

btn2 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 2, command=lambda:btn_click(2))
btn2.grid(row = 2, column = 2)

btn3 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 3, command=lambda:btn_click(3))
btn3.grid(row = 2, column = 3)

btn4 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 4, command=lambda:btn_click(4))
btn4.grid(row = 3, column = 1)

btnn = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = '+',command = lambda:btn_click('+'))
btnn.grid(row = 2, column = 4)

btn5 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 5, command=lambda:btn_click(5))
btn5.grid(row = 3, column = 2)

btn6 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 6, command=lambda:btn_click(6))
btn6.grid(row = 3, column = 3)

btnw = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = '*',command = lambda:btn_click('*'))
btnw.grid(row = 3, column = 4)

btn7 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 7, command=lambda:btn_click(7))
btn7.grid(row = 4, column = 1)

btn8 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 8, command=lambda:btn_click(8))
btn8.grid(row = 4, column = 2)

btnd = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = '/',command = lambda:btn_click('/'))
btnd.grid(row = 4, column = 4)

btn9 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 9, command=lambda:btn_click(9))
btn9.grid(row = 4, column = 3)

btn0 = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 0, command=lambda:btn_click(0))
btn0.grid(row = 5, column = 1)

btnc = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = 'c', command = btn_c)
btnc.grid(row = 5, column = 2)

btnq = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = '=',command = btn_result)
btnq.grid(row = 5, column = 3)

btnj = Button(window, bg = 'pink', fg = 'black', bd = 10 , text = '-',command = lambda:btn_click('-'))
btnj.grid(row = 5, column = 4)

window.mainloop()