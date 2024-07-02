import random
import tkinter as tk
from tkinter import PhotoImage


def heads_tails():
    a=random.randrange(0,2)
    if a==0:
        img=PhotoImage(file='coin.png')
        himg=tk.Label(window,image=img)
        hl=tk.Label(window, text="It's Heads!", font=('Arial',50))
        himg.image=img
        himg.grid(column=0,row=2)
        hl.grid(column=0,row=3,pady=100)

    else:
        img1=PhotoImage(file='coin1.png')
        timg=tk.Label(window,image=img1)
        tl=tk.Label(window, text="It's Tails!", font=('Arial',50))
        timg.image=img1
        timg.grid(column=0,row=2)
        tl.grid(column=0,row=3,pady=100)



window=tk.Tk()
window.title("Toss a Coin")
window.geometry("500x500")
window.iconbitmap('favicon.ico')
window.config(background="Light Blue")
lab=tk.Label(window, text="Toss in proggres please click the button!", font="Arial")
button=tk.Button(window,text="Click Me to Toss the Coin", font="Elephant",command=heads_tails)
button.grid(column=0,row=1,padx=100,pady=5)
lab.grid(column=0,row=0,padx=100,pady=5)
window.mainloop()
