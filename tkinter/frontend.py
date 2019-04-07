#ececec

"""
A program that store this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
from tkinter import messagebox
import backend

# create a hash table to store id and value pair
hash = {}

def get_selected_row(event):
    global selected
    global value_list
    if list1.curselection():
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        for k, v in hash.items():
            if v == selected_tuple:
                selected = k
                value = v
        value_list = value.split(" | ")
    else:
        pass

def view_command():
    # be careful!!! I change everything to str
    list1.delete(0, END)
    for row in backend.view():
        id, value = row[0], row[1:]
        string = ""
        for element in value:
            string += str(element)
            string += " | "
        list1.insert(END, string)
        hash[id] = string

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        value = row[1:]
        string = ""
        for element in value:
            string += str(element)
            string += " | "
        list1.insert(END, string)
    # update hash
    for row in backend.view():
        id, value = row[0], row[1:]
        string = ""
        for element in value:
            string += str(element)
            string += " | "
        hash[id] = string

def add_command():
    if title_text.get() == "" or author_text.get() == "" or year_text.get() == "" or isbn_text.get() == "":
        messagebox.showerror("Error", "All Entries Must Be Filled In")
    elif any(isbn_text.get() in v for v in hash.values()):
        messagebox.showerror("Error", "No duplication Allowed")
    else:
        list1.delete(0, END)
        backend.insert(title_text.get().strip(), author_text.get().strip(), year_text.get(), isbn_text.get())
        messagebox.showinfo("Success", "Book Entry Added!")

def delete_command():
    list1.delete(0, END)
    backend.delete(selected)
    messagebox.showinfo("Success", "Book Entry Deleted!")

def update_command():
    list1.delete(0, END)
    if title_text.get() == "":
        title = value_list[0]
    else:
        title = title_text.get()
    if author_text.get() == "":
        author = value_list[1]
    else:
        author = author_text.get()
    if year_text.get() == "":
        year = value_list[2]
    else:
        year = year_text.get()
    if isbn_text.get() == "":
        isbn = value_list[3]
    else:
        isbn = isbn_text.get()

    backend.update(selected, title.strip(), author.strip(), year, isbn)
    messagebox.showinfo("Success", "Entry Has Been Updated!")





window = Tk()
window.title("bookstore")
window["bg"] = "#ececec"

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

b1 = Button(window, text="View all", width=10, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=10, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=10, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=10, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=10, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=10, command=window.destroy)
b6.grid(row=7, column=3)

#scroll bar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

for i in [l1, l2, l3, l4, e1, e2, e3, e4]:
    i["bg"] = "#ececec"

for i in [e1, e2, e3, e4, b1, b2, b3, b4, b5, b6]:
    i.config(highlightbackground="#ececec")

window.mainloop()
