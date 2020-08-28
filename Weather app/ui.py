import tkinter as tk
from voice import *
import threading


class ui:
    def __init__(self, window):
        self.window = window

        def thrd1():
            title = tk.Label(master=self.window, text="")
            title.configure(font=("DejaVu Sans", 15, "bold"))
            title.pack()
        t = threading.Thread(target=thrd1)
        #t.start()

        def thrd2():
            window.withdraw()
            toplevel = tk.Toplevel(self.window)  # close the first window
            toplevel.geometry("953x500")
            voice(toplevel)

        p = threading.Thread(target=thrd2)
        p.start()