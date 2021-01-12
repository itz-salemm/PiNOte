from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox, font
from tkinter import ttk 
from datetime import datetime
import webbrowser

global open_name
open_name = False

#Definition of functions
def new():
	Newfolder = ttk.Frame(notebook)
	notebook.add(Newfolder, text="New Folder")

	notebook.pack(fill="both", expand="yes")

	text = scrolledtext.ScrolledText(Newfolder, height=1000, undo=True)
	text.configure(bg='black', foreground='white', font=("Arial 12"), padx=10, pady=10)
	text.pack(fill=BOTH)
def save():
	global open_name
	if open_name:
		root.filename.write(text.get(1.0, END))
def save_as():
	root.filename = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
	if root.filename is None:
		file_save = str(text.get(1.0, END))
		root.filename.write(file_save)
def exit():
	message = messagebox.askquestion('PiNote', "Do you want to save the changes?")
	if message == "yes":
		save_as()
	else:
		root.destroy()
def open_file():
	root.filename = filedialog.askopenfilename(initialdir='/', title="Select File", filetypes=(("Python file", "*.py"), ("All files", "*.*")))
	#Check to see if theere is a file name
	if root.filename:
		#Make the name global so we can access it later
		global open_name
		open_name = root.filename

	name = root.filename
	root.title(f'{name} - PiNote')
	file = open(root.filename)
	text.insert('end', file.read())
def undo():
	pass
def redo():
	pass
def cut():
	text.event_generate("<<Cut>>")
def copy():
	text.event_generate("<<Copy>>")
def paste():
	text.event_generate("<<Paste>>")
def delete():
	message = messagebox.askquestion('PiNote', "Do you want to Delete All?")
	if message == "yes":
		text.delete('1.0', 'end')
	else:
		return 'break'
def select_all():
	text.tag_add('sel', '1.0', 'end')
	return 'break'
def time():
	pass
def view_help():
	pass
def send_feedback():
	pass



#UI Designs

root = Tk()
root.geometry('1700x800')
root.minsize(200,100)
root.title("PiNote")
root.configure(bg='black')

#Notebook 
notebook = ttk.Notebook(root)
Newfolder = ttk.Frame(notebook)
notebook.add(Newfolder, text="New Folder")
notebook.pack(fill="both", expand="yes")

#Text Area
text = scrolledtext.ScrolledText(Newfolder, height=1000, undo=True)
text.pack(fill=BOTH)
text.configure(bg='black', foreground='white', font=("Arial 12"), padx=10, pady=10)
menubar= Menu(root)


#MENU TAB

#File Menu Tab
file = Menu(menubar,tearoff = 0)
file.add_command(label="New                             ", accelerator="Ctrl+N", command=new)
file.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
file.add_command(label="Save", accelerator="Ctrl+S", command=save)
file.add_command(label="Save as", accelerator="Ctrl+Shift+S",  command=save_as)
file.add_command(label="Save all", accelerator="Ctrl+Shift+S")
file.add_separator()
file.add_command(label="Close", accelerator="Ctrl+N")
file.add_command(label="Close", accelerator="Ctrl+N")
file.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=file, font=('verdana',10,'bold'))

#Edit Menu Tab
edit = Menu(menubar,tearoff=0)
edit.add_command(label="Undo                              ", accelerator="Ctrl+Z", command=undo)
edit.add_command(label="Redo", accelerator="Ctrl+Y", command=redo)
edit.add_separator()
edit.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
edit.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
edit.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
edit.add_command(label="Delete", accelerator="Del", command=delete)
edit.add_command(label="Select All", accelerator="Ctrl+A", command=select_all)
edit.add_command(label="Time/Date", accelerator="F5", command=time)
menubar.add_cascade(label="Edit", menu=edit)

#Format Menu Tab
Format = Menu(menubar,tearoff =0)
Format.add_command(label="Word wrap                              ")
menubar.add_cascade(label="Format", menu=Format)

#Help Menu Tab
Help = Menu(menubar, tearoff = 0)
Help.add_command(label="View Help                              ", command=view_help)
Help.add_command(label="Send Feedback", command=send_feedback)
menubar.add_cascade(label="Help", menu=Help)


#Mouse Click
m = Menu(root,tearoff =0)
m.add_command(label="Select All", accelerator="Ctrl-A", command=select_all)
m.add_command(label="Cut", accelerator="Ctrl-A", command=cut)
m.add_command(label="Copy", accelerator="Ctrl-C", command=copy)
m.add_command(label="Paste", accelerator="Ctrl-V", command=paste)
m.add_command(label="Delete", accelerator="Del", command=delete)
m.add_separator()
m.add_command(label="Undo", accelerator="Ctrl-Z", command=undo)
m.add_command(label="Redo", accelerator="Ctrl-Y", command=redo)

def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

root.bind("<Button-3>", do_popup)


root.config(menu=menubar)

root.mainloop()