from tkinter import *
from random import randint

def generate():
    entry_1.delete(0,END)
    try:
        pw_length=int(entry_2.get())
        password=''
        if var_1.get()==0:
            for i in range(pw_length):
                password+=chr(randint(65,122))
            entry_1.insert(0, password)
        elif var_1.get()==1:
            for i in range(pw_length):
                password+=chr((randint(48,122)))
            entry_1.insert(0, password)
        elif var_1.get()==2:
            for i in range(pw_length):
                password+=chr((randint(33,126)))
            entry_1.insert(0, password)
        else:
            pass
    except ValueError:
        pass


#GUI INTERFACE
root=Tk()
root.title("Password Generator")

my_password=Label(root, text="Password:")
my_password.grid(row=0, column=0)

entry_1=Entry(root)
entry_1.grid(row=0, column=1, padx=30)

length_n=Label(root, text="Length:")
length_n.grid(row=1, column=0)

generate_button=Button(root, text="Generate Password", command=generate)
generate_button.grid(row=0, column=2)

var_1=IntVar()
low_button=Radiobutton(root, text="Low", variable=var_1, value=0)
low_button.grid(row=1, column=2, sticky='E')
medium_button=Radiobutton(root, text="Medium", variable=var_1, value=1)
medium_button.grid(row=1, column=3)
strong_button=Radiobutton(root, text="Strong", variable=var_1, value=2)
strong_button.grid(row=1, column=4)

entry_2=Entry(root)
entry_2.grid(row=1, column=1)


root.mainloop()
