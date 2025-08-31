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
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_command(label="paste")
menubar.add_cascade(label="Edit",menu=edit menu)


helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help",menu=helpmenu)

window.config(menu=menubar)

window.mainloop()
