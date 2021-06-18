# These are all my programming running in the background of my window.
from tkinter import *
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json

# Window size, title, whenever you can resize it and colour
window = Tk()
window.geometry("600x600")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"
variable = StringVar(window)

# Defining my Claim class for my window
class Claim:
    result = StringVar()
    variable.set("Select your choice")

    def __init__(self, window):
        self.label = Label(window, text='Congratulations!', bg='royalblue', font=("Arial", 20, "bold"))
        self.label.place(x=200, y=50)
        self.account_name = Label(window, text='Account Holder Name: ', bg='royalblue', font=("Arial", 15))
        self.account_name.place(x=30, y=150)
        self.account_name_entry = Entry(window)
        self.account_name_entry.place(x=250, y=150)
        self.account_number = Label(window, text='Bank Account Number: ', bg='royalblue', font=("Arial", 15))
        self.account_number.place(x=30, y=230)
        self.account_number_entry = Entry(window)
        self.account_number_entry.place(x=250, y=230)
        self.bank = Label(window, text='Select your Bank: ', bg='royalblue', font=("Arial", 15))
        self.bank.place(x=30, y=300)
        self.optmenu = OptionMenu(window, variable, "ABSA Bank", "Capetic Bank", "FNB", "Nedbank", "Standard Bank")
        self.optmenu.place(x=250, y=300, width=170)
        self.confirm_email = Label(window, text='Confirm email address: ', bg='royalblue', font=("Arial", 15))
        self.confirm_email.place(x=30, y=400)
        self.confirm_email_entry = Entry(window)
        self.confirm_email_entry.place(x=250, y=400)
        self.verify = Button(window, text='Verify', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                             command=self.verify)
        self.verify.place(x=50, y=500)
        self.convert = Button(window, text='Currency Convertor', bg='lightgreen', borderwidth=5,
                              font=("Arial", 12, "bold"), command=self.convertor)
        self.convert.place(x=230, y=500)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=500, y=500)

    def add_files(self, add_files):
        print(add_files)
        add_files = json.dumps(add_files)
        with open("bank.txt", "a+") as bank_file:
            bank_file.write(add_files)

    def verify(self):
        Name = self.account_name_entry.get()
        Number = self.account_number_entry.get()
        Bank = self.optmenu.getboolean()

        if Name == " " or Number == " ":
            messagebox.showerror("Error", "Please enter valid details")

        player = {
            "Account Holder Name": Name,
            "Bank Account Number": Number,
            "Bank": Bank
        }
        self.add_files(player)

        try:
            sender_email_id = 'lottobyrontinker@gmail.com'

            receiver_email_id = (self.confirm_email_entry.get())

            password = 'lottobyron'

            subject = "Greetings"
            msg = MIMEMultipart()
            msg['From'] = sender_email_id
            msg['To'] = ','.join(receiver_email_id)
            msg['Subject'] = subject

            body = "Congratulations.\n"
            body = body + "You have claim your prize. Have a nice day."

            msg.attach(MIMEText(body, 'plain'))
            text = msg.as_string()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()

            s.login(sender_email_id, password)

            s.sendmail(sender_email_id, receiver_email_id, text)

        except:
            messagebox.showinfo("Alert!", "Please check your emails for further information regarding your prize")
            window.destroy()

    def convertor(self):
        msg_box = messagebox.askquestion("Currency Convertor", "Are you sure you want to convert your currency?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
            import convertor

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            messagebox.showinfo("Goodbye", "You are now exiting the program, Thank you for playing!")
            window.destroy()

# Reference what should be displayed on the window
obj = Claim(window)
# Without this the window will not stop running resulting in no results being displayed
window.mainloop()
