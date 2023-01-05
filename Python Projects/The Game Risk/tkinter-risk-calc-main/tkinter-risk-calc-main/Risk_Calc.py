import tkinter as tk
from random import *

#Build
root = tk.Tk()
root.title("Risk Calculator")
root.geometry("1000x300")
#Theme
root.configure(bg="#ffffff")

#functions
def clc(at,de):
    while at >= 2 and de >= 0:
        at -= choice(range(0,3))
        de -= choice(range(0,3))
    if at <= 0:
        alpha= "Attacking side has ", str(1), " unit left."
    else:
        alpha="Attacking side has ", str(at), " units left."
    if de <= 0:
        bravo="Defending side has ", str(0), " unit left."
    else:
        bravo="Defending side has ", str(de), " units left."
    res.config(text=''.join(alpha))
    res2.config(text=''.join(bravo))
    
def clc2(at,de):
    atode=choice(range(1,4))
    other=True
    while other==True:
        if atode==1:
            at -= 2
        elif atode==2:
            at -= 1
            de -= 1
        else:
            de -= 2
        break
    alpha= "Attacking side has ", str(at), " units left."
    bravo= "Defending side has ", str(de), " units left."
    res.config(text=''.join(alpha))
    res2.config(text=''.join(bravo))
    
def clc3(at,de,ro):
    other=True
    count=0
    while other==True and count<=ro:
        count += 1
        atode=choice(range(1,4))
        if atode==1:
            at -= 2
        elif atode==2:
            at -= 1
            de -= 1
        else:
            de -= 2
    alpha="Attacking side has ", str(at), " units left."
    bravo="Defending side has ", str(de), " units left."
    res.config(text=''.join(alpha))
    res2.config(text=''.join(bravo))

#Theme editors
def dark():
    root.configure(bg='#000000')
    L1.config(bg='#000000',fg='#FFFFFF')
    a1.config(bg='#000000',fg='#FFFFFF')
    L2.config(bg='#000000',fg='#FFFFFF')
    d1.config(bg='#000000',fg='#FFFFFF')
    L3.config(bg='#000000',fg='#FFFFFF')
    r1.config(bg='#000000',fg='#FFFFFF')
    butt.config(bg='#000000',fg='#FFFFFF')
    butt2.config(bg='#000000',fg='#FFFFFF')
    butt3.config(bg='#000000',fg='#FFFFFF')
    res.config(bg='#000000',fg='#FFFFFF')
    res2.config(bg='#000000',fg='#FFFFFF')

def light():
    root.configure(bg='#FFFFFF')
    L1.config(bg='#FFFFFF',fg='#000000')
    a1.config(bg='#FFFFFF',fg='#000000')
    L2.config(bg='#FFFFFF',fg='#000000')
    d1.config(bg='#FFFFFF',fg='#000000')
    L3.config(bg='#FFFFFF',fg='#000000')
    r1.config(bg='#FFFFFF',fg='#000000')
    butt.config(bg='#FFFFFF',fg='#000000')
    butt2.config(bg='#FFFFFF',fg='#000000')
    butt3.config(bg='#FFFFFF',fg='#000000')
    res.config(bg='#FFFFFF',fg='#000000')
    res2.config(bg='#FFFFFF',fg='#000000')

def sepia():
    root.configure(bg='#b8a88a')
    L1.config(bg='#b8a88a',fg='#000000')
    a1.config(bg='#b8a88a',fg='#000000')
    L2.config(bg='#b8a88a',fg='#000000')
    d1.config(bg='#b8a88a',fg='#000000')
    L3.config(bg='#b8a88a',fg='#000000')
    r1.config(bg='#b8a88a',fg='#000000')
    butt.config(bg='#b8a88a',fg='#000000')
    butt2.config(bg='#b8a88a',fg='#000000')
    butt3.config(bg='#b8a88a',fg='#000000')
    res.config(bg='#b8a88a',fg='#000000')
    res2.config(bg='#b8a88a',fg='#000000')

#Labels and entries
L1=tk.Label(root, text="Enter Attacking units:", font=("Arial", 16),bg='#FFFFFF',fg='#000000')
a1=tk.Entry(root,font=("Arial", 16),bg='#FFFFFF',fg='#000000')
L2=tk.Label(root, text="Enter Defending units:",font=("Arial", 16),bg='#FFFFFF',fg='#000000')
d1=tk.Entry(root,font=("Arial", 16))
L3=tk.Label(root, text="Enter rolls:", font=("Arial", 16),bg='#FFFFFF',fg='#000000')
r1=tk.Entry(root,font=("Arial", 16),bg='#FFFFFF',fg='#000000')
res=tk.Label(root, text="",font=("Arial", 16),bg='#FFFFFF',fg='#000000')
res2=tk.Label(root, text="",font=("Arial", 16),bg='#FFFFFF',fg='#000000')

#buttons
butt=tk.Button(root,text="Instant",font=("Arial", 14),bg='#FFFFFF',fg='#000000',command=lambda : clc(int(a1.get()),int(d1.get())))
butt2=tk.Button(root, text="One Roll",font=("Arial", 14),bg='#FFFFFF',fg='#000000', command=lambda : clc2(int(a1.get()), int(d1.get())))
butt3=tk.Button(root, text="Numbered Roll", font=("Arial", 14),bg='#FFFFFF',fg='#000000', command=lambda : clc3(int(a1.get()),int(d1.get()),int(r1.get())))
butt4=tk.Button(root, text="Dark Theme",font=("Arial",8),bg='#000000',fg='#FFFFFF',command=lambda : dark())
butt5=tk.Button(root, text="Light Theme",font=("Arial",8),bg='#000000',fg='#FFFFFF',command=lambda : light())
butt6=tk.Button(root, text="Sepia Theme", font=("Arial", 8),bg='#b8a88a',fg='#000000',command=lambda : sepia())

#placements for everything
L1.place(x=20, y=30)
a1.place(x=25, y=70)
L2.place(x=300, y=30)
d1.place(x=305, y=70)
L3.place(x=580, y=30)
r1.place(x=585,y=70)
butt.place(x=20, y=200)
butt2.place(x=325, y=200)
butt3.place(x=580,y=200)
butt4.place(x=900,y=30)
butt5.place(x=900,y=60)
butt6.place(x=900,y=90)
res.place(x=20, y=130)
res2.place(x=380, y=130)

#run window
root.mainloop()