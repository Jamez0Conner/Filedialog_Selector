from tkinter import *
from customtkinter import *
import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

root = Tk()
root.title("File Selector")
root.geometry('352x255')
root.configure(background='white')
root.resizable(False, False)

def set_Path(entry_path):
    path = ctk.filedialog.askopenfilename()
    # next we pass the entry field to auto delete whatever is currently in the entry field
    # delete starting at index 0 to the END of the entry field. ex: (from here 0 to -> here END)
    # Next we will use INSERT in the entry field, also at the 0 index. And what I want to insert is the path()
    entry_path.delete(0, ctk.END)
    entry_path.insert(0, path)

label_Title = CTkLabel(root, text='*Attach MP3 File',fg_color='white', font=('Helvetica regular',17),text_color='black')
label_Title.pack()
label_Title.place(x=110,y=40)

txt_Path = ctk.CTkEntry(root,width=120,border_color='black',fg_color='white',text_color='black')
txt_Path.pack()
txt_Path.place(x=117,y=80)


btn_get_path = ctk.CTkButton(root, text='Upload',command=lambda: set_Path(txt_Path))
btn_get_path.pack()
btn_get_path.place(x=107,y=140)

root.mainloop()

