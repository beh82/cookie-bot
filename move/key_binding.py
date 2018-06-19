from tkinter import *

root = Tk()


def leftkey(event):
    print('left key pressed')

def rightkey(event):
    print('right key pressed')

def topkey(event):
    print('top key pressed')

def buttomkey(event):
    print('buttom key pressed')


root.bind('<Left>' , leftkey)
root.bind('<Right>', rightkey)
root.bind('<Up>'   , topkey)
root.bind('<Down>' , buttomkey)


root.mainloop()
