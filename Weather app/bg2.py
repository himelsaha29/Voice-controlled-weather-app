from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = "C:\\Users\\HimelSaha\\Pictures\\Saved Pictures\\03aorrcx9lm21.png"
WIDTH, HEIGHT = 953, 500

root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGHT))

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
titles = tk.Label(root, bg='yellow', text="title")
button_window = canvas.create_window(WIDTH / 2, HEIGHT / 2, anchor=tk.CENTER, window=titles)

root.mainloop()