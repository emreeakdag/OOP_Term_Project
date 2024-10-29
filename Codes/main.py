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
    hide_All()
    login_frame.pack()
    back_login_btn.pack_forget()
    register_name.pack_forget()

def hide_All():
    login_frame.pack_forget()

def show_Register_Panel():
    hide_All()
    register_frame.pack()
    back_login_btn.pack()
    register_name.pack()

# Frame Tanımlamaları
login_frame = Frame(window)
register_frame = Frame(window)

# Widget Tanımlamaları
label = Label(login_frame, text="Kullanıcı Adı:")
entry = Entry(login_frame)
login_button = Button(login_frame, text="Giriş Yap")
login_button.place(x=100,y=100)
register_btn = Button(login_frame, text="Kayit Ol" , command=show_Register_Panel)
register_name = Label(register_frame, text="Siüü")
back_login_btn = Button(register_frame,text="Back Login", command=login_panel)

# Frame Göster
login_frame.pack()
register_frame.pack()

# Widget Göster
label.pack()
entry.pack()
login_button.pack()
register_btn.pack()

login_panel()

window.mainloop()