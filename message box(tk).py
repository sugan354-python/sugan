from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('message box')
#showinfo,showwarning,showerror,
#askquestion,askokcancel,askyesno

def popup():
    response = messagebox.showerror("this is my Popup!","hello world!")
    Label(window, text=response).pack()
    if response == 1:
        Label(window, tex="you clicked yes!").pack()
    else:
        Label(window,text="you Clicked no!!").pack()

Button(window, text="Popup", command=popup).pack()
mainloop()
          
