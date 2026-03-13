import tkinter as tk
from tkinter import messagebox

def show_text():
    user_text = entry.get()
    messagebox.showinfo("Вы ввели", user_text)

root = tk.Tk()
root.title("Текстовое поле + Кнопка")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

button = tk.Button(root, text="Показать текст", command=show_text)
button.pack(pady=5)

root.mainloop()
