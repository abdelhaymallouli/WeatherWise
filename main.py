from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

from gui_elements import create_gui_elements
from weather import get_weather

# Initialize the main window
root = Tk()
root.title("WeatherWise")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Create and place GUI elements
textfield, clock, name, labels = create_gui_elements(root, get_weather)

root.mainloop()
