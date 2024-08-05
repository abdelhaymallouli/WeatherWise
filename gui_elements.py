from tkinter import *
import tkinter as tk
from tkinter import messagebox

def create_gui_elements(root, get_weather):
    # Keeping references to the images
    global search_image, search_icon, logo_image, frame_image
    
    # Research box - 
    try:
        search_image = PhotoImage(file="images/search.png")
        search_label = Label(image=search_image)
        search_label.place(x=20, y=20)  # Adjust the placement as needed
    except Exception as e:
        messagebox.showerror("Error", f"Image not found: {e}")

    # Text field for city input
    textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
    textfield.place(x=50, y=40)
    textfield.focus()

    # Search icon button
    try:
        search_icon = PhotoImage(file="images/search-icon.png")
        myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=lambda: get_weather(textfield.get(), textfield, clock, name, labels))
        myimage_icon.place(x=400, y=34)
    except Exception as e:
        messagebox.showerror("Error", f"Search icon image not found: {e}")

    # Logo image
    try:
        logo_image = PhotoImage(file="images/logo.png")
        logo = Label(image=logo_image)
        logo.place(x=150, y=100)
    except Exception as e:
        messagebox.showerror("Error", f"Logo image not found: {e}")

    # Bottom Box
    try:
        frame_image = PhotoImage(file="images/box.png")
        frame_myimage = Label(image=frame_image)
        frame_myimage.pack(padx=5, pady=5, side=BOTTOM)
    except Exception as e:
        messagebox.showerror("Error", f"Frame image not found: {e}")

    # Labels
    label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label1.place(x=120, y=400)

    label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label2.place(x=250, y=400)

    label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label3.place(x=430, y=400)

    label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
    label4.place(x=650, y=400)

    w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    w.place(x=120, y=430)
    h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    h.place(x=280, y=430)
    d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    d.place(x=450, y=430)
    p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
    p.place(x=670, y=430)

    # Time
    name = Label(root, font=("arial", 15, "bold"))
    name.place(x=30, y=100)
    clock = Label(root, font=("Helvetica", 20))
    clock.place(x=30, y=130)

    labels = {
        "wind": w,
        "humidity": h,
        "description": d,
        "pressure": p
    }

    return textfield, clock, name, labels

