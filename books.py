import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import constants as c
import widgets as w

padding = 100

def field(parent,text,hint):
    frame=ctk.CTkFrame(parent,fg_color=c.backgroundColor)
    frame.rowconfigure((0,1),weight=1,uniform="a")
    frame.columnconfigure(0,weight=1,uniform="a")
    label=tk.Label(frame,text=text,bg=c.backgroundColor,font=(c.family,22))
    label.grid(row=0,column=0,sticky='ws',padx=c.padding)
    entry=w.my_entry(frame,hint=hint,font=ctk.CTkFont(c.family))
    entry.grid(row=1,column=0,sticky="wen")
    return frame


def buttons(parent):
    frame=ctk.CTkFrame(parent,fg_color=c.backgroundColor)
    frame.columnconfigure((0,1),weight=1,uniform="a")
    frame.rowconfigure(0,weight=1,uniform="a")
    submit_button=w.my_button(frame,"Cancel",font=ctk.CTkFont(c.family,size=18),command=lambda:print("cancel"))
    submit_button.grid(row=0,column=0, sticky = 'w')
    cancel_button=w.my_button(frame,"Submit",font=ctk.CTkFont(c.family,size=18),command=lambda:print("submit"))
    cancel_button.grid(row=0,column=1, sticky = 'e', padx=(0,padding))
    return frame

class BookCU(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=c.backgroundColor)

        # grid configuration : main frame (self)
        self.rowconfigure((0,1,2,3,4,5),weight=1,uniform="a")
        self.columnconfigure(0,weight=1,uniform="a")
        self.columnconfigure(1,weight=2,uniform="a")

        # title : row 1
        title_frame=field(self,"Title","Enter book title")
        title_frame.grid(row=0,column=1,sticky="we",padx=(0,padding))

        # author : row 2
        author_frame=field(self,"Author","Enter book author")
        author_frame.grid(row=1,column=1,sticky="we",padx=(0,padding))

        # ISBN : row 3
        isbn_frame=field(self,"ISBN","Enter book ISBN")
        isbn_frame.grid(row=2,column=1,sticky="we",padx=(0,padding))

        # color picker : row 4
        color_frame=field(self,"Book Color","Enter book color")
        color_frame.grid(row=3,column=1,sticky="we",padx=(0,padding))

        # image picker : row 5
        image_frame=field(self,"Title","Enter book image")
        image_frame.grid(row=4,column=1,sticky="we",padx=(0,padding))

        # buttons : row 6 (cancel and submit)
        buttons_frame=buttons(self)
        buttons_frame.grid(row=5,column=1,sticky="we")


# test frame class
#! UNCOMMENT TO RUN FROM THIS FILE

# window=ctk.CTk()
# window.geometry("800x600")

# window.rowconfigure(0,weight = 1)
# window.columnconfigure(0,weight = 1)

# frame = BookCU(window)
# frame.grid(sticky = 'nsew')

# window.mainloop()