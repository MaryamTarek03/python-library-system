import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
import constants as c

def sign_out_button(parent):
    sign_out_button = ctk.CTkButton(parent, 
            text = '',
            corner_radius = 15,
            image = ctk.CTkImage(light_image = Image.open(c.sign_out)),
            compound = 'top',
            fg_color = c.primaryColor,
            text_color = 'black',
            hover_color = c.backgroundColor)
    return sign_out_button

def nav_button(parent, command, img_path, text):
    photo = Image.open(img_path).resize((100,100))
    button = ctk.CTkButton(parent,
            text= '',
            font = ctk.CTkFont(size = 8),
            image = ctk.CTkImage(light_image= photo, size=(55, 55)),
            text_color = 'black',
            hover_color = c.backgroundColor,
            fg_color = c.primaryColor,
            compound = 'top',
            command = command)
    return button

def my_entry(parent, hint, font, isHidden = False):
    char = ''
    if (isHidden == True):
        char = '*'
    search_bar = ctk.CTkEntry(parent, 
            placeholder_text = hint,
            font = font,
            corner_radius = c.radius, 
            fg_color = c.primaryColor,
            placeholder_text_color = c.fontColor,
            border_width = 0,
            height = c.widget_height, 
            show = char
            # lambda : '*' if isHidden else '*'
        )
    return search_bar

def my_button(parent, text, font, command):
    button = ctk.CTkButton(parent, 
            height = c.widget_height, 
            text = text,
            font = font,
            fg_color = c.buttonColor,
            hover_color = c.buttonHoverColor, 
            text_color = 'white',
            corner_radius = c.radius,
            command = command
        )
    return button

def frame_colored(parent):
    frame = ctk.CTkFrame(parent, fg_color = c.primaryColor, corner_radius = c.radius)
    return frame