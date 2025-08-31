from tkinter import *
window =Tk()
window.title('Radio Tutorial')
choice = IntVar()
choice.set("2")
def clicked(value):
    myLabel  = Label(window, text=value)
    myLabel.pack()
    print(value)
Radiobutton(window,text="male",variable=choice,value=1,command=lambda:clicked(choice.get())).pack(anchor=W)
Radiobutton(window,text="female",variable=choice,value=2,command=lambda:clicked(choice.get())).pack(anchor=W)
mainloop()
