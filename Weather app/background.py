from tkinter import *
from tkinter import messagebox
top = Tk(className="bg")

#C = Canvas(top, bg="blue", height=500, width=953)
#filename = PhotoImage(file = "C:\\Users\\HimelSaha\\Pictures\\Saved Pictures\\03aorrcx9lm21.png")
#background_label = Label(top, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

#C.pack()
top.geometry("953x500")
titles = Label(top, bg='yellow', text="\n\ntitle")
titles.configure(font=("Lucida Console", 15, "bold"))
titles.pack()
top.configure(background="yellow")
top.mainloop()