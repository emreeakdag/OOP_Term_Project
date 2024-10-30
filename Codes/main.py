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
    def __init__(self, name, surname, email, gender, username, pasword):
        super().__init__(username, pasword)
        self.name = name
        self.surname = surname
        self.email = email
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
from tkinter.ttk import Combobox

window = Tk()
window.title("Taxi Booking")
window.geometry("500x500")


def login_panel():
    hide_all()
    login_frame.place(x=0, y=0, width=500, height=500)
    lgn_main.place(x=180, y=50)
    lgn_name_lbl.place(x=50, y=150)
    lgn_name_ent.place(x=120, y=150)
    lgn_pasword_lbl.place(x=50, y=180)
    lgn_pasword_ent.place(x=120, y=180)

    login_button.place(x=300, y=350, width=100, height=50)
    lgn_signup_btn.place(x=100, y=350, width=100, height=50)
    lgn_exit_btn.place(x=225, y=425, width=50, height=50)


def hide_all():
    for frame in (login_frame, register_frame, menu_frame, taxi_call_frame, progress_frame):
        frame.place_forget()


def register_panel():
    hide_all()
    register_frame.place(x=0, y=0, width=500, height=500)
    register_main.place(x=200, y=50)
    rgs_name_lbl.place(x=125,y=150)
    rgs_name_ent.place(x=195, y=150)
    rgs_surname_lbl.place(x=125, y=180)
    rgs_surname_ent.place(x=195, y=180)
    rgs_username_lbl.place(x=125, y=210)
    rgs_username_ent.place(x=195, y=210)
    rgs_email_lbl.place(x=125, y=240)
    rgs_email_ent.place(x=195, y=240)
    rgs_genders_lbl.place(x=125, y=270)
    rgs_genders_cmbx.place(x=195, y=270)

    back_login_btn.place(x=100, y=350, width=100, height=50)
    rgs_signup_btn.place(x=300, y=350, width=100, height=50)


def menu_panel():
    hide_all()
    menu_frame.place(x=0, y=0, width=500, height=500)
    menu_main.place(x=210, y=50)
    menu_call_taxi_btn.place(x=200, y=125, width=100, height=50)
    menu_progress_btn.place(x=200, y=200, width=100, height=50)
    menu_logout_btn.place(x=200, y=275, width=100, height=50)


def taxi_call_panel():
    hide_all()
    taxi_call_frame.place(x=0, y=0, width=500, height=500)
    taxi_call_main.place(x=180, y=100)
    back_from_call_taxi_btn.place(x=200, y=450)


def progress_panel():
    hide_all()
    progress_frame.place(x=0, y=0, width=500, height=500)
    progress_main.place(x=180, y=100)
    back_from_progress_btn.place(x=200, y=450)


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
lgn_main = Label(login_frame, text="Welcome to Taxi Booking")
login_button = Button(login_frame, text="Login", command=menu_panel)
lgn_name_lbl = Label(login_frame, text="Username")
lgn_name_ent = Entry(login_frame)
lgn_pasword_lbl = Label(login_frame, text="Pasword")
lgn_pasword_ent = Entry(login_frame)
lgn_exit_btn = Button(login_frame, text="Exit", command=window.destroy)
lgn_signup_btn = Button(login_frame, text="Sign Up", command=register_panel, bg="gray")

# Register Panel Widgets
# rgs = register
back_login_btn = Button(register_frame, text="Back Login", command=login_panel)
rgs_name_lbl = Label(register_frame, text="Name")
rgs_name_ent = Entry(register_frame)
rgs_surname_lbl = Label(register_frame, text="Surname")
rgs_surname_ent = Entry(register_frame)
rgs_username_lbl = Label(register_frame, text="Username")
rgs_username_ent = Entry(register_frame)
rgs_email_lbl = Label(register_frame, text="E-mail")
rgs_email_ent = Entry(register_frame)

rgs_genders_lbl = Label(register_frame, text="Gender")
genders = ["Man", "Woman"]
rgs_genders_cmbx= Combobox(register_frame, values=genders)

rgs_signup_btn = Button(register_frame, text="Sign Up", command=login_panel)


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