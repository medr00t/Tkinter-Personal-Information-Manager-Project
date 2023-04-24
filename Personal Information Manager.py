from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x400")
root.title("Menu page")

num_list = []
name_list = []
nickname_list = []


def new_window(Title):
    window = tk.Toplevel()
    window.title(Title)
    window.geometry("400x400")
    return window


# if the var_name.get() == 0 restart the root & TopLevel windows (bug fixed)
def null_get(variable, TopLevel_window, function):

    if variable.get() == 0:
        root = tk.Tk()

        # destroying the main window
        root.destroy()

        # recreating the window
        root = tk.Tk()
        root.geometry("400x400")
        root.title("Menu page")

        TopLevel_window.destroy()

        # Calling the function that create the top level window
        function()
        return root, TopLevel_window


def edit():
    global window
    global entry_edit
    global entry_edit_name
    global entry_edit_nickname
    global entry_edit_num

    window = new_window("Edit window")
    label_entry = tk.Label(window, text="I want to edit the element number : ")
    label_entry.pack()

    # the index to edit starts from 1 to max length
    entry_edit = tk.Entry(window)
    entry_edit.pack()

    # Entries to edit informations
    label_entryEdit_num = tk.Label(window, text="Num")
    label_entryEdit_num.pack()
    entry_edit_num = tk.Entry(window)
    entry_edit_num.pack()

    label_entryEdit_name = tk.Label(window, text="Name")
    label_entryEdit_name.pack()
    entry_edit_name = tk.Entry(window)
    entry_edit_name.pack()

    label_entryEdit_nickname = tk.Label(window, text="Nickname")
    label_entryEdit_nickname.pack()
    entry_edit_nickname = tk.Entry(window)
    entry_edit_nickname.pack()

    # submit button
    edit_submit_button = tk.Button(window, text="Start Editing ", command=editSubmit)
    edit_submit_button.pack()


def editSubmit():
    global window

    index = int(entry_edit.get()) - 1
    new_num = entry_edit_num.get()
    new_name = entry_edit_name.get()
    new_nickname = entry_edit_nickname.get()

    if len(num_list) > index and index >= 0:
        print(index)
        print(len(num_list))
        num_list[index] = new_num
        name_list[index] = new_name
        nickname_list[index] = new_nickname
        messagebox.showinfo("Successfully", "The informations were successfully edited !")
        window.destroy()
        showAll()

    elif index == -1:
        messagebox.showinfo("Error 404", "Indexes start from 1 !")
        window.destroy()

    else:
        messagebox.showinfo("Error 404", f"Index out of range : \n      Please check if the index is correct. ")
        print(index)
        print(len(num_list))
        window.destroy()


def delete():
    global window_delete
    global entry_delete

    window_delete = new_window("Delete window")
    label_entry = tk.Label(window_delete, text="Enter the index of 'first index = 1' : ")
    label_entry.pack()

    # the index to deete starts from 1 to max length
    entry_delete = tk.Entry(window_delete)
    entry_delete.pack()

    # submit button
    delete_submit_button = tk.Button(window_delete, text="Start Deleting", command=deleteSubmit)
    delete_submit_button.pack()


def deleteSubmit():
    global window_delete

    index = int(entry_delete.get()) - 1

    del num_list[index]
    del name_list[index]
    del nickname_list[index]
    messagebox.showinfo("Successfully", "The ELement was successfully Deleted !")
    window_delete.destroy()


def showAll():
    global window_show

    window_show = new_window("Show All window")
    text = tk.Text(window_show)
    if len(num_list) != 0:
        for i in range(len(num_list)):
            text.insert(tk.END, f"{i+1} | Num.{num_list[i]} | Name : {name_list[i]} | Nickname :{nickname_list[i]} \n")
            text.insert(tk.END, "-------------------------------------------------")
    else:
        text.insert(tk.END, "Error : No element found :( ! ")
    text.configure(state=DISABLED)
    text.pack()


def search():
    global entry_search
    global window_search
    window_search = new_window("Search window")
    entry_search = tk.Entry(window_search)
    entry_search.pack()
    search_submit_button = tk.Button(window_search, text="Start searching ", command=searchSubmit)
    search_submit_button.pack()


def searchSubmit():
    window_search_result = new_window("Search window")
    text = tk.Text(window_search_result)
    boolean = False

    null_get(searchIn_menu_var, window_search_result, search)

    if searchIn_menu_var.get() == "Num":
        for i in range(len(num_list)):
            if entry_search.get() == num_list[i]:
                boolean = True
                text.insert(tk.END,
                            f"{i} | Num.{num_list[i]} | Name : {name_list[i]} | Nickname :{nickname_list[i]} \n")
                text.insert(tk.END, "---------------------------------")

    elif searchIn_menu_var.get() == "Name":
        for i in range(len(name_list)):
            if entry_search.get() == name_list[i]:
                boolean = True
                text.insert(tk.END,
                            f"{i} | Num.{num_list[i]} | Name : {name_list[i]} | Nickname :{nickname_list[i]} \n")
                text.insert(tk.END, "----------------------------------")

    elif searchIn_menu_var.get() == "Nickname":
        for i in range(len(nickname_list)):
            if entry_search.get() == nickname_list[i]:
                boolean = True
                text.insert(tk.END,
                            f"{i} | Num.{num_list[i]} | Name : {name_list[i]} | Nickname :{nickname_list[i]} \n")
                text.insert(tk.END, "---------------------------------")

    elif searchIn_menu_var.get() == "All":
        for i in range(len(num_list)):
            boolean = True
            if (entry_search.get() == num_list[i]) or (entry_search.get() == name_list[i]) or (
                    entry_search.get() == nickname_list[i]):
                text.insert(tk.END,
                            f"{i} | Num.{num_list[i]} | Name : {name_list[i]} | Nickname :{nickname_list[i]} \n")
                text.insert(tk.END, "---------------------------------")
    if boolean == False:
        text.insert(tk.END, "Error : No element found :( ! ")

    text.configure(state=DISABLED)
    text.pack()
    window_search.destroy()


