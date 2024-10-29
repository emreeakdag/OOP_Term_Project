class user:
    def __init__(self,username,pasword):
        self.__username = username
        self.__pasword = pasword

    def get_username(self):
        return self.__username
    
    def set_username(self, new_username):
        self.__username = new_username

    def get_pasword(self):
        return self.__pasword
    
    def set_pasword(self, new_pasword):
        self.__pasword = new_pasword


class customer(user):
    def __init__(self, name, surname, gender, username, pasword):
        super().__init__(username, pasword)
        self.name = name
        self.surname = surname
        self.gender = gender


class Taxi:
    def __init__(self, brand, model,plate,capacity):
        self.brand = brand
        self.model = model
        self.plate = plate
        self.capacity = capacity


class Sedan(Taxi):
    def __init__(self, brand, model, plate, capacity):
        super().__init__(brand, model, plate, capacity= 4)

    def acceleration_time(self):
        return "0-100 km/h: 8 seconds"
    

class SUV(Taxi):
    def __init__(self, brand,model, plate, capacity):
        super().__init__(self, brand, model, plate, capacity= 6)

    def acceleration_time(self):
        return "0-100 km/h: 9 seconds"
    

class Hatchback(Taxi):
    def __init__(self, brand, model, plate, capacity):
        super().__init__(self, brand, model, plate, capacity= 5)
    
    def acceleration_time(self):
        return "0-100 km/h: 7 seconds"
    



#-----------------------------------------


from tkinter import *
import tkinter as tk


window = tk.Tk()
window.title("Taxi Booking")
window.geometry("500x500")

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)



#frame1 = tk.Frame(window, borderwidth=2, relief="groove")
#frame1.grid(row=0, column=0, padx=10, pady=10)




def login_panel():
    login_label = tk.Label(frame1, text="This is Login Panel")
    tk.Label(window, text="User Name:").place(x= 7, y=50)
    username_entry = tk.Entry(window)
    username_entry.place(x= 80, y=50)
    username_entry.pack_forget()

    tk.Label(window, text="Pasword:").place(x=22, y=80)
    pasword_entry = tk.Entry(window)
    pasword_entry.place(x=80, y=80) 

    frame1.pack()
    frame2.pack_forget()


def register_panel():


    tk.Label(window, text="word:").place(x=22, y=80)
    pasword_entry = tk.Entry(window)
    pasword_entry.place(x=80, y=80)


    frame2.pack()
    frame1.pack_forget()

register_panel_button = tk.Button(frame2, text="Register")

login_panel_button = tk.Button(frame1, text="Login", command=lambda: register_panel)
login_panel_button.pack()

back_login_button = tk.Button(frame2, text="Back Login", command=lambda: login_panel)



login_panel()
register_panel()

window.mainloop()

