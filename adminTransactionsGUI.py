import tkinter as tk
import cars_db
import transactions_db
import cars
import shared

BG_BUTTON = 'HotPink3'
GEOMETRY_SIZE = '700x450'
DATABASE = 'mydatavase.db'


class TransactionDisplayer:
    def __init__(self, car_app):
        self.car_app = car_app
        self.car_app.geometry(GEOMETRY_SIZE)
        self.car_app.title('Transaction Editor')
        self.car_app.configure(bg=shared.BG_COLOR)

        cars_db.CarsDatabase(DATABASE)
        trans_db = transactions_db.TransactionsDatabase(DATABASE)

        def select_item(event):
            global selected_item
            index = cars_list.curselection()[0]
            selected_item = cars_list.get(index)

        def my_trans():
            cars_list.delete(0, tk.END)
            for rows in trans_db.all_transactions():
                cars_list.insert(tk.END, rows)

        def remove_transaction():
            try:
                trans_db.remove(selected_item[0])

                my_trans()
            except:
                pass

        def i_exit_fun():

            i_exit = tk.messagebox.askyesno("Car Dealer Management Database System",
                                            "Do you want to exit?")
            if i_exit > 0:
                car_app.destroy()
                return

        def back():
            self.car_app.destroy()
            self.car_app = tk.Tk()
            cars.Cars(self.car_app)
            self.car_app.mainloop()

        # Create window

        # frames
        main_frame = tk.Frame(self.car_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()
        #

        button_frame = tk.Frame(main_frame, width=735, height=40, bd=1, relief=tk.RIDGE,bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)
        #
        listbox_frame = tk.Frame(main_frame, bd=0, width=735,
                                 height=310, padx=80, pady=10, relief=tk.RIDGE,bg=shared.BG_COLOR)
        listbox_frame.pack(side=tk.TOP)

        # -----LISTBOX------------------
        cars_list = tk.Listbox(listbox_frame, height=15, width=90)

        cars_list.grid(row=0, column=0, columnspan=3, rowspan=6)

        # creating scrollbar
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.grid(row=3, column=3, sticky='ns')

        # set scroll to listbox

        cars_list.configure(yscrollcommand=scrollbar.set,bg=shared.LISTBOX_COLOR)
        scrollbar.configure(command=cars_list.yview,bg=shared.BG_COLOR)

        # bind select

        cars_list.bind('<<ListboxSelect>>', select_item)

        # buttons

        back_btn = tk.Button(button_frame, text='< Back', width=15, command=back,bg=shared.BG_COLOR)
        back_btn.grid(column=1, row=0, sticky=tk.W)
        #
        book_btn = tk.Button(button_frame, text='Remove Transaction', width=15,
                             command=remove_transaction,bg=shared.BG_COLOR)
        book_btn.grid(column=2, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12, command=i_exit_fun,
                             bg=BG_BUTTON)
        exit_btn.grid(column=3, row=0, sticky=tk.W)
        # commands

        my_trans()


if __name__ == "__main__":
    car_disp = tk.Tk()
    application = TransactionDisplayer(car_disp)

    car_disp.mainloop()
