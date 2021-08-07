
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk
import os
import urllib
image = urllib.URLopener()
image.retrieve("http://www.gunnerkrigg.com//comics/00000001.jpg","00000001.jpg")
root = Tk()
root.title("Untitled - Text-edit")
root.geometry('800x500')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
root.iconphoto(False, icon)
