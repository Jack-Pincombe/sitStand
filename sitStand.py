# A basic program to tell the user when to sit and to stand
#jack pincombe jackpincombe@hotmail.co.uk

import _tkinter

from _tkinter import ttk



root = tk()

li = "jack pincombe".split()

listb = Listbox(root)

for item in li:
    listb.insert(0,item)

lisb.pack()
root.mainloop()
