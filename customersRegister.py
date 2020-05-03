from tkinter import *
import tkinter.messagebox
from customers_db import CustomersDatabase
import carsDisplayer as cd
import shared as s
import mainTest2 as test


class CustomerRegister:
    def __init__(self, cust_app):
        self.cust_app = cust_app
        self.cust_app.geometry('650x200')
        self.cust_app.title('Customer Registration Panel')

        db = CustomersDatabase('mydatavase.db')

        # creating functions
        def clear_text():
            name_entry.delete(0, END)
            lastname_entry.delete(0, END)
            email_entry.delete(0, END)
            access_key_entry.delete(0, END)
            phone_entry.delete(0, END)

        def add_cust():
            if name_text.get() == '' or lastname_text.get() == '' or email_text.get() == '' or access_key_text.get() == '' or phone_text.get() == '':
                tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                return
            try:
                if isinstance(int(access_key_text.get()), int) == False:
                    tkinter.messagebox.showerror("Access Key can't be a text", "Please write a numeric key")
                    return
            except:
                tkinter.messagebox.showerror("Access Key can't be a text", "Please write a numeric key")
                return

            try:
                if isinstance(int(phone_text.get()), int) == False:
                    tkinter.messagebox.showerror("Nuber can't include characters",
                                                 "Please write your number using.. numbers :)")
                    return
            except:
                tkinter.messagebox.showerror("Nuber can't include characters",
                                             "Please write your number using.. numbers :)")
                return
            if (len(access_key_text.get()) < 3):
                tkinter.messagebox.showerror("Access key fail",
                                             "Access key must have at least 3 digits")
                return

            if searchCust() != -1:
                db.insert(name_text.get().capitalize(), lastname_text.get().capitalize(), email_text.get(),
                          access_key_text.get(), phone_text.get())
                tkinter.messagebox.showinfo("Registration Successful", "Success!")
                s.logged_id = db.getID(email_text.get(), access_key_text.get())

                self.cust_app.destroy()
                self.cust_app = Tk()
                application = cd.CarsDisplayer(self.cust_app)
                self.cust_app.mainloop()

        def searchCust():

            for row in db.searchEmail(email_text.get()):
                if row:
                    tkinter.messagebox.showerror("Error", "This email is in this database")
                    return -1

        def back():
            self.cust_app.destroy()
            self.cust_app = Tk()
            application = test.MainTest(self.cust_app)

            self.cust_app.mainloop()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Registration Panel", "Do you want to exit?")
            if iExit > 0:
                cust_app.destroy()
                return

        # Create window

        # frames
        mainFrame = Frame(self.cust_app)
        mainFrame.grid()

        dataFrame = Frame(mainFrame, bd=0, width=700, height=100, padx=50, relief=RIDGE)
        dataFrame.pack(side=TOP)
        buttonFrame = Frame(mainFrame, width=735, height=40, bd=1, relief=RIDGE)
        buttonFrame.pack(side=TOP)

        # part
        name_text = StringVar()
        name_label = Label(dataFrame, text='Name', font=('calibri', 12), pady=20)
        name_label.grid(row=0, column=0, sticky=E)
        name_entry = Entry(dataFrame, textvariable=name_text, font=('calibri', 12))
        name_entry.grid(row=0, column=1)

        lastname_text = StringVar()
        lastname_label = Label(dataFrame, text='Lastname', font=('calibri', 12))
        lastname_label.grid(row=0, column=2, sticky=E, padx=(30, 0))
        lastname_entry = Entry(dataFrame, textvariable=lastname_text, font=('calibri', 12))
        lastname_entry.grid(row=0, column=3)

        email_text = StringVar()
        email_label = Label(dataFrame, text='Email', font=('calibri', 12))
        email_label.grid(row=1, column=0, sticky=E)
        email_entry = Entry(dataFrame, textvariable=email_text, font=('calibri', 12))
        email_entry.grid(row=1, column=1)

        access_key_text = StringVar()
        access_key_label = Label(dataFrame, text='Access Key', font=('calibri', 12))
        access_key_label.grid(row=1, column=2, sticky=E)
        access_key_entry = Entry(dataFrame, textvariable=access_key_text, font=('calibri', 12))
        access_key_entry.grid(row=1, column=3)

        phone_text = StringVar()
        phone_label = Label(dataFrame, text='Phone Number', font=('calibri', 12), pady=20)
        phone_label.grid(row=2, column=0, sticky=E)
        phone_entry = Entry(dataFrame, textvariable=phone_text, font=('calibri', 12))
        phone_entry.grid(row=2, column=1)

        # buttons

        add_btn = Button(buttonFrame, text='Create Account', width=12, command=add_cust)
        add_btn.grid(column=0, row=0, sticky=W)

        clear_btn = Button(buttonFrame, text='Clear', width=12, command=clear_text)
        clear_btn.grid(column=1, row=0, sticky=W)

        menu_btn = Button(buttonFrame, text='Menu', width=12, command=back)
        menu_btn.grid(column=2, row=0, sticky=W)

        exit_btn = Button(buttonFrame, text='Exit', width=12, command=iExit, bg='firebrick2')
        exit_btn.grid(column=3, row=0, sticky=W)


if __name__ == "__main__":
    cust_app = Tk()
    application = CustomerRegister(cust_app)

    cust_app.mainloop()
