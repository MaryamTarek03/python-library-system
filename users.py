import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import constants as c
import widgets as w
import customtkinter as ctk

def add_data() :
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    if name and email and phone :
        tree.insert('', 'end', values = (name, email, phone))
        clear_entries()
    else:
       messagebox.showwarning("Input Error", "Please fill all fields")

def update_data() :
    selected_item = tree.selection()
    if selected_item :
        name = name_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
        if name and email and phone :
            tree.item(selected_item, values = (name, email, phone))
            clear_entries()
        else:
           messagebox.showwarning("Input Error", "Please fill all fields")
    else:
       messagebox.showwarning("Selection Error", "Please select an item to update")

def delete_data() :
    selected_item = tree.selection()
    if selected_item :
        tree.delete(selected_item)
    else :
        messagebox.showwarning("Selection Error", "Please select an item to delete")

def clear_entries() :
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


class Users(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=c.backgroundColor)

        # grid configuration : main frame
        self.rowconfigure((0,1,2,3), weight = 1)
        self.rowconfigure(4, weight = 6)
        self.columnconfigure((0,1,2), weight = 1)

        # labels
        name_label = tk.Label(self, text = "Name",font=(c.family), background=c.backgroundColor)
        name_label.grid(row = 0, column = 0, padx = 10, pady = 10,sticky='e')
        email_label = tk.Label(self, text = "Email",font=(c.family), background=c.backgroundColor)
        email_label.grid(row = 1, column = 0, padx = 10, pady = 10,sticky='e')
        phone_label = tk.Label(self, text = "Phone Number",font=(c.family), background=c.backgroundColor)
        phone_label.grid(row = 2, column = 0, padx = 10, pady = 10,sticky='e')

        # entries
        name_entry = w.my_entry(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user name")
        name_entry.grid(row = 0, column = 1, columnspan= 2, padx = (10,200), pady = 10, sticky='we')
        email_entry = w.my_entry(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user email")
        email_entry.grid(row = 1, column = 1, columnspan= 2, padx = (10,200), pady = 10, sticky='we')
        phone_entry = w.my_entry(self,font=ctk.CTkFont(c.family,size=16),hint="Enter user phone number")
        phone_entry.grid(row = 2, column = 1, columnspan= 2, padx = (10,200), pady = 10, sticky='we')

        # buttons
        add_button = w.my_button(self,text="Add",font=ctk.CTkFont(c.family,size=20),command=add_data)
        add_button.grid(row = 3, column = 0, padx = 10, pady = 20,sticky='e')
        update_button = w.my_button(self,text="Update",font=ctk.CTkFont(c.family,size=20),command=update_data)
        update_button.grid(row = 3, column = 1, padx = 10, pady = 10)
        delete_button = w.my_button(self,text="Delete",font=ctk.CTkFont(c.family,size=20),command=delete_data)
        delete_button.grid(row = 3, column = 2, padx = 10, pady = 10,sticky='w')

        # table
        tree = ttk.Treeview(self, columns = ("Name", "Email", "Phone Number"), show = 'headings')
        tree.heading("Name", text = "Name")
        tree.heading("Email", text = "Email")
        tree.heading("Phone Number", text = "Phone Number")
        tree.grid(row = 4, column = 0, columnspan = 3, padx = 10, pady = 10)



# test Users class
# root = tk.Tk()
# root.title("CRUD Users")
# root.geometry("800x600")

# Users(root).pack()

# root.mainloop()