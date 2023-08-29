from tkinter import *
import random

def roll():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    label.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label.pack()

root = Tk()
root.geometry("700x450")
root.title("Roll Dice")
label = Label(root,text="",font=("times",260))
button = Button(root,text="Let's roll the dice...",width=40,height=5,font=('times',15),bg="cyan",bd=5,command=roll)
button.pack(padx=5,pady=5)

root.mainloop()
