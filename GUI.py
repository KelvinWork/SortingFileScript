import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

app_width = 500
app_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()



window.mainloop()