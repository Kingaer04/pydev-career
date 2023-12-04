import sys
from tkinter import *

"""SAMPLES"""

# widget = Label(root)
# widget.config(text="Hello GUI world!")
# widget.pack(expand=YES, fill=BOTH)
# root.mainloop()

def hello(event):
    print('Press twice to exit')

def greeting():
    print("OIIIIIII WELCOME")

    
def quit(event):
    print("Hello, I must leave now!")
    sys.exit()

root = Tk()

root.title("Hello")
#Label(root, text="Hello GUI world!").pack(expand=YES, fill=BOTH) # To expand when the window is been expand
#Button(root, text="PRESS THIS TO QUIT", command=root.quit).pack(expand=YES, fill=X)
#widget = Button(root, text="Hello GUI world!")
#widget.pack()
#widget.bind('<Button-1>', hello)
#widget.bind('<Double-1>', quit)

win = Frame()
win.pack()
Label(win, text="WELCOME TO MY CLASS").pack(side=TOP)
Button(win, text="Hello", command=greeting).pack(side=LEFT)
Button(win, text="Quit", command=win.quit).pack(side=RIGHT)

root.mainloop()
