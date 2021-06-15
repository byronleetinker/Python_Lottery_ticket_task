from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("1000x500")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"


class Play:
    def __init__(self, window):
        self.lotto_list = []
        self.player = Label(window, text='Player Number: ', bg='royalblue', font=("Arial", 12, "bold"))
        self.player.place(x=10, y=20)
        self.player_entry = Entry(window, bg='royalblue', state='readonly')
        self.player_entry.place(x=140, y=20)
        self.info = Label(window, text='Please choose 6 numbers from ranging from 1 to 46.', bg='royalblue',
                          font=("Arial", 12, "bold"))
        self.info.place(x=10, y=140)
        self.results = Label(window, text='Results.', bg='royalblue', font=("Arial", 12, "bold"))
        self.results.place(x=730, y=140)
        self.number_entry = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry.place(x=30, y=190)
        self.number_entry2 = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry2.place(x=90, y=190)
        self.number_entry3 = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry3.place(x=150, y=190)
        self.number_entry4 = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry4.place(x=210, y=190)
        self.number_entry5 = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry5.place(x=270, y=190)
        self.number_entry6 = Text(window, width=3, height=2, font=("Arial", 20, "bold"))
        self.number_entry6.place(x=330, y=190)
        self.number_entry7 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry7.place(x=600, y=190)
        self.number_entry8 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry8.place(x=660, y=190)
        self.number_entry9 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry9.place(x=720, y=190)
        self.number_entry10 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry10.place(x=780, y=190)
        self.number_entry11 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry11.place(x=840, y=190)
        self.number_entry12 = Text(window, width=3, height=2, font=("Arial", 20, "bold"), state='disabled')
        self.number_entry12.place(x=900, y=190)
        self.play = Button(window, text='Play', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"), command=self.lotto_numbers)
        self.play.place(x=170, y=300)
        self.play_again = Button(window, text='Play again', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"))
        self.play_again.place(x=145, y=380)
        self.claim = Button(window, text='Claim Prize', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                            command=self.claim_prize)
        self.claim.place(x=700, y=300)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=730, y=380)

    def lotto_numbers(self):
        lotto = []
        while len(lotto) < 6:
            number = random.randint(1, 49)
            lotto.append(number)
        print(lotto[0])

        self.number_entry7.configure(state=NORMAL)
        self.number_entry7.insert(0, lotto[0])
        self.number_entry8.config(state='normal')
        self.number_entry8.insert(0, lotto[1])
        self.number_entry9.config(state='normal')
        self.number_entry9.insert(0, lotto[2])
        self.number_entry10.config(state='normal')
        self.number_entry10.insert(0, lotto[3])
        self.number_entry11.config(state='normal')
        self.number_entry11.insert(0, lotto[4])
        self.number_entry12.config(state='normal')
        self.number_entry12.insert(0, lotto[5])

    def claim_prize(self):
        msg_box = messagebox.askquestion("Claiming your Prize", "Are you sure you want to claim your prize?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()
            import claim_prize

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Play(window)
window.mainloop()
