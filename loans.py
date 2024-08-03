import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import customtkinter as ctk
import widgets as w
import constants as c



# Function to Book Names and members
def search():
    # query = return_search_entry.get().lower()
    # filtered_books = [book for book in loaned_books if query in book["Title"].lower() or query in book["User Name"].lower()]
    # update_loaned_books_list(filtered_books)
    pass

# Function to clear issue book fields
def clear_issue_fields():
    # book_name_entry.delete(0, tk.END)
    # user_name_entry.delete(0, tk.END)
    # issue_date_entry.delete(0, tk.END)
    # due_date_entry.delete(0, tk.END)
    pass

# Function to update the loaned books list
def update_loaned_books_list(filtered_books=None):
    # for i in loaned_books_list.get_children():
    #     loaned_books_list.delete(i)
    # books = filtered_books if filtered_books else loaned_books
    # for i, book in enumerate(books):
    #     loaned_books_list.insert("", "end", iid=i, values=(book["Title"], book["User Name"], book["Issue Date"], book["Due Date"], book["Status"]))
    pass

# Function to return a book
def return_book():
    # selected_item = loaned_books_list.selection()
    # if selected_item:
    #     item_index = int(selected_item[0])
    #     loaned_books.pop(item_index)
    #     update_loaned_books_list()
    # else:
    #     messagebox.showerror("Error", "Please select a book to return.")
    pass

# Function to issue a book
def issue_book():
    # book_name = book_name_entry.get()
    # user_name = user_name_entry.get()
    # issue_date = issue_date_entry.get()
    # due_date = due_date_entry.get()

    # if book_name and user_name and issue_date and due_date:
    #     loaned_books.append({
    #         "Title": book_name,
    #         "User Name": user_name,
    #         "Issue Date": issue_date,
    #         "Due Date": due_date,
    #         "Status": "Issued"
    #     })
    #     update_loaned_books_list()
    #     clear_issue_fields()
    # else:
    #     messagebox.showerror("Error", "All fields must be filled out.")
    pass



class LoanTable(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        loaned_books_label = tk.Label(self, text="List of Loaned Books", font=(c.family, 16), bg=c.backgroundColor)
        loaned_books_label.pack(anchor="w")

        loaned_books_list = ttk.Treeview(self, columns=("Title", "User Name", "Issue Date", "Due Date", "Status"), show="headings")
        loaned_books_list.heading("Title", text="Book Name")
        loaned_books_list.heading("User Name", text="User Name")
        loaned_books_list.heading("Issue Date", text="Issue Date")
        loaned_books_list.heading("Due Date", text="Due Date")
        loaned_books_list.heading("Status", text="Status")
        loaned_books_list.pack(fill=tk.X)


def field(parent, text, hint):
    frame = ctk.CTkFrame(parent, fg_color = c.backgroundColor)
    
    # frame grid configuration
    frame.columnconfigure(0, weight = 1, uniform = 'a')
    frame.columnconfigure(1, weight = 2, uniform = 'a')
    frame.rowconfigure(0, weight = 1, uniform = 'a')

    # label
    label = tk.Label(frame, text=text, background=c.backgroundColor, font=(c.family, 16))
    label.grid(row=0, column=0, sticky='e')

    # entry
    entry = w.my_entry(frame, hint, (c.family, 20))
    entry.grid(row = 0, column = 1, sticky = 'we', padx = (10, 75))

    # return
    return frame

class IssueBook(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        issue_label = tk.Label(self, text="Issue Book", font=(c.family, 24), bg=c.backgroundColor)
        issue_label.grid(row=0, column=0, columnspan=2)


        # grid configuration
        self.rowconfigure((0,1,2,3,4,5), weight = 1, uniform = 'a')
        self.rowconfigure(5, weight = 2, uniform = 'a')
        self.columnconfigure((0,1), weight = 1, uniform = 'a')

        book_title = field(self, 'Book Title', 'Enter Book Title')
        book_title.grid(row = 1, column = 0, columnspan = 2, sticky= 'we')

        user_name = field(self, 'User Name', 'Enter User Name')
        user_name.grid(row = 2, column = 0, columnspan = 2, sticky= 'we')

        issue_date = field(self, 'Issue Date', 'Enter Issue Date')
        issue_date.grid(row = 3, column = 0, columnspan = 2, sticky= 'we')

        due_date = field(self, 'Due Date', 'Enter Due Date')
        due_date.grid(row = 4, column = 0, columnspan = 2, sticky= 'we')

        cancel_button = w.my_button(self, 'Clear', (c.family, 20), command= clear_issue_fields)
        cancel_button.grid(row = 5, column = 0, sticky = 'e', padx = 10)

        issue_button = w.my_button(self, 'Issue Book', (c.family, 20), command= issue_book)
        issue_button.grid(row = 5, column = 1, sticky = 'w', padx = 10)


def issue_page():
    global issue_window 
    issue_window = tk.Toplevel()

    # app window size attributes
    display_width = issue_window.winfo_screenwidth()
    display_height = issue_window.winfo_screenheight()
    left = int(display_width / 2 - 500 / 2)
    top = int(display_height / 2 - 400 / 2)
    issue_window.geometry(f'500x400+{left}+{top}')

    # window configure
    issue_window.resizable(False, False)
    issue_window.rowconfigure(0, weight = 1, uniform = 'a')
    issue_window.columnconfigure(0, weight = 1, uniform = 'a')

    # frame configure
    frame = IssueBook(issue_window)
    frame.grid(row = 0, column = 0, sticky = 'nsew')

class Loan(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)
        
        # grid configuration
        self.rowconfigure((0,2), weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 3, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # search area
        search_area = w.SearchArea(self, search, 'loans')
        search_area.grid(row = 0, column = 0, padx= c.padding)

        # loans table
        table = LoanTable(self)
        table.grid(row = 1, column = 0, padx= 50)

        # issue book button
        issue_button = w.my_button(self, 'Issue a Book', font=ctk.CTkFont(c.family, size= 20), command=issue_page)
        issue_button.grid(row = 2, column = 0)