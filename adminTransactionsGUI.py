from tkinter import *
import tkinter.messagebox
from cars_db import CarsDatabase
from transactions_db import TransactionsDatabase
import cars as cr

class TransactionDisplayer:
    def __init__(self, car_app):
        self.car_app = car_app
        self.car_app.geometry('700x450')
        self.car_app.title('Transaction Editor')

        db = CarsDatabase('mydatavase.db')
        trans_db = TransactionsDatabase('mydatavase.db')


        def select_item(event):
            global selected_item
            index = cars_list.curselection()[0]
            selected_item = cars_list.get(index)


        def myTrans():
            cars_list.delete(0, END)
            for rows in trans_db.allTransactions():
                cars_list.insert(END, rows)
        def remove_transaction():
            try:
                trans_db.remove(selected_item[0])

                myTrans()
            except:
                pass


        def iExit():
            iExit = tkinter.messagebox.askyesno("Car Dealer Management Database System", "Do you want to exit?")
            if iExit > 0:
                car_app.destroy()
                return

        def back():
            self.car_app.destroy()
            self.car_app=Tk()
            appBack=cr.Cars(self.car_app)
            self.car_app.mainloop()

        # Create window

        # frames
        mainFrame = Frame(self.car_app)
        mainFrame.grid()
        #

        buttonFrame = Frame(mainFrame, width=735, height=40, bd=1, relief=RIDGE)
        buttonFrame.pack(side=TOP)
        #
        listboxFrame = Frame(mainFrame, bd=0, width=735, height=310, padx=80, pady=10, relief=RIDGE)
        listboxFrame.pack(side=TOP)

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



        back_btn = Button(buttonFrame, text='< Back', width=15,command=back)
        back_btn.grid(column=1, row=0, sticky=W)
        #
        book_btn = Button(buttonFrame, text='Remove Transaction', width=15, command=remove_transaction)
        book_btn.grid(column=2, row=0, sticky=W)



        exit_btn = Button(buttonFrame, text='Exit', width=12, command=iExit, bg='firebrick2')
        exit_btn.grid(column=3, row=0, sticky=W)
        # commands

        myTrans()


if __name__ == "__main__":
    car_disp = Tk()
    application = TransactionDisplayer(car_disp)

    car_disp.mainloop()