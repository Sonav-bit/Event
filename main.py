from tkinter import *
root=Tk()

def handle_key( event):
    print(event.char)
root.bind('<Key>',handle_key)
def handle_click (event):
    print('A button is clicked')
b1=Button(root,text='click me')
b1.pack()
b1.bind('<Button-1>',handle_click)


root.mainloop()

