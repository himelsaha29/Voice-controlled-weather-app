import tkinter as tk
from voice import *
from ui import *


windows = tk.Tk(className='WeatherApp')
windows.geometry("953x500")

ui(windows)
windows.mainloop()