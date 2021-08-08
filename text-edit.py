
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
root.update()
root.mainloop()

def open_file():
   file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*"),("Python file", "*.py*")])
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
                                   filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*"), ("Python file", "*.py*")])
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
   mb.showinfo("About TextEdit", "This is just another text editor")
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

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
file_menu.add_command(label="New", command=open_new_file)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Close File", command=exit_application)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
edit_menu.add_command(label='Copy', command=copy_text)
edit_menu.add_command(label='Cut', command=cut_text)
edit_menu.add_command(label='Paste', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
edit_menu.add_command(label='Delete', command=delete_last_char)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
help_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')
help_menu.add_command(label='About TextEdit', command=about_notepad)
help_menu.add_command(label='About Commands', command=about_commands)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)


text_area = Text(root, font=("Times New Roman", 12))
text_area.grid(sticky=NSEW)
scroller = Scrollbar(text_area, orient=VERTICAL)
scroller.pack(side=RIGHT, fill=Y)
scroller.config(command=text_area.yview)
text_area.config(yscrollcommand=scroller.set)
