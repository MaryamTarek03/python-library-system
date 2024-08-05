import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
import constants as c
import widgets as w
import database as db

# Sample data for demonstration
books = [
    {"title": "Book A", "author": "Author 1", "genre": "Fiction", "status": "issued"},
    {"title": "Book B", "author": "Author 2", "genre": "Non-Fiction", "status": "available"},
    {"title": "Book C", "author": "Author 1", "genre": "Fiction", "status": "issued"},
]

users = [
    {"name": "User 1"},
    {"name": "User 2"},
]

borrowings = [
    {"book_title": "Book A", "author": "Author 1", "user_name": "User 1", "issue_date": "2024-01-10", "due_date": "2024-02-10", "return_date": None},
    {"book_title": "Book C", "author": "Author 1", "user_name": "User 2", "issue_date": "2024-02-01", "due_date": "2024-03-01", "return_date": None},
]

# # Initialize main window
# report = tk.Tk()
# report.title("Library Management System - Reports")
# # report.resizable(False, False)

# # Variables
# fontsize = 25
# Width = 800
# Height = 600
# x = 80
# y = 50
# buttonColor = '#F26B6D'
# backgroundColor = '#FBF8F5'

# report['bg'] = backgroundColor
# screenwidth = report.winfo_screenwidth()
# screenheight = report.winfo_screenheight()
# report.geometry(f'{Width}x{Height}+{x}+{y}')

# report_type_var = tk.StringVar()

# Widgets declaration


class Report(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)
        self.rowconfigure((0,1,2,3,5), weight = 1, uniform='a')
        self.rowconfigure(4, weight = 5, uniform='a')
        self.columnconfigure(0, weight = 1, uniform='a')
        self.columnconfigure(1, weight = 2, uniform='a')

        # Report Type Dropdown
        tk.Label(self, text='Report Type', font=c.family, bg=c.backgroundColor).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        ctk.CTkComboBox(self, 
                        width=200, 
                        fg_color = 'white', 
                        border_color = c.primaryColor, 
                        button_color = c.primaryColor, 
                        dropdown_fg_color = c.primaryColor,
                        state='readonly', 
                        values=('Issued Books', 'Overdue Books', 'Active Users', 'User Borrowing History', 'Inventory Status'),
                        ).grid(row=0, column=1, padx=(10, 200), pady=10, sticky='we')
        # textvariable=report_type_var,

        # Date Range Picker
        tk.Label(self, text="Start Date", font=c.family, bg=c.backgroundColor).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        start_date_entry = w.my_entry(self, hint='Enter Start Date (YYYY-MM-DD)', font=(c.family, 16), height=20)
        start_date_entry.grid(row=1, column=1, padx=(10, 200), pady=10, sticky='we')

        tk.Label(self, text="End Date", font=c.family, bg=c.backgroundColor).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        end_date_entry = w.my_entry(self, hint='Enter End Date (YYYY-MM-DD)', font=(c.family, 16), height=20)
        end_date_entry.grid(row=2, column=1, padx=(10, 200), pady=10, sticky='we')

        # Generate Report Button
        generate_report_button = w.my_button(self, text='Generate Report', font=(c.family, 16, 'bold'), command=generate_report)
        generate_report_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Report View
        report_tree = ttk.Treeview(self, columns=("book_title", "user_name", "issue_date", "due_date", "return_date"), show="headings")
        report_tree.heading("book_title", text="Book Title")
        report_tree.heading("user_name", text="User Name")
        report_tree.heading("issue_date", text="Issue Date")
        report_tree.heading("due_date", text="Due Date")
        report_tree.heading("return_date", text="Return Date")
        report_tree.grid(row=4, column=0, columnspan=2, padx=100, pady=10, sticky='nsew')

        # Export Button
        export_button = w.my_button(self, text='Export', font=(c.family, 16, 'bold'), command=export_report)
        export_button.grid(row=5, column=0, columnspan=2, pady=10)


# Create GUI
def create_widgets(report):

    pass


# Generate Report function
def generate_report():
    pass
    # report_type = report_type_var.get()
    # start_date = start_date_entry.get()
    # end_date = end_date_entry.get()

    # try:
    #     start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    #     end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    # except ValueError:
    #     messagebox.showerror("Invalid Date", "Please enter valid date ranges.")
    #     return report_tree.delete(*report_tree.get_children())

    # if report_type == 'Issued Books':
    #     for b in borrowings:
    #         issue_date = datetime.strptime(b['issue_date'], '%Y-%m-%d')
    #         if start_date_dt <= issue_date <= end_date_dt:
    #             report_tree.insert("", "end", values=(b['book_title'], b['author'], b['user_name'], b['issue_date'], b['due_date'], b['return_date']))

    # elif report_type == 'Overdue Books':
    #     today = datetime.now()
    #     for b in borrowings:
    #         due_date = datetime.strptime(b['due_date'], '%Y-%m-%d')
    #         if due_date < today and b['return_date'] is None:
    #             report_tree.insert("", "end", values=(b['book_title'], b['author'], b['user_name'], b['issue_date'], b['due_date'], b['return_date']))

    # elif report_type == 'Books by Genre/Author':
    #     genre_author_counts = {}
    #     for book in books:
    #         key = (book['genre'], book['author'])
    #         if key in genre_author_counts:
    #             genre_author_counts[key] += 1
    #         else:
    #             genre_author_counts[key] = 1

    #     for (genre, author), count in genre_author_counts.items():
    #         report_tree.insert("", "end", values=(None, author, None, None, None, genre, count))

    # elif report_type == 'Active Users':
    #     active_users = {}
    #     for b in borrowings:
    #         issue_date = datetime.strptime(b['issue_date'], '%Y-%m-%d')
    #         if start_date_dt <= issue_date <= end_date_dt:
    #             if b['user_name'] in active_users:
    #                 active_users[b['user_name']] += 1
    #             else:
    #                 active_users[b['user_name']] = 1

    #     for user_name, borrow_count in active_users.items():
    #         report_tree.insert("", "end", values=(None, None, user_name, None, None, borrow_count))

    # elif report_type == 'User Borrowing History':
    #     user_name = start_date_entry.get()
    #     user_borrowing_history = [b for b in borrowings if b['user_name'] == user_name]

    #     for b in user_borrowing_history:
    #         report_tree.insert("", "end", values=(b['book_title'], b['author'], b['user_name'], b['issue_date'], b['due_date'], b['return_date']))

    # elif report_type == 'Inventory Status':
    #     for book in books:
    #         report_tree.insert("", "end", values=(book['title'], book['author'], None, None, None, book['status']))

# Export Report function
def export_report():
    # file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    # if not file_path:
    #     return

    # with open(file_path, "w") as f:
    #     for row in report_tree.get_children():
    #         values = report_tree.item(row, "values")
    #         f.write(",".join(str(v) for v in values if v) + "\n")

    # messagebox.showinfo("Export", "Report exported successfully!")
    pass

# # Initialize GUI components
# create_widgets(report)

# # Run the main loop
# report.mainloop()