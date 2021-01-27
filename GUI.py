from tkinter import *
from tkinter import filedialog
from File_Sort_Programme import *

window = Tk()

def submit():
    destination_path = destination_ent.get()
    source_path = source_ent.get()
    formatted_destination_path = destination_path[2:] + "/"
    formatted_source_path = source_path[2:] + "/"
    mosquito_sort_algorithm(formatted_source_path, formatted_destination_path)

def browse_source_file():
    file_name = filedialog.askdirectory()
    source_ent.insert(END, file_name)

def browse_destination_file():
    file_name = filedialog.askdirectory()
    destination_ent.insert(END, file_name)
    print(file_name)



def generate_mosquito_folder():
    #mosquito_category_folder()
    pass


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

file_status_ent = Label(
    text = "Hellow",
    bg = "Green"
)

submit_btn = Button(
    text = "Start Sorting",
    command = submit
)
open_source_file_btn = Button(
    text = "Browse File",
    command = browse_source_file
)
open_destination_file_btn = Button(
    text = "Browse File",
    command = browse_destination_file
)

generate_file_structure_btn = Button(
    text = "Generate Folder Structure",
    command = generate_mosquito_folder

)

destination_lbl.grid(row=0, column=0, padx=10, pady=5)
destination_ent.grid(row=0, column=1, padx=10, pady=5)
open_destination_file_btn.grid(row=0, column=2, padx=10, pady=5)

file_status_ent.grid(row=1, column=0, padx=10, pady=5)
generate_file_structure_btn.grid(row=1, column=1, padx=10, pady=5)


source_lbl.grid(row=2, column=0, padx=10, pady=5)
source_ent.grid(row=2, column=1, padx=10, pady=5)
open_source_file_btn.grid(row=2, column=2, padx=10, pady=5)

submit_btn.grid(row=3, column=2, padx=10, pady=5)








window.geometry('500x500')
window.title("Mosquito Sorting Programe")
window.mainloop()