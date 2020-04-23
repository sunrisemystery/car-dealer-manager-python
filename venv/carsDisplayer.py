from tkinter import *
import tkinter.messagebox
from cars_db import CarsDatabase
from transactions_db import TransactionsDatabase
import customerTransactionGUI as ctg
import customerEditAccount as cea
import shared as s
import sqlite3


class CarsDisplayer:
    def __init__(self, car_app):
        self.car_app = car_app
        self.car_app.geometry('700x450')
        self.car_app.title('Available Car List')


        db = CarsDatabase('mydatavase.db')
        trans_db=TransactionsDatabase('mydatavase.db')

        # creating functions
        def clear_text():
            brand_entry.delete(0, END)
            model_entry.delete(0, END)
            color_entry.delete(0, END)
            year_entry.delete(0, END)
            price_entry.delete(0, END)


        def populate_list():
            cars_list.delete(0, END)
            for row in db.fetch_available():
                cars_list.insert(END, row)


        def select_item(event):
            global selected_item
            index = cars_list.curselection()[0]
            selected_item = cars_list.get(index)

            brand_entry.delete(0, END)
            brand_entry.insert(END, selected_item[1])

            model_entry.delete(0, END)
            model_entry.insert(END, selected_item[2])

            color_entry.delete(0, END)
            color_entry.insert(END, selected_item[3])

            year_entry.delete(0, END)
            year_entry.insert(END, selected_item[4])

            price_entry.delete(0, END)
            price_entry.insert(END, selected_item[6])



        def searchCar():
            cars_list.delete(0, END)
            for row in db.search(year_text.get(), price_text.get(), brand_text.get(), model_text.get(),
                                 color_text.get()):
                cars_list.insert(END, row)
        def myTrans():
            self.car_app.destroy()
            self.car_app=Tk()
            mytransaction=ctg.TransactionCustomerDisplayer(self.car_app)
            self.car_app.mainloop()
                

        def bookcar():
            try:
                iscar=db.isout(selected_item[0])
                if iscar[0]==0:
                    pass
                else:
                    db.outofstock(selected_item[0])
                    tkinter.messagebox.showinfo("Book Successful", "Book Successful")
                    populate_list()
                    trans_db.insertTransaction(s.logged_id,selected_item[0])
            except:
                pass

        def update_car():
            db.update(selected_item[0],brand_text.get(),model_text.get(),color_text.get(),year_text.get(),price_text.get())
            populate_list()

        def editacc():
            self.car_app.destroy()
            self.car_app = Tk()
            editaccnt = cea.CustomerEditAcc(self.car_app)
            self.car_app.mainloop()



        def iExit():
            iExit = tkinter.messagebox.askyesno("Car Dealer Management Database System", "Do you want to exit?")
            if iExit > 0:
                car_app.destroy()
                return

        # Create window

        # frames
        mainFrame = Frame(self.car_app)
        mainFrame.grid()

        dataFrame = Frame(mainFrame, bd=0, width=700, height=100, padx=100, relief=RIDGE)
        dataFrame.pack(side=TOP)
        buttonFrame = Frame(mainFrame, width=735, height=40, bd=1, relief=RIDGE)
        buttonFrame.pack(side=TOP)

        listboxFrame = Frame(mainFrame, bd=0, width=735, height=310, padx=80, pady=10, relief=RIDGE)
        listboxFrame.pack(side=TOP)

        # part
        brand_text = StringVar()
        brand_label = Label(dataFrame, text='Brand Name', font=('calibri', 12), pady=20)
        brand_label.grid(row=0, column=0, sticky=E)
        brand_entry = Entry(dataFrame, textvariable=brand_text, font=('calibri', 12))
        brand_entry.grid(row=0, column=1)

        model_text = StringVar()
        model_label = Label(dataFrame, text='Model Name', font=('calibri', 12))
        model_label.grid(row=0, column=2, sticky=E, padx=(30, 0))
        model_entry = Entry(dataFrame, textvariable=model_text, font=('calibri', 12))
        model_entry.grid(row=0, column=3)

        color_text = StringVar()
        color_label = Label(dataFrame, text='Car Color', font=('calibri', 12))
        color_label.grid(row=1, column=0, sticky=E)
        color_entry = Entry(dataFrame, textvariable=color_text, font=('calibri', 12))
        color_entry.grid(row=1, column=1)

        year_text = StringVar()
        year_label = Label(dataFrame, text='Car Year ', font=('calibri', 12))
        year_label.grid(row=1, column=2, sticky=E)
        year_entry = Entry(dataFrame, textvariable=year_text, font=('calibri', 12))
        year_entry.grid(row=1, column=3)

        price_text = StringVar()
        price_label = Label(dataFrame, text='Car Price', font=('calibri', 12), pady=20)
        price_label.grid(row=2, column=0, sticky=E)
        price_entry = Entry(dataFrame, textvariable=price_text, font=('calibri', 12))
        price_entry.grid(row=2, column=1)
        # -----LISTBOX------------------
        cars_list = Listbox(listboxFrame, height=15, width=90)

        cars_list.grid(row=0, column=0, columnspan=3, rowspan=6)

        # creating scrollbar
        scrollbar = Scrollbar(listboxFrame)
        scrollbar.grid(row=3, column=3, sticky='ns')

        # set scroll to listbox

        cars_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=cars_list.yview)

        # bind select

        cars_list.bind('<<ListboxSelect>>', select_item)

        # buttons


        clear_btn = Button(buttonFrame, text='Clear', width=12, command=clear_text)
        clear_btn.grid(column=0, row=0, sticky=W)

        display_btn = Button(buttonFrame, text='Display', width=12, command=populate_list)
        display_btn.grid(column=1, row=0, sticky=W)

        search_btn = Button(buttonFrame, text='Search', width=12, command=searchCar)
        search_btn.grid(column=2, row=0, sticky=W)

        book_btn = Button(buttonFrame, text='Book A Car', width=12,command=bookcar)
        book_btn.grid(column=3, row=0, sticky=W)

        menu_btn = Button(buttonFrame, text='My Transactions', width=12,command=myTrans)
        menu_btn.grid(column=4, row=0, sticky=W)

        edit_btn = Button(buttonFrame, text='Edit Account', width=12,command=editacc)
        edit_btn.grid(column=5, row=0, sticky=W)

        exit_btn = Button(buttonFrame, text='Exit', width=12, command=iExit, bg='firebrick2')
        exit_btn.grid(column=6, row=0, sticky=W)
        # commands

        populate_list()


if __name__=="__main__":
    car_disp=Tk()
    application=CarsDisplayer(car_disp)

    car_disp.mainloop()