import string
import random
from tkinter import *

top = Tk()


def randomPassGen():
    passchar = list(string.ascii_letters + string.digits + "_@")
    """
    passchar = list(string.ascii_letters + string.digits + "_@")
    print(passChar)
    output would be ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    # 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
    # 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', 
    # '2', '3', '4', '5', '6', '7', '8', '9', '_', '@']"""

    length = 20
    # length of the password we can set it any length
    passwd = []
    # An iterating loop to select a random set of characters that can be used for the password
    for i in range(length):
        passwd.append(random.choice(passchar))
    random.shuffle(passwd)
    # the array passwd is shuffled, so it can not in a predictable manner
    password = "".join(passwd)
    return password


def onClick():
    passwd = randomPassGen()
    mylabel = Label(top, text=passwd)
    mylabel.pack()


top.minsize(width=640, height=400)
top.geometry("640x400")
img = PhotoImage(file='rsz_2457130f27e8216f443f6fa9b9ae76dda.png')
label = Label(top,image=img)
B = Button(top, text="Generate Password", command=onClick)

label.place(x=0, y=0)
B.pack()
top.mainloop()

