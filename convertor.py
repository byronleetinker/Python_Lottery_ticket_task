# These are all my programming running in the background of my window.
from tkinter import *
from tkinter import messagebox
import requests

# Window size, title, whenever you can resize it and colour
window = Tk()
window.geometry("600x600")
window.title('Lottery_Ticket')
window.resizable("False", "False")
window["bg"] = "royalblue"
value = IntVar()


# Defining the Convertor class for my window includes labels, entries, buttons and their placements.
# These are defined by the names, size, fonts and even colours.
class Convertor:

    # Defining everything that will be displayed on the tkinter window
    def __init__(self, window):
        self.label = Label(window, text='Currency Convertor.', bg='royalblue', font=("Arial", 20, "bold"))
        self.label.place(x=170, y=30)
        self.information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
        self.information_json = self.information.json()
        self.conversion_rate = self.information_json['conversion_rates']
        self.value_label = Label(window, text="Value:", bg="royalblue", font=("Arial", 12, "bold"))
        self.value_label.place(x=180, y=100)
        self.value_entry = Entry(window, textvariable=value, width=20)
        self.value_entry.place(x=250, y=100)
        self.from_label = Label(window, text="From: ZAR", bg="royalblue", font=("Arial", 12, "bold"))
        self.from_label.place(x=250, y=150)
        self.convert = Label(window, text="To:", bg="royalblue", font=("Arial", 12, "bold"))
        self.convert.place(x=250, y=180)
        self.convert_label = Label(window, text="Converted to: ", bg="royalblue", font=("Arial", 12, "bold"))
        self.convert_label.place(x=260, y=450)
        self.exit = Button(window, text='Exit', bg='lightgreen', borderwidth=5, font=("Arial", 12, "bold"),
                           command=self.exit)
        self.exit.place(x=500, y=500)
        self.convert_btn = Button(window, text="Convert", bg="lightgreen", borderwidth=5, command=self.convert_curr,
                                  font=("Arial", 12, "bold"))
        self.convert_btn.place(x=50, y=500)
        self.convert_list = Listbox(window, width=20)
        for i in self.conversion_rate.keys():
            self.convert_list.insert(END, str(i))
        self.convert_list.place(x=230, y=230)

    # Defining the currency function, this gives function to my currency convertor.
    def convert_curr(self):
        num = float(self.value_entry.get())
        print(self.information_json['conversion_rates'][self.convert_list.get(ACTIVE)])
        self.information_json['conversion_rates'][self.convert_list.get(ACTIVE)]
        ans = round(num * self.information_json['conversion_rates'][self.convert_list.get(ACTIVE)], 2)
        self.convert_label['text'] = ans

    # Defining the exit function making sure that you really want to exit the program and
    # if you do it will close the program
    def exit(self):
        msg_box = messagebox.askquestion("Exit Application", "Are you sure you want to exit the application?",
                                         icon='warning')
        if msg_box == "yes":
            # If the player wants to exit the program, it will display this message and the window will close.
            messagebox.showinfo("Goodbye", "You are now exiting the program, Thank you for playing!")
            window.destroy()


# Reference what should be displayed on the window
obj = Convertor(window)
# Without this the window will not stop running resulting in no results being displayed
window.mainloop()
