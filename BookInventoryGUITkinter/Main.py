from tkinter import *
from backend import Database

database = Database("bookinventory.db")


def get_selected_row(event):
    global selected_row
    try:
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.view_all():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in database.search(title_var.get(), author_var.get(), year_var.get(), ISBN_var.get()):
        list1.insert(END, row)


def insert_command():
    database.insert_table(title_var.get(), author_var.get(), year_var.get(), ISBN_var.get())
    list1.delete(0, END)
    list1.insert(END, (title_var.get(), author_var.get(), year_var.get(), ISBN_var.get()))


def delete_command():
    database.delete_row(selected_row[0])


def update_command():
    database.update_row(selected_row[0], title_var.get(), author_var.get(), year_var.get(), ISBN_var.get())


window = Tk()
window.wm_title("BookInventory")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Year")
l2.grid(row=1, column=0)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_var = StringVar()
e1 = Entry(window, textvariable=title_var)
e1.grid(row=0, column=1)

author_var = StringVar()
e2 = Entry(window, textvariable=author_var)
e2.grid(row=0, column=3)

year_var = StringVar()
e3 = Entry(window, textvariable=year_var)
e3.grid(row=1, column=1)

ISBN_var = StringVar()
e4 = Entry(window, textvariable=ISBN_var)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=50)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)
b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
