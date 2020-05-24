"""Defines a class responsible for Transactions' Window for Admin."""
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
import cars_db
import transactions_db
import carsDisplayer
import shared

GEOMETRY_SIZE = '620x400'
DATABASE = 'mydatavase.db'
BG_BUTTON = 'HotPink3'


class TransactionCustomerDisplayer:
    """This class displays Transactions' Window for Customer and contains
        functionality for buttons."""

    def __init__(self, car_app):
        """Inits TransactionCustomerDisplayer."""
        self.car_app = car_app
        self.car_app.geometry(GEOMETRY_SIZE)
        car_app.configure(bg=shared.BG_COLOR)
        self.car_app.title('Transaction Viewer')

        cars_db.CarsDatabase('mydatavase.db')
        trans_db = transactions_db.TransactionsDatabase(DATABASE)

        def select_item(event):
            """Stores an index of selected item."""
            global selected_item
            try:
                if table.selection() != ():
                    selected_item = table.set(table.selection())
            except:
                pass

        def my_trans():
            """Displays customer's transactions."""
            for i in table.get_children():
                table.delete(i)
            for row in trans_db.search_transactions(shared.logged_id):
                table.insert('', tk.END, values=row)

        def i_exit_fun():
            """Finishes program."""
            i_exit = tkinter.messagebox.askyesno("Car Dealer Management Database System",
                                                 "Do you want to exit?")
            if i_exit > 0:
                car_app.destroy()
                return

        def back():
            """Turns back to Available Car List Panel."""
            self.car_app.destroy()
            self.car_app = tk.Tk()
            carsDisplayer.CarsDisplayer(self.car_app)
            self.car_app.mainloop()

        # frames
        main_frame = tk.Frame(self.car_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        button_frame = tk.Frame(main_frame, width=620, height=40, bd=1, relief=tk.RIDGE,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        table_frame = tk.Frame(main_frame, bd=0, width=735, height=310,
                               padx=80, pady=10, relief=tk.RIDGE, bg=shared.BG_COLOR)
        table_frame.pack(side=tk.TOP)

        # creating table
        cols = ('ID', 'BRAND', 'MODEL', 'COLOR', 'YEAR', 'PRICE', 'DATE')
        col_size = [(25, 25), (50, 50), (100, 100), (50, 50), (50, 50),
                    (50, 50), (111, 111)]
        table = tkinter.ttk.Treeview(table_frame, columns=cols, show='headings', height=10)
        table.grid()

        for x, y in zip(cols, col_size):
            table.column(x, minwidth=y[0], width=y[1], anchor=tk.CENTER)
            table.heading(x, text=x)

        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_y.configure(command=table.yview())
        scroll_y.grid(row=0, column=3, sticky='ns')

        table.configure(yscrollcommand=scroll_y.set)
        table.bind('<ButtonRelease-1>', select_item)

        # buttons

        back_btn = tk.Button(button_frame, text='< Back', width=12, command=back,
                             bg=shared.BG_COLOR)
        back_btn.grid(column=1, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12,
                             command=i_exit_fun, bg=BG_BUTTON)
        exit_btn.grid(column=2, row=0, sticky=tk.W)
        # commands

        my_trans()
