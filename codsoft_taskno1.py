from tkinter import *
from tkinter.font import *

root=Tk()
root.title("To-Do List")
root.geometry("600x600")

font=Font(family="arial",size=25,weight="bold")

frame = Frame(root, bg="#add8e6", padx=2, pady=2)  # Light blue border
frame.pack(pady=10)

list_todo=Listbox(frame,font=font,width=60,height=8,bg="SystemButtonFace",bd=1,
 fg="#464646", highlightthickness=0, highlightcolor="#add8e6", activestyle=None)
list_todo.pack(side=LEFT,fill=Y)

scrollbar=Scrollbar(frame)
scrollbar.pack(side=RIGHT,fill=BOTH)
list_todo.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_todo.yview)

input=Entry(root, font=('arial',24))
input.pack(pady=20)

button_frame=Frame(root)
button_frame.pack(pady=20)

#Functions for buttons
def add_item():
    item_text=input.get().strip()
    if item_text:
        list_todo.insert(END,item_text)
        input.delete(0,END)

def delete_item():
    list_todo.delete(ANCHOR)

def mark_as_done():
    list_todo.itemconfig(
            list_todo.curselection(),
            fg="#808080")
    list_todo.selection_clear(0,END)

def unmark_item():
    list_todo.itemconfig(
        list_todo.curselection(),
        fg="#464646"
    )
    list_todo.selection_clear(0,END)

def delete_marked():
    count=0
    while count<list_todo.size():
        if list_todo.itemcget(count, "fg")=="#808080":
            list_todo.delete(list_todo.index(count))
        else:
            count+=1

#Add buttons to the Box
add_button=Button(button_frame, text="Add Item", command=add_item)
add_button.grid(row=0, column=0, padx=15)

delete_button=Button(button_frame, text="Delete Item", command=delete_item)
delete_button.grid(row=0, column=1, padx=15)

mark_button=Button(button_frame, text="Mark as Done", command=mark_as_done)
mark_button.grid(row=0, column=2, padx=15)

unmark_button=Button(button_frame, text="Unmark Item", command=unmark_item)
unmark_button.grid(row=0, column=3, padx=15)

delete_marked_button=Button(button_frame, text="Delete all Marked", command=delete_marked)
delete_marked_button.grid(row=0, column=4, padx=15)


root.mainloop()
