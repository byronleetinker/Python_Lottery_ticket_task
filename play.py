from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound
import uuid

window = Tk()
window.geometry("1000x500")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"

player_entry = uuid.uuid1()
print(player_entry)

class Play:
    def __init__(self, window):
        self.lotto_list = []
        self.player = Label(window, text='Player ID: ', bg='royalblue', font=("Arial", 12, "bold"))
        self.player.place(x=10, y=20)
        self.player_entry = Label(window, text=player_entry, bg='royalblue', font=("Arial", 12, "bold"))
        self.player_entry.place(x=90, y=20)
        self.info = Label(window, text='Please choose 6 numbers from ranging from 1 to 49.', bg='royalblue',
                          font=("Arial", 12, "bold"))
        self.info.place(x=10, y=140)
        self.results = Label(window, text='Results.', bg='royalblue', font=("Arial", 12, "bold"))
        self.results.place(x=730, y=140)
        self.number_entry = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry.place(x=30, y=210)
        self.number_entry2 = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry2.place(x=90, y=210)
        self.number_entry3 = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry3.place(x=150, y=210)
        self.number_entry4 = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry4.place(x=210, y=210)
        self.number_entry5 = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry5.place(x=270, y=210)
        self.number_entry6 = Entry(window, width=3, font=("Arial", 20, "bold"))
        self.number_entry6.place(x=330, y=210)
        self.number_entry7 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry7.place(x=600, y=210)
        self.number_entry8 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry8.place(x=660, y=210)
        self.number_entry9 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry9.place(x=720, y=210)
        self.number_entry10 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry10.place(x=780, y=210)
        self.number_entry11 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry11.place(x=840, y=210)
        self.number_entry12 = Entry(window, width=3, font=("Arial", 20, "bold"), state='readonly')
        self.number_entry12.place(x=900, y=210)
        self.play = Button(window, text='Play', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.lotto_numbers)
        self.play.place(x=170, y=300)
        self.play_again = Button(window, text='Play again', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                                 command=self.play_again)
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

        if number not in lotto:
            lotto.append(number)

        if self.number_entry.get() == "" or self.number_entry2.get() == "" or self.number_entry3.get() == "" or self.number_entry4.get() == "" or self.number_entry5.get() == "" or self.number_entry6.get() == "":
            messagebox.showerror("Empty Entries", "Fill in all Entries")
        else:
            self.number_entry7.configure(state="normal")
            self.number_entry7.insert(0, lotto[0])
            self.number_entry7.configure(state='readonly')
            self.number_entry8.config(state='normal')
            self.number_entry8.insert(0, lotto[1])
            self.number_entry8.configure(state='readonly')
            self.number_entry9.config(state='normal')
            self.number_entry9.insert(0, lotto[2])
            self.number_entry9.configure(state='readonly')
            self.number_entry10.config(state='normal')
            self.number_entry10.insert(0, lotto[3])
            self.number_entry10.configure(state='readonly')
            self.number_entry11.config(state='normal')
            self.number_entry11.insert(0, lotto[4])
            self.number_entry11.configure(state='readonly')
            self.number_entry12.config(state='normal')
            self.number_entry12.insert(0, lotto[5])
            self.number_entry12.configure(state='readonly')

            lotto = set(lotto)
            user_numbers = {int(self.number_entry.get()), int(self.number_entry2.get()), int(self.number_entry3.get()),
                            int(self.number_entry4.get()), int(self.number_entry5.get()),
                            int(self.number_entry6.get())}
            matches = lotto.intersection(user_numbers)
            win = len(matches)

        if win == 2:
            messagebox.showinfo("Congratulations", "You've won R20.00")

        elif win == 3:
            messagebox.showinfo("Congratulations", "You've won R100.00")

        elif win == 4:
            messagebox.showinfo("Congratulations", "You've won R2 384.00")

        elif win == 5:
            messagebox.showinfo("Congratulations", "You've won R8 584.00")

        elif win == 6:
            messagebox.showinfo("Congratulations", "You've won R10 000 000.000")

        else:
            messagebox.showinfo("Tough Luck", "Play again and stand a chance of winning R10 000 000.00")

    def play_again(self):
        self.number_entry.delete(0, END)
        self.number_entry2.delete(0, END)
        self.number_entry3.delete(0, END)
        self.number_entry4.delete(0, END)
        self.number_entry5.delete(0, END)
        self.number_entry6.delete(0, END)
        self.number_entry7.config(state='normal')
        self.number_entry8.config(state='normal')
        self.number_entry9.config(state='normal')
        self.number_entry10.config(state='normal')
        self.number_entry11.config(state='normal')
        self.number_entry12.config(state='normal')
        self.number_entry7.delete(0, END)
        self.number_entry8.delete(0, END)
        self.number_entry9.delete(0, END)
        self.number_entry10.delete(0, END)
        self.number_entry11.delete(0, END)
        self.number_entry12.delete(0, END)

    def claim_prize(self):
        msg_box = messagebox.askquestion("Claiming your Prize", "Are you sure you want to claim your prize?",
                                         icon='warning')
        if msg_box == "yes":
            playsound("byron.mp3")
            window.destroy()
            import claim_prize

    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            window.destroy()


obj = Play(window)
window.mainloop()
