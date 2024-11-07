from tkinter import *
root = Tk()

root.geometry("500x600")
root.title("Calculator By AI")
root.wm_iconbitmap("1.ico")
root.configure(background="light blue")

Scvalue = StringVar()
Scvalue.set(" ")
screen = Entry(root, textvar = Scvalue,font="Algerian 40 bold")
screen.pack(fill= X, ipadx=8, padx=10, pady=10)

f= Frame(root,bg="light blue")
b=Button(f,text="7",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="8",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="9",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
f.pack()


f= Frame(root,bg="light blue")
b=Button(f,text="4",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="5",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="6",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
f.pack()


f= Frame(root,bg="light blue")
b=Button(f,text="1",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="2",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
b=Button(f,text="3",font="Algerian 20 bold", padx=22, pady=28)
b.pack(side=LEFT)
f.pack()
root.mainloop()
