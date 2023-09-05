from tkinter import *
from tkinter import messagebox
import os


def login():
    user = username.get()
    code = password.get()

    if user == "Andre" and code == "1234":
        root = Toplevel(screen)
        root.title("Bill")
        root.geometry("1280x720+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False, False)

        def Reset():
            entry_dosa.delete(0, END)
            entry_cookies.delete(0, END)
            entry_tea.delete(0, END)
            entry_coffee.delete(0, END)
            entry_juice.delete(0, END)
            entry_pancakes.delete(0, END)
            entry_pancakes.delete(0, END)
            entry_eggs.delete(0, END)

        def Total():
            try:
                a1 = int(dosa.get())
            except:
                a1 = 0

            try:
                a2 = int(cookies.get())
            except:
                a2 = 0

            try:
                a3 = int(tea.get())
            except:
                a3 = 0

            try:
                a4 = int(coffee.get())
            except:
                a4 = 0

            try:
                a5 = int(juice.get())
            except:
                a5 = 0

            try:
                a6 = int(pancakes.get())
            except:
                a6 = 0

            try:
                a7 = int(eggs.get())
            except:
                a7 = 0

            #! define cost of each item per quantity
            c1 = 60*a1
            c2 = 30*a2
            c3 = 7*a3
            c4 = 100*a4
            c5 = 20*a5
            c6 = 15*a6
            c7 = 7*a7

            lbl_total = Label(f2, font=("arial", 20, "bold"),
                              text="Total", width=16, fg="lightyellow", bg="black")
            lbl_total.place(x=0, y=50)

            entry_total = Entry(f2, font=("arial", 20, "bold"),
                                textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
            entry_total.place(x=20, y=100)

            totalcost = c1+c2+c3+c4+c5+c6+c7
            string_bill = str('%.2f' % totalcost), "€"
            Total_bill.set(string_bill)

        Total_bill = StringVar()

        Label(root, text="Bill Management System", bg="black", fg="white",
              font=("Calibri", 33), width="300", height="2").pack()

        #! MENU CARD
        f = Frame(root, bg="lightgreen", highlightbackground="Black",
                  highlightthickness=1, width=300, height=370)
        f.place(x=10, y=118)

        Label(f, text="Menu Card", bg="lightgreen", fg="black",
              font=("Gabriola", 40, "bold")).place(x=50, y=0)

        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Dosa...........60€/plate", fg="black", bg="lightgreen").place(x=10, y=80)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Cookies.......30€/plate", fg="black", bg="lightgreen").place(x=10, y=110)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Tea.............7€/cup", fg="black", bg="lightgreen").place(x=10, y=140)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Coffee.........100€/cup", fg="black", bg="lightgreen").place(x=10, y=170)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Juice..........20€/glass", fg="black", bg="lightgreen").place(x=10, y=200)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Pancakes...15€/pack", fg="black", bg="lightgreen").place(x=10, y=230)
        Label(f, font=("Lucida Calligraphy", 15, "bold"),
              text="Eggs...........7€/egg", fg="black", bg="lightgreen").place(x=10, y=260)

        #! BILL
        f2 = Frame(root, bg="lightyellow", highlightbackground="Black",
                   highlightthickness=1, width=300, height=370)
        f2.place(x=950, y=118)

        Bill = Label(f2, text="Bill", font=("calibri", 20), bg="lightyellow")
        Bill.place(x=120, y=10)

        #! ENTRY WORK
        f1 = Frame(root, bd=5, height=370, width=300, relief=RAISED)
        f1.pack()

        dosa = StringVar()
        cookies = StringVar()
        tea = StringVar()
        coffee = StringVar()
        juice = StringVar()
        pancakes = StringVar()
        eggs = StringVar()

        #! Label
        lbl_dosa = Label(f1, text="Dosa", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_dosa.grid(row=1, column=0)
        lbl_cookies = Label(f1, text="Cookies", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_cookies.grid(row=2, column=0)
        lbl_tea = Label(f1, text="Tea", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_tea.grid(row=3, column=0)
        lbl_coffee = Label(f1, text="Coffee", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_coffee.grid(row=4, column=0)
        lbl_juice = Label(f1, text="Juice", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_juice.grid(row=5, column=0)
        lbl_pancakes = Label(f1, text="Pancakes", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_pancakes.grid(row=6, column=0)
        lbl_eggs = Label(f1, text="Eggs", font=(
            "aria", 20, "bold"), fg="blue4", width=12)
        lbl_eggs.grid(row=7, column=0)

        #! Entry
        entry_dosa = Entry(f1, font=("aria", 20, "bold"),
                           textvariable=dosa, bd=6, width=8, bg="lightpink")
        entry_dosa.grid(row=1, column=1)
        entry_cookies = Entry(f1, font=("aria", 20, "bold"),
                              textvariable=cookies, bd=6, width=8, bg="lightpink")
        entry_cookies.grid(row=2, column=1)
        entry_tea = Entry(f1, font=("aria", 20, "bold"),
                          textvariable=tea, bd=6, width=8, bg="lightpink")
        entry_tea.grid(row=3, column=1)
        entry_coffee = Entry(f1, font=("aria", 20, "bold"),
                             textvariable=coffee, bd=6, width=8, bg="lightpink")
        entry_coffee.grid(row=4, column=1)
        entry_juice = Entry(f1, font=("aria", 20, "bold"),
                            textvariable=juice, bd=6, width=8, bg="lightpink")
        entry_juice.grid(row=5, column=1)
        entry_pancakes = Entry(f1, font=("aria", 20, "bold"),
                               textvariable=pancakes, bd=6, width=8, bg="lightpink")
        entry_pancakes.grid(row=6, column=1)
        entry_eggs = Entry(f1, font=("aria", 20, "bold"),
                           textvariable=eggs, bd=6, width=8, bg="lightpink")
        entry_eggs.grid(row=7, column=1)

        #! Buttons
        btn_reset = Button(f1, text="Reset", font=("ariel", 16, "bold"),
                           fg="black", bg="lightblue", width=10, command=Reset)
        btn_reset.grid(row=8, column=0)

        btn_total = Button(f1, bd=5, fg="Black", bg="lightblue", font=(
            "ariel", 16, "bold"), width=10, text="Total", command=Total)
        btn_total.grid(row=8, column=1)

    elif user == "" and code == "":
        messagebox.showerror("Invalid", "Please enter Username and Password")
    elif user == "":
        messagebox.showerror("Invalid", "Username is required")
    elif code == "":
        messagebox.showerror("Invalid", "Password is required")
    elif user != "Andre" and code != "1234":
        messagebox.showerror("Invalid", "Username or Password is incorrect")
    elif user == "Andre":
        messagebox.showerror("Invalid", "Please enter a valid Username")
    elif code == "1234":
        messagebox.showerror("Invalid", "Please enter a valid assword")


def main_screen():

    global screen
    global username
    global password

    screen = Tk()
    screen.geometry("1280x720+150+80")
    screen.configure(bg="#d7dae2")

    #! icon
    image_icon = PhotoImage(file="icon.png")
    screen.iconphoto(False, image_icon)
    screen.title("Login System")

    lblTitle = Label(text="Login System", font=(
        "Arial", 50), bg="#d7dae2", fg="black")
    lblTitle.pack(pady=50)

    bordercolor = Frame(screen, bg="black", width=800, height=400)
    bordercolor.pack()

    mainframe = Frame(bordercolor, bg="#d7dae2", width=800, height=400)
    mainframe.pack(padx=20, pady=20)

    Label(mainframe, text="Username", font=(
        "Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=50)
    Label(mainframe, text="Password", font=(
        "Arial", 30, "bold"), bg="#d7dae2").place(x=100, y=150)

    username = StringVar()
    password = StringVar()

    entry_username = Entry(mainframe, textvariable=username, width=12, bd=2,
                           font=("Arial", 30))
    entry_username.place(x=400, y=50)
    entry_password = Entry(mainframe, textvariable=password, width=12, bd=2,
                           font=("Arial", 30), show="*")
    entry_password.place(x=400, y=150)

    def reset():
        entry_username.delete(0, END)
        entry_password.delete(0, END)

    Button(mainframe, text="Login", height=2, width=23,
           bg="#ed3933", fg="white", bd=0, command=login).place(x=100, y=250)
    Button(mainframe, text="Reset", height=2, width=23,
           bg="#1089ff", fg="white", bd=0, command=reset).place(x=300, y=250)
    Button(mainframe, text="Exit", height=2, width=23,
           bg="#00bd56", fg="white", bd=0, command=screen.destroy).place(x=500, y=250)

    screen.mainloop()


main_screen()
