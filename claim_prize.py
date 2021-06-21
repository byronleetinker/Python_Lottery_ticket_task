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


# Defining my Claim class for my window includes labels, entries, buttons and their placements.
# These are defined by the names, size, fonts and even colours.
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

    # Defining the adding the information to the bank file.
    def add_files(self, add_files):
        print(add_files)
        add_files = json.dumps(add_files)
        with open("bank.txt", "a+") as bank_file:
            bank_file.write(add_files)

    # Defining the function verification that insures all entries are filled and once all information is correctly inserted an email will be sent.
    def verify(self):
        Name = self.account_name_entry.get()
        Number = self.account_number_entry.get()

        if Name == " ":
            messagebox.showerror("Error", "Please enter valid details")

        elif len(Number) != 16:
            messagebox.showerror("Error", "Please enter correct bank account number")

        player = {
            "Account Holder Name": Name,
            "Bank Account Number": Number,
        }
        self.add_files(player)

    def verify(self):
        # Sender's email
        sender_email_id = 'lottobyrontinker@gmail.com'
        # Receiver's email
        receiver_email_id = self.confirm_email_entry.get()
        # Password for sender's email
        password = 'lottobyron'
        subject = "Lottery Ticket"
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = receiver_email_id
        msg['Subject'] = subject
        body = "Congratulations\n"
        body = body + "You have claimed your prize. Enjoy your day."
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(sender_email_id, password)
        # message to be sent

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, text)
        # terminating the session
        s.quit()
        messagebox.showinfo("Alert!", "Please check your emails for further information regarding your prize")
        window.destroy()

    # Defining the function convertor which takes you to the next window which will be the Currency Convertor.

    def convertor(self):
        msg_box = messagebox.askquestion("Currency Convertor", "Are you sure you want to convert your currency?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
            import convertor

    # Defining the exit function making sure that you really want to exit the program and
    # if you do it will close the program
    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        # If the player wants to exit the program, it will display this message and the window will close.
        if msg_box == "yes":
            messagebox.showinfo("Goodbye", "You are now exiting the program, Thank you for playing!")
            window.destroy()


# Reference what should be displayed on the window
obj = Claim(window)
# Without this the window will not stop running resulting in no results being displayed
window.mainloop()
