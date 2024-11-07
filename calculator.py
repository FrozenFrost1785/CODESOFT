from tkinter import *
import math

def get_input(digit):
    current=input_label['text']
    new=current+str(digit)
    input_label.config(text=new)

def clear():
    input_label.config(text='')

def operation(op):
    global f_no,operator
    f_no=float(input_label['text'])
    operator=op
    input_label.config(text='')

def result():
    global f_no,operator,s_no
    try:
        if(operator=='+'):
            s_no=float(input_label['text'])
            input_label.config(text=str(f_no+s_no))
        elif(operator=='-'):
            s_no=float(input_label['text'])
            input_label.config(text=str(f_no-s_no))
        elif(operator=='*'):
            s_no=float(input_label['text'])
            input_label.config(text=str(f_no*s_no))
        elif(operator=='**'):
            s_no=float(input_label['text'])
            input_label.config(text=str(f_no**s_no))
        elif(operator=='root'):
            input_label.config(text=str(math.sqrt(f_no)))
        elif(operator=='%'):
            s_no=float(input_label['text'])
            input_label.config(text=str((f_no*100)/s_no))
        else:
            s_no=float(input_label['text'])
            if(s_no==0):
                input_label.config(text='Error')
            else:
                input_label.config(text=str(round(f_no/s_no,8)))
    except ValueError:
        input_label.config(text='Error')
    except Exception:
        input_label.config(text=str(Exception))


root=Tk()
root.title('Calculator')
root.geometry('430x385')
root.resizable(0,0)
root.configure(background='black')

input_label=Label(root,text='',bg='black',fg='white')
input_label.grid(row=0,column=0,columnspan=5,pady=(20,10),sticky='e')
input_label.config(font=('arial',30,'bold'))


buttons=[   ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('%', 4, 0), ('0', 4, 1), ('.', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('**', 5, 1), ('root', 5, 2), ('=', 5, 3)]


for (text, row, column) in buttons:
    if text == '=':
        button = Button(root, text=text, bg='#00a65a', fg='white', width=9, height=2, command=result)
        button.grid(row=row, column=column)
        button.config(font=('arial', 14))
    elif text in ('+', '-', '*', '/','%','**','root'):
        button = Button(root, text=text, bg='#f9a603', fg='white', width=9, height=2, command=lambda text=text: operation(text))
        button.grid(row=row, column=column)
        button.config(font=('arial', 14))
    elif text == 'C':
        button_clear = Button(root, text=text, bg='#D30000', fg='white', width=9, height=2, command=clear)
        button_clear.grid(row=row, column=column)
        button_clear.config(font=('arial', 14))
    else:
        button = Button(root, text=text, bg='#023e8a', fg='white', width=9, height=2, command=lambda text=text: get_input(text))
        button.grid(row=row, column=column)
        button.config(font=('arial', 14))


root.mainloop()