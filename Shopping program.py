import tkinter as tk
from tkinter import ttk, messagebox

def add_todo(event=None):
    todo = entry.get().strip()
    if todo:
        listbox.insert(tk.END, todo)
        entry.delete(0, tk.END)
        update_count()

def delete_selected():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        update_count()
    except IndexError:
        messagebox.showwarning("Error", "No items selected!")

def clear_all():
    if messagebox.askyesno("Are you sure you want to delete the entire list?" , "OK"):
        listbox.delete(0, tk.END)
        update_count()

def update_count():
    count_label.config(text=f"Number of items: {listbox.size()}")

root = tk.Tk()
root.title("Shopping list")
root.geometry("500x500")
root.configure(bg="#bc116f")

# قاب بالا
top_frame = ttk.Frame(root)
top_frame.pack(pady=10)

entry = ttk.Entry(top_frame, width=35)
entry.grid(row=0, column=0, padx=5)
entry.bind("<Return>", add_todo)

add_button = ttk.Button(top_frame, text="Add", command=add_todo)
add_button.grid(row=0, column=1, padx=5)

# لیست + اسکرول‌بار
frame_list = ttk.Frame(root)
frame_list.pack(pady=10)

scrollbar = ttk.Scrollbar(frame_list, orient="vertical")
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame_list, width=50, height=18, yscrollcommand=scrollbar.set, selectmode=tk.SINGLE)
listbox.pack(side="left", padx=5)
scrollbar.config(command=listbox.yview)

# قاب پایین
bottom_frame = ttk.Frame(root)
bottom_frame.pack(pady=10)

delete_button = ttk.Button(bottom_frame, text="Items number", command=delete_selected)
delete_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(bottom_frame, text="delete Items", command=clear_all)
clear_button.grid(row=0, column=1, padx=5)

count_label = ttk.Label(root, text="count : 0 ", font=("tahoma", 11, "bold"))
count_label.pack(pady=10)

root.mainloop()
