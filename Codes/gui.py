from tkinter import *
from tkinter import ttk
import tkinter as tk







window = tk.Tk()
window.title("Taxi Booking")
window.geometry("400x400+550+150")


# Frame fonksiyonunu kullanarak çerçeve oluşturacağız. Her frame bir sayfayı temsil edecek

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)

def go_to_page1():
    frame1.pack() # pack fonksiyonu pencereye ekleyerek görünür hale gelmesini sağlar
    frame2.pack_forget()


def go_to_page2():
    frame1.pack_forget()
    frame2.pack()
    

login_label = tk.Label(frame1, text="Login Panel")
login_label.pack()

register_label = tk.Label(frame2, text="Register Panel")
register_label.pack()


register_panel_button = tk.Button(window, text="Register", command=go_to_page2)

login_panel_button = tk.Button(window, text="Back to Login Panel", command=go_to_page1)



frame1.pack()

login_panel_button.pack()
register_panel_button.pack()


window.mainloop()
