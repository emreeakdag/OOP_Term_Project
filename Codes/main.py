from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import sqlite3


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password


class Customer(User):
    def __init__(self, name, surname, email, gender, username, password):
        super().__init__(username, password)
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender


class Welcome:
    @staticmethod
    def get_welcome_message():
        return "Welcome to Taxi Booking"

    @staticmethod
    def get_welcome_message(name):  # Overload metot örneği
        return f"Welcome to Taxi Booking, {name}!"


class Taxi:
    def __init__(self, brand, model, plate, capacity):
        self.brand = brand
        self.model = model
        self.plate = plate
        self.capacity = capacity


class Sedan(Taxi):
    def __init__(self, brand, model, plate, capacity):
        super().__init__(brand, model, plate, capacity)

    def acceleration_time(self):
        return "0-100 km/h: 8 seconds"


class SUV(Taxi):
    def __init__(self, brand, model, plate, capacity):
        super().__init__(brand, model, plate, capacity)

    def acceleration_time(self):
        return "0-100 km/h: 9 seconds"


class Hatchback(Taxi):
    def __init__(self, brand, model, plate, capacity):
        super().__init__(brand, model, plate, capacity)

    def acceleration_time(self):
        return "0-100 km/h: 7 seconds"


# Database Setup
conn = sqlite3.connect("taxi_booking.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    gender TEXT,
    username TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
)
""")
conn.commit()

# Vehicles
vehicles = {
    "Sedan": [
        Sedan("Toyota", "Camry", "01EM396", 5),
        Sedan("Honda", "Accord", "34ABC123", 5)
    ],
    "SUV": [
        SUV("Nissan", "X-Trail", "06DEF789", 7),
        SUV("Ford", "Explorer", "07GHI012", 7)
    ],
    "Hatchback": [
        Hatchback("Volkswagen", "Golf", "01EA01", 5),
        Hatchback("Ford", "Fiesta", "34DEF34", 5)
    ]
}

# Functions

def register_user():
    name = rgs_name_ent.get()
    surname = rgs_surname_ent.get()
    email = rgs_email_ent.get()
    gender = rgs_genders_cmbx.get()
    username = rgs_username_ent.get()
    password = rgs_password_ent.get()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        cursor.execute("INSERT INTO customers (name, surname, email, gender, username) VALUES (?, ?, ?, ?, ?)",
                       (name, surname, email, gender, username))
        conn.commit()

        print("Kayıt başarılı!")
        rgs_name_ent.delete(0, END)
        rgs_surname_ent.delete(0, END)
        rgs_username_ent.delete(0, END)
        rgs_password_ent.delete(0, END)
        rgs_email_ent.delete(0, END)
        rgs_genders_cmbx.set("")

    except sqlite3.IntegrityError:
        print("Bu kullanıcı adı zaten kullanılıyor. Başka bir kullanıcı adı deneyin.")


def show_vehicle_details(vehicle):
    details = (
        f"Brand : {vehicle.brand}\n"
        f"Model : {vehicle.model}\n"
        f"Plate : {vehicle.plate}\n"
        f"Capacity : {vehicle.capacity}\n"
        f"{vehicle.acceleration_time()}"
    )
    txc_details_label.config(text=details)
    return details


def update_model_combobox(event):
    selected_type = txc_type_combobox.get()
    txc_model_combobox['values'] = [f"{v.brand} {v.model}" for v in vehicles[selected_type]]
    txc_model_combobox.set("")


def on_model_select(event):
    selected_type = txc_type_combobox.get()
    selected_model = txc_model_combobox.get()
    for vehicle in vehicles[selected_type]:
        if f"{vehicle.brand} {vehicle.model}" == selected_model:
            show_vehicle_details(vehicle)
            break


def call_taxi():
    selected_type = txc_type_combobox.get()
    selected_model = txc_model_combobox.get()

    if selected_type and selected_model:
        for vehicle in vehicles[selected_type]:
            if f"{vehicle.brand} {vehicle.model}" == selected_model:
                details = show_vehicle_details(vehicle)  # Get the details of the selected vehicle
                progress_current_taxi_label.config(text=details)  # Update progress panel with vehicle details
                progress_panel()  # Navigate to the In Progress panel
                break
    else:
        print("Lütfen bir araç türü ve modeli seçin.")

        
def login_user():
    username = lgn_name_ent.get()
    password = lgn_password_ent.get()

    if not username or not password:
        print("Kullanıcı adı ve şifre boş olamaz.")
        return

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Giriş başarılı!")
        menu_panel()
    else:
        print("Kullanıcı adı veya şifre yanlış.")


def login_panel():
    hide_all()
    login_frame.place(x=0, y=0, width=500, height=500)
    lgn_main.config(text=Welcome.get_welcome_message("User"))  # Overloaded method çağrısı
    lgn_main.place(x=180, y=50)
    lgn_name_lbl.place(x=50, y=150)
    lgn_name_ent.place(x=120, y=150)
    lgn_password_lbl.place(x=50, y=180)
    lgn_password_ent.place(x=120, y=180)
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
    rgs_name_lbl.place(x=125, y=150)
    rgs_name_ent.place(x=195, y=150)
    rgs_surname_lbl.place(x=125, y=180)
    rgs_surname_ent.place(x=195, y=180)
    rgs_username_lbl.place(x=125, y=210)
    rgs_username_ent.place(x=195, y=210)
    rgs_password_lbl.place(x=125, y=240)
    rgs_password_ent.place(x=195, y=240)
    rgs_email_lbl.place(x=125, y=270)
    rgs_email_ent.place(x=195, y=270)
    rgs_genders_lbl.place(x=125, y=300)
    rgs_genders_cmbx.place(x=195, y=300)
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
    txc_main.place(x=210, y=50)
    txc_type_lbl.place(x=100, y=150)
    txc_type_combobox.place(x=170, y=150, width=150, height=30)
    txc_model_lbl.place(x=100, y=200)
    txc_model_combobox.place(x=170, y=200, width=150, height=30)
    txc_details_label.place(x=170, y=250)
    txc_call_taxi_btn.place(x=200, y=380)
    back_from_txc_btn.place(x=200, y=450)


def progress_panel():
    hide_all()
    progress_frame.place(x=0, y=0, width=500, height=500)
    progress_main.place(x=180, y=100)
    progress_current_taxi_label.place(x=50, y=150)
    back_from_progress_btn.place(x=200, y=450)

# UI Setup
window = Tk()
window.title("Taxi Booking")
window.geometry("500x500")

# Frame Definitions
login_frame = Frame(window)
register_frame = Frame(window)
menu_frame = Frame(window)
taxi_call_frame = Frame(window)
progress_frame = Frame(window)

# Widget Definitions
lgn_main = Label(login_frame, text="")
login_button = Button(login_frame, text="Login", command=login_user)
lgn_name_lbl = Label(login_frame, text="Username")
lgn_name_ent = Entry(login_frame)
lgn_password_lbl = Label(login_frame, text="Password")
lgn_password_ent = Entry(login_frame, show="*")
lgn_exit_btn = Button(login_frame, text="Exit", command=window.destroy)
lgn_signup_btn = Button(login_frame, text="Sign Up", command=register_panel, bg="gray")

register_main = Label(register_frame, text="Register Panel")
menu_main = Label(menu_frame, text="Menu Panel")
progress_main = Label(progress_frame, text="In Progress Panel")

back_login_btn = Button(register_frame, text="Back Login", command=login_panel)
rgs_name_lbl = Label(register_frame, text="Name")
rgs_name_ent = Entry(register_frame)
rgs_surname_lbl = Label(register_frame, text="Surname")
rgs_surname_ent = Entry(register_frame)
rgs_username_lbl = Label(register_frame, text="Username")
rgs_username_ent = Entry(register_frame)
rgs_password_lbl = Label(register_frame, text="Password")
rgs_password_ent = Entry(register_frame)
rgs_email_lbl = Label(register_frame, text="E-mail")
rgs_email_ent = Entry(register_frame)
rgs_genders_lbl = Label(register_frame, text="Gender")
genders = ["Man", "Woman"]
rgs_genders_cmbx = Combobox(register_frame, values=genders)
rgs_signup_btn = Button(register_frame, text="Sign Up", command=register_user)

menu_call_taxi_btn = Button(menu_frame, text="Call a Taxi", command=taxi_call_panel)
menu_progress_btn = Button(menu_frame, text="In Progress", command=progress_panel)
menu_logout_btn = Button(menu_frame, text="Log Out", command=login_panel)

txc_main = Label(taxi_call_frame, text="Taxi Call Panel")
txc_type_lbl = Label(taxi_call_frame, text="Car Type")
txc_model_lbl = Label(taxi_call_frame, text="Car Model")
txc_type_combobox = ttk.Combobox(taxi_call_frame, values=list(vehicles.keys()), state="readonly")
txc_type_combobox.bind("<<ComboboxSelected>>", update_model_combobox)
txc_model_combobox = ttk.Combobox(taxi_call_frame, state="readonly")
txc_model_combobox.bind("<<ComboboxSelected>>", on_model_select)
txc_details_label = Label(taxi_call_frame, text="", anchor="nw", justify="left")
txc_call_taxi_btn = Button(taxi_call_frame, text="Call", command=call_taxi)
back_from_txc_btn = Button(taxi_call_frame, text="Back to Menu", command=menu_panel)

progress_current_taxi_label = Label(progress_frame, text="", anchor="nw", justify="left")
back_from_progress_btn = Button(progress_frame, text="Back to Menu", command=menu_panel)

# Initial Panel
login_panel()
window.mainloop()