def sortBy():
    window_sort = new_window("sort window")
    text = tk.Text(window_sort)

    null_get(sort_menu_var, window_sort, sortBy)

    if sort_menu_var.get() == "Num":
        text.insert(tk.END, f"{sort_menu_var.get()} : \n")
        text.insert(tk.END, f"----------------------------------------\n")
        text.insert(tk.END, f"\n")

        for i in range(len(num_list)):
            text.insert(tk.END, f"{num_list[i]}\n")
            text.insert(tk.END, "-------------------------------------------------")


    elif sort_menu_var.get() == "Name":
        text.insert(tk.END, f"{sort_menu_var.get()} : \n")
        text.insert(tk.END, f"----------------------------------------\n")
        text.insert(tk.END, f"\n")

        for i in range(len(name_list)):
            text.insert(tk.END, f"{name_list[i]}\n")
            text.insert(tk.END, "-------------------------------------------------")

    else:
        text.insert(tk.END, f"{sort_menu_var.get()} : \n")
        text.insert(tk.END, f"----------------------------------------\n")
        text.insert(tk.END, f"\n")

        for i in range(len(nickname_list)):
            text.insert(tk.END, f"{nickname_list[i]}\n")
            text.insert(tk.END, "-------------------------------------------------")

    text.configure(state=DISABLED)
    text.pack()


def addNew():
    global window_add
    global num_Entry
    global name_Entry
    global nickname_Entry

    window_add = new_window("Add Window")

    num_label = tk.Label(window_add, text="Num")
    num_Entry = tk.Entry(window_add)

    name_label = tk.Label(window_add, text="Name")
    name_Entry = tk.Entry(window_add)

    nickname_label = tk.Label(window_add, text="Nickname")
    nickname_Entry = tk.Entry(window_add)

    add_button = tk.Button(window_add, text="Add", command=addToList)

    num_label.pack()
    num_Entry.pack()
    name_label.pack()
    name_Entry.pack()
    nickname_label.pack()
    nickname_Entry.pack()
    add_button.pack()


def addToList():
    num = num_Entry.get()
    name = name_Entry.get()
    nickname = nickname_Entry.get()

    if num and name and nickname:

        num_list.append(num)
        name_list.append(name)
        nickname_list.append(nickname)

        window_add.destroy()
        messagebox.showinfo("Successfully", "The informations were successfully added !")
    else:
        messagebox.showinfo("Error", "Error : Invalid data")

    # creation of the menu


menu = tk.Menu(root)
sort_menu_var = tk.StringVar()
searchIn_menu_var = tk.StringVar()

# menu content
sort_menu = tk.Menu(menu, tearoff=0)
add_menu = tk.Menu(menu, tearoff=0)
delete_menu = tk.Menu(menu, tearoff=0)
edit_menu = tk.Menu(menu, tearoff=0)
showAll_menu = tk.Menu(menu, tearoff=0)
search_menu = tk.Menu(menu, tearoff=0)

# Full-menu content
menu.add_cascade(label="Add new ", menu=add_menu)
menu.add_cascade(label="Sort By", menu=sort_menu)
menu.add_cascade(label="Show All", menu=showAll_menu)
menu.add_cascade(label="Search in ", menu=search_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label="Delete", menu=delete_menu)

# add-menu item
add_menu.add_checkbutton(label="Add new", command=addNew)

# showAll-menu item
showAll_menu.add_checkbutton(label="Show All", command=showAll)

# Search-menu item
search_menu.add_checkbutton(label="Num", variable=searchIn_menu_var, onvalue="Num", command=search)
search_menu.add_checkbutton(label="Name", variable=searchIn_menu_var, onvalue="Name", command=search)
search_menu.add_checkbutton(label="Nickname", variable=searchIn_menu_var, onvalue="Nickname", command=search)
search_menu.add_checkbutton(label="All", variable=searchIn_menu_var, onvalue="All", command=search)

# edit-menu item
edit_menu.add_checkbutton(label="Edit", command=edit)

# sort-menu item
sort_menu.add_checkbutton(label="Num", variable=sort_menu_var, onvalue="Num", command=sortBy)
sort_menu.add_checkbutton(label="Name", variable=sort_menu_var, onvalue="Name", command=sortBy)
sort_menu.add_checkbutton(label="Nickname", variable=sort_menu_var, onvalue="Nickname", command=sortBy)

# delete-menu item
delete_menu.add_checkbutton(label="Delete", command=delete)

root.config(menu=menu)
root.mainloop()
