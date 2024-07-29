import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import constants as c
import widgets as w


class Home(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        # font
        font_main = ctk.CTkFont(family=c.family, size = 18, weight = 'bold')
        
        # frame : search area
        self.search_area = ctk.CTkFrame(self, fg_color = c.backgroundColor)
        self.search_area.grid(row = 0 , column = 0, sticky = 'nsew')

        # frame : summary area
        self.summary = w.frame_colored(self)
        self.summary.grid(row = 2, sticky = 'nsew', padx = c.padding, pady = c.padding)
        
        # grid configuration : whole frame
        self.rowconfigure((0,1), weight = 1, uniform = 'c')
        self.rowconfigure(2, weight = 2, uniform = 'c')
        self.columnconfigure(0, weight = 1, uniform = 'c')

        # grid configuration : search area
        self.search_area.columnconfigure(0 , weight = 8, uniform = 'd')
        self.search_area.columnconfigure(1 , weight = 2, uniform = 'd')
        self.search_area.rowconfigure((0, 1), weight = 1)

        # grid configuration : summary area
        self.summary.columnconfigure((0, 1, 2), weight = 1, uniform = 'summary')
        self.summary.rowconfigure(0, weight = 1, uniform = 'summary')

        # row 1 : filter

        # row 1.1 : search

        # :: search bar 
        self.search_bar = w.my_entry(self.search_area, hint = 'Search for books', font = font_main)
        self.search_bar.grid(row = 0 , column = 0, sticky = 'new', padx = (c.padding, 5), pady = c.padding)

        # :: search button
        self.search_button = w.my_button(self.search_area, text = 'search', font = font_main, command= lambda : print('search'))
        self.search_button.grid(row = 0, column = 1, sticky = 'new', padx = (5, c.padding), pady = c.padding)

        # row 1.2 : categories
        

        # row 2: popular


        # row 3: summary
        # items
        self.summary_item_books = SummaryItem(self.summary, text = 'books', number = 540)
        self.summary_item_loans = SummaryItem(self.summary, text = 'loans', number = 27)
        self.summary_item_due_loans = SummaryItem(self.summary, text = 'due loans', number = 4)

        # grid
        self.summary_item_books.grid(column = 0, row = 0, sticky = 'nsew', padx = c.padding, pady = c.padding)
        self.summary_item_loans.grid(column = 1, row = 0, sticky = 'nsew', padx = c.padding, pady = c.padding)
        self.summary_item_due_loans.grid(column = 2, row = 0, sticky = 'nsew', padx = c.padding, pady = c.padding)

class SummaryItem(ctk.CTkFrame):
    def __init__(self, parent, text, number):
        super().__init__(parent, fg_color = 'transparent')
        
        # attributes
        self.number = ctk.CTkLabel(self, text = f'{number}', font = ctk.CTkFont('Gabriola', size = 50, weight = 'bold'))
        self.text = ctk.CTkLabel(self, text = text, font = ctk.CTkFont('Gabriola', size = 20))
        
        # grid configuration
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')

        # widgets
        self.number.grid(row = 0, sticky = 'sew')
        self.text.grid(row = 1, sticky = 'new')