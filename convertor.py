from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("600x600")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"


class Convertor:
    def __init__(self, window):
        self.label = Label(window, text='Currency Convertor.', bg='royalblue', font=("Arial", 20, "bold"))
        self.label.place(x=170, y=50)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=500, y=500)

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Convertor(window)
window.mainloop()