import tkinter as tk
from tkinter import messagebox

def show_selection():
    selected_index = listbox.curselection()
    if selected_index:
        item = listbox.get(selected_index)
        messagebox.showinfo("Вы выбрали", item)
    else:
        messagebox.showwarning("Ошибка", "Выберите элемент!")

root = tk.Tk()
root.title("Список и выбор элемента")

items = ["Python", "Java", "C++", "JavaScript"]

listbox = tk.Listbox(root)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

button = tk.Button(root, text="Показать выбранный", command=show_selection)
button.pack(pady=5)

root.mainloop()
