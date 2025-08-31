import tkinter as tk
def on_checkbox_click():
    if checkbox_var.get():
        label.config(text="checkbox checked")
    else:
        label.config(text="checkbox unchecked")
root=tk.Tk()
root.title("checkbox example")
label=tk.Label(root,text="chech or Uncheck th box:")
label.pack(pady=10)

#create a checkbutton
checkbox_var=tk.BooleanVar()
checkbox=tk.Checkbutton(root,text="check me",variable=checkbox_var,command=on_checkbox_click)
checkbox.pack()
root.mainloop()
