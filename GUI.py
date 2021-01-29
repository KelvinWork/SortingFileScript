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
    update_result_lbl.config(
        text = "Sorting completed",
        bg="green",
        font=('Helvetica', 12, 'bold')
    )
    update_lbl.config(
        text = check_items_folder(formatted_destination_path + "unidentifiable")
    )


def browse_source_file():
    file_name = filedialog.askdirectory()
    source_ent.insert(END, file_name)
    print(type(file_name))
    if (btn_event_listener() == 1 and type(file_name) is str):
        open_source_file_btn.config(
            state="disabled"
        )

def browse_destination_file():
    file_name = filedialog.askdirectory()
    destination_ent.insert(END, file_name)

    formatted_file_name = file_name[2:] + "/"
    generate_mosquito_folder(formatted_file_name)
    if (btn_event_listener() == 1 and type(formatted_file_name) is str):
        open_destination_file_btn.config(
            state = "disabled"
        )
    return formatted_file_name


def generate_mosquito_folder(formatted_file_name):
    #mosquito_category_folder()

    if os.listdir(formatted_file_name) == []:
        mosquito_category_folder(formatted_file_name)
        file_status_lbl.config(
            text = "Folder has been generated !",
            bg = "green",
            font=('Helvetica', 10, 'bold')
        )

    else:
        file_status_lbl.config(
            text = "Error generating folder. \n Please ensure folder is empty",
            bg = "red",
            fg = "white",
            font = ('Helvetica', 12 , 'bold')
        )

def btn_event_listener():
    return 1



destination_lbl = Label(
    text = "Enter the folder destination path :"
)

source_lbl = Label(
    text = "Enter the folder source path :"
)

file_status_text_lbl= Label(
    text = " FILE STATUS"
)
file_status_lbl = Label(
    text = "STATUS",
    bg = "Gray",
    fg = "White",
    font = ('Helvetica', 12 , 'bold')
)

update_text_lbl = Label(
    text = "Update :"
)

update_result_lbl = Label(
    text = "- - - - - - - -"
)
update_lbl = Label(
    text = "- - - - - - - -"
)


destination_ent = Entry(
)

source_ent = Entry(

)



submit_btn = Button(
    text = "Start Sorting",
    command = submit
)
open_source_file_btn = Button(
    text = "Browse File",
    command = lambda:[browse_source_file(),btn_event_listener()]
)
open_destination_file_btn = Button(
    text = "Browse File",
    command = lambda:[browse_destination_file(),btn_event_listener()]
)

reset_btn = Button(
    text = "Reset",

)


destination_lbl.grid(row=0, column=0, padx=10, pady=5)
destination_ent.grid(row=0, column=1, padx=10, pady=5)
open_destination_file_btn.grid(row=0, column=2, padx=10, pady=5)

file_status_text_lbl.grid(row=1, column=0, padx=10, pady=5)
file_status_lbl.grid(row=1, column=1, padx=10, pady=5)



source_lbl.grid(row=2, column=0, padx=10, pady=5)
source_ent.grid(row=2, column=1, padx=10, pady=5)
open_source_file_btn.grid(row=2, column=2, padx=10, pady=5)

submit_btn.grid(row=3, column=2, padx=10, pady=5)

update_text_lbl.grid(row=4, column=0, padx=10, pady=5)
update_result_lbl.grid(row=4, column=1, padx=10, pady=5)
update_lbl.grid(row=5, column=1, padx=10, pady=5)

reset_btn.grid(row=6, column=0, padx=10, pady=5)








window.geometry('800x500')
window.title("Mosquito Sorting Programe")
window.mainloop()