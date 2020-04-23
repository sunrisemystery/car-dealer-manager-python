from tkinter import *
import tkinter.messagebox
from customers_db import CustomersDatabase
import carsDisplayer as cd
import cars as cars
import shared as s
import mainTest2 as test

import sqlite3



class CustomerLogin:
    def __init__(self, cust_app):
        self.cust_app = cust_app
        self.cust_app.geometry('420x200')
        self.cust_app.title('Customer Login Panel')


        db = CustomersDatabase('mydatavase.db')

        # creating functions
        def clear_text():

            email_entry.delete(0, END)
            access_key_entry.delete(0, END)


        def add_cust():
            if email_text.get() == '' or access_key_text.get() == '':
                tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                return
 

            searchCust()


        def searchCust():

            row=db.searchUser(email_text.get(),access_key_text.get())
            if not row:

                tkinter.messagebox.showerror("Error", "Wrong email or access key!")
                return
            else:
                row2=db.isAdmin(email_text.get(),access_key_text.get())



                if not row2:
                    tkinter.messagebox.showinfo("Login Successful", "Success!")
                   
                    
                    s.logged_id=db.getID(email_text.get(),access_key_text.get())
                    

                    self.cust_app.destroy()
                    self.cust_app=Tk()
                    application=cd.CarsDisplayer(self.cust_app)
                    self.cust_app.mainloop()
                else:
                    tkinter.messagebox.showinfo("Login Successful", "Success! - Admin Permission")
                    self.cust_app.destroy()
                    self.cust_app=Tk()
                    application=cars.Cars(self.cust_app)
                    self.cust_app.mainloop()
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

        dataFrame = Frame(mainFrame, bd=0, width=700, height=100,padx=50, relief=RIDGE)
        dataFrame.pack(side=TOP)
        buttonFrame = Frame(mainFrame, width=735, height=40, bd=1, relief=RIDGE)
        buttonFrame.pack(side=TOP)



        # part



        email_text = StringVar()
        email_label = Label(dataFrame, text='Email', font=('calibri', 12),pady=10,padx=10)
        email_label.grid(row=1, column=0, sticky=E)
        email_entry = Entry(dataFrame, textvariable=email_text, font=('calibri', 12))
        email_entry.grid(row=1, column=1)

        access_key_text = StringVar()
        access_key_label = Label(dataFrame, text='Access Key', font=('calibri', 12),pady=20)
        access_key_label.grid(row=2, column=0, sticky=E)
        access_key_entry = Entry(dataFrame, textvariable=access_key_text, font=('calibri', 12))
        access_key_entry.grid(row=2, column=1)



        # buttons

        add_btn = Button(buttonFrame, text='Login', width=12, command=add_cust,padx=10)
        add_btn.grid(column=0, row=0, sticky=W)


        clear_btn = Button(buttonFrame, text='Clear', width=12, command=clear_text)
        clear_btn.grid(column=1, row=0, sticky=W)

        menu_btn = Button(buttonFrame, text='Menu', width=12,command=back)
        menu_btn.grid(column=2, row=0, sticky=W)

        exit_btn = Button(buttonFrame, text='Exit', width=12, command=iExit, bg='firebrick2')
        exit_btn.grid(column=3, row=0, sticky=W)



if __name__ == "__main__":
    cust_app = Tk()
    application = CustomerLogin(cust_app)

    cust_app.mainloop()
