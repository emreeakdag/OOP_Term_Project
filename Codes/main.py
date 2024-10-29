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

window = Tk()
window.title("Taxi Booking")
window.geometry("500x500")


def login_panel():
    hide_all()
    login_frame.grid(row=0, column=0, sticky="nsew")
    lgn_main.grid(row=0, column=0, columnspan=2)
    lgn_name_lbl.grid(row=1, column=0, sticky="w")
    lgn_name_ent.grid(row=1, column=1)
    login_button.grid(row=2, column=0, columnspan=2)
    register_btn.grid(row=3, column=0)
    lgn_exit_btn.grid(row=4, column=4, columnspan=2)


def hide_all():
    for frame in (login_frame, register_frame, menu_frame, taxi_call_frame, progress_frame):
        frame.grid_forget()


def register_panel():
    hide_all()
    register_frame.grid(row=0, column=0, sticky="nsew")
    register_main.grid(row=0, column=0, columnspan=2)
    back_login_btn.grid(row=1, column=0)
    # ... rest of register panel widgets with grid


def menu_panel():
    hide_all()
    menu_frame.grid(row=0, column=0, sticky="nsew")
    menu_main.grid(row=0, column=0, columnspan=2)
    menu_call_taxi_btn.grid(row=1, column=0)
    menu_progress_btn.grid(row=1, column=1)
    
    menu_logout_btn.grid(row=1, column=2)


def taxi_call_panel():
    hide_all()
    taxi_call_frame.grid(row=0, column=0, sticky="nsew")
    taxi_call_main.grid(row=0, column=0, columnspan=2)
    back_from_call_taxi_btn.grid(row=1, column=0, columnspan=2)


def progress_panel():
    hide_all()
    progress_frame.grid(row=0, column=0, sticky="nsew")
    progress_main.grid(row=0, column=0, columnspan=2)
    back_from_progress_btn.grid(row=1, column=0, columnspan=2)


# Frame Definitions
login_frame = Frame(window)
register_frame = Frame(window)
menu_frame = Frame(window)
taxi_call_frame = Frame(window)
progress_frame = Frame(window)

# Widget Definitions

register_main = Label(register_frame, text="Register Panel")
menu_main = Label(menu_frame, text="Menu Panel")
taxi_call_main = Label(taxi_call_frame, text="Taxi Call Panel")
progress_main = Label(progress_frame, text="In Progress Panel")

# Login Panel Widgets
lgn_main = Label(login_frame, text="Login Panel")
login_button = Button(login_frame, text="Login", command=menu_panel)
lgn_name_lbl = Label(login_frame, text="Username")
lgn_name_ent = Entry(login_frame)
lgn_exit_btn = Button(login_frame, text="Exit", command=window.destroy)

# Register Panel Widgets (add grid definition for remaining widgets)
register_btn = Button(login_frame, text="Register", command=register_panel, bg="gray")
back_login_btn = Button(register_frame, text="Back Login", command=login_panel)

# Menu Panel Widgets
menu_call_taxi_btn = Button(menu_frame, text="Call a Taxi", command=taxi_call_panel)
menu_progress_btn = Button(menu_frame, text="In Progress", command=progress_panel)
menu_logout_btn = Button(menu_frame, text="Log Out", command=login_panel)


# Call Taxi Widgets
back_from_call_taxi_btn = Button(taxi_call_frame, text="Back to Menu", command=menu_panel)

# In Progress Panel
back_from_progress_btn = Button(progress_frame, text="Back to Menu", command=menu_panel)


# Initial Panel Display
login_panel()

window.mainloop()