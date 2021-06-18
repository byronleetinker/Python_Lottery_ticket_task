# Byron Tinker. Class 1
# These are all my programming running in the background of my window.
from tkinter import *
from tkinter import messagebox
from validate_email import validate_email
import rsaidnumber
from datetime import date
from dateutil.relativedelta import relativedelta
import json

# Window size, title, whenever you can resize it and colour
window = Tk()
window.geometry("600x600")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"

# Defining my Welcome class for my window


class Welcome:
    def __init__(self, window):
        self.label = Label(window, text='Welcome!', bg='royalblue', font=("Arial", 20, "bold"))
        self.label.place(x=250, y=30)
        self.label2 = Label(window, text='Please enter your details.', bg='royalblue', font=("Arial", 20, "bold"))
        self.label2.place(x=160, y=80)
        self.name = Label(window, text='Name', bg='royalblue', font=("Arial", 12, "bold"))
        self.name.place(x=280, y=150)
        self.name_entry = Entry(window)
        self.name_entry.place(x=220, y=180)
        self.number = Label(window, text='Phone Number', bg='royalblue', font=("Arial", 12, "bold"))
        self.number.place(x=250, y=230)
        self.number_entry = Entry(window)
        self.number_entry.place(x=220, y=260)
        self.email = Label(window, text='Email Address', bg='royalblue', font=("Arial", 12, "bold"))
        self.email.place(x=250, y=310)
        self.email_entry = Entry(window)
        self.email_entry.place(x=220, y=340)
        self.id = Label(window, text='ID Number', bg='royalblue', font=("Arial", 12, "bold"))
        self.id.place(x=260, y=390)
        self.id_entry = Entry(window)
        self.id_entry.place(x=220, y=420)
        self.verify = Button(window, text='Verify', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                             command=self.verify)
        self.verify.place(x=50, y=500)
        self.delete = Button(window, text='Clear', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                             command=self.delete)
        self.delete.place(x=270, y=500)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=500, y=500)
        player_entry = self.name_entry.get().strip() + self.id_entry.get()[:2]
        print(player_entry)

    def age_validation(self):
        ID = rsaidnumber.parse(self.id_entry.get())
        birthdate = ID.date_of_birth
        age = relativedelta(date.today(), birthdate.date())
        age = age.years

        if age >= 18:
            age = str(age)
            messagebox.showinfo("You are " + age + " years old", "You may begin playing")
            window.destroy()
            import play

        elif age <= 18:
            age = str(age)
            messagebox.showerror("Sorry, You are " + age + " years old", "You are too young too play")

    def add_files(self, text_add_files):
        print(text_add_files)
        text_add_files = json.dumps(text_add_files)
        with open("login.txt", "a+") as login_file:
            login_file.write(text_add_files)

    def verify(self):
        Name = self.name_entry.get()
        Number = self.number_entry.get()
        Email = self.email_entry.get()
        ID = self.id_entry.get()

        if Name == " ":
            messagebox.showerror("Error", "Please enter valid details")

        elif len(Number) != 10:
            messagebox.showerror("Error", "Please enter correct phone number")

        elif Email == " ":
            messagebox.showerror("Error", "Please enter the correct email address")

        elif not validate_email(Email):
            messagebox.showerror("Error", "Please enter the correct email address")

        if len(ID) != 13:
            messagebox.showerror("Error", "Please enter correct ID number")
            ID = rsaidnumber.parse(ID)
            ID.valid
        else:
            self.age_validation()

            # self.age_validation(ID)
            player = {
                "Name": Name,
                "Phone number": Number,
                "Email": Email,
                "ID number": str(ID)
            }
            self.add_files(player)

    def delete(self):
        self.name_entry.delete(0, END)
        self.number_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.id_entry.delete(0, END)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()

# Reference what should be displayed on the window
obj = Welcome(window)
# Without this the window will not stop running resulting in no results being displayed
window.mainloop()
