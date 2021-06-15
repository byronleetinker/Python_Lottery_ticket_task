from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x600")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"
variable = StringVar(window)


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
        self.account_number.place(x=30, y=250)
        self.account_number_entry = Entry(window)
        self.account_number_entry.place(x=250, y=250)
        self.bank = Label(window, text='Select your Bank: ', bg='royalblue', font=("Arial", 15))
        self.bank.place(x=30, y=350)
        self.optmenu = OptionMenu(window, variable, "ABSA Bank", "Capetic Bank", "FNB", "Nedbank", "Standard Bank")
        self.optmenu.place(x=250, y=350, width=170)
        self.verify = Button(window, text='Verify', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"))
        self.verify.place(x=50, y=500)
        self.convert = Button(window, text='Currency Convertor', bg='lightgreen', borderwidth=5,
                              font=("Arial", 12, "bold"), command=self.convertor)
        self.convert.place(x=230, y=500)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=500, y=500)

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
            window.destroy()


obj = Claim(window)
window.mainloop()
