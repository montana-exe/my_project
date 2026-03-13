import tkinter as tk

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Меню File → Exit")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

root.mainloop()
