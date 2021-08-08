
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk
import os
import urllib
image = urllib.URLopener()
image.retrieve("http://www.gunnerkrigg.com//comics/00000001.jpg","00000001.jpg")
root = Tk()
root.title("Text-edit")
root.geometry('800x500')
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
icon = ImageTk.PhotoImage(Image.open('Notepad.png'))
root.iconphoto(False, icon)
def open_file():
   file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*"),(Python file", "*.py*")])
   if file != '':
       root.title(f"{os.path.basename(file)}")
       text_area.delete(1.0, END)
       with open(file, "r") as file_:
           text_area.insert(1.0, file_.read())
           file_.close()
   else:
       file = None
def open_new_file():
   root.title("TextEdit")
   text_area.delete(1.0, END)
def save_file():
   global text_area
   file = text_area.get(1.0, END)
   if file == '':
       file = None
   else:
       file = open(file, "w")
       file.write(text_area.get(1.0, END))
       file.close()
   if file is None:
       file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                   filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
   else:
       file = open(file, "w")
       file.write(text_area.get(1.0, END))
       file.close()
       root.title(f"{os.path.basename(file)} - Notepad")
def exit_application():
   root.destroy()
def copy_text():
   text_area.event_generate("<<Copy>>")
def cut_text():
   text_area.event_generate("<<Cut>>")
def paste_text():
   text_area.event_generate("<<Paste>>")
def select_all():
   text_area.event_generate("<<Control-Keypress-A>>")
def delete_last_char():
   text_area.event_generate("<<KP_Delete>>")
def about_notepad():
   mb.showinfo("About Notepad", "This is just another Notepad, but this is better than all others")
def about_commands():
   commands = """
Under the File Menu:
- 'New' clears the entire Text Area
- 'Open' clears text and opens another file
- 'Save As' saves your file in the same / another extension
Under the Edit Menu:
- 'Copy' copies the selected text to your clipboard
- 'Cut' cuts the selected text and removes it from the text area
- 'Paste' pastes the copied/cut text
- 'Select All' selects the entire text
- 'Delete' deletes the last character 
"""
   mb.showinfo(title="All commands", message=commands, width=60, height=40)
root.update()
root.mainloop()
