from tkinter import *
from tkinter import filedialog

window = Tk()

def submit():
    destination_path = destination_ent.get()
    source_path = source_ent.get()

def browse_files():
    file_name = filedialog.askdirectory()
    source_ent.insert(END, file_name)

destination_lbl = Label(
    text = "Enter the folder destination path :"
)

source_lbl = Label(
    text = "Enter the folder source path :"
)

destination_ent = Entry(
)

source_ent = Entry(

)

submit_btn = Button(
    text = "Start Sorting",
    command = submit
)
open_file_btn = Button(
    text = "Browse File",
    command = browse_files
)

destination_lbl.grid(row=0, column=0, padx=10, pady=5)
destination_ent.grid(row=0, column=1, padx=10, pady=5)

source_lbl.grid(row=1, column=0, padx=10, pady=5)
source_ent.grid(row=1, column=1, padx=10, pady=5)
open_file_btn.grid(row=1, column=2, padx=10, pady=5)

submit_btn.grid(row=2, column=2, padx=10, pady=5)








window.geometry('500x500')
window.mainloop()