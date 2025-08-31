from tkinter import *
window= Tk()

window.title("Menu Bar sub option Tutoial")
window.geometry('350x200')

menubar = Menu(window)
filemenu = Menu(menubar,tearoff=1)
filemenu.add_command(label="open")
filemenu.add_command(label="save")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=window.quit)
menubar.add_cascade(label="file",menu=filemenu)

editmenu = Menu(menubar,tearoff=0)
editmenu.add_command(Label="cut")
editmenu.add_command(label="copy")
window.mainloop()
