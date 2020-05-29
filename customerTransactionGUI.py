"""Defines a class responsible for Transactions' Window for Admin."""
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk

import adminTransactionsGUI
import carsDisplayer
import cars_db
import shared
import transactions_db

GEOMETRY_SIZE = '620x400'
COLS = ('ID', 'BRAND', 'MODEL', 'COLOR', 'YEAR', 'PRICE', 'DATE')
COL_SIZE = [(25, 25), (50, 50), (100, 100), (50, 50), (50, 50),
            (50, 50), (111, 111)]


class TransactionCustomerDisplayer(adminTransactionsGUI.TransactionBase):
    """This class displays Transactions' Window for Customer and contains
        functionality for buttons."""

    def __init__(self, car_app):
        """Inits TransactionCustomerDisplayer."""
        adminTransactionsGUI.TransactionBase.__init__(self, car_app)
        self.car_app.geometry(GEOMETRY_SIZE)
        self.car_app.configure(bg=shared.BG_COLOR)
        self.car_app.title('Transaction Viewer')

        cars_db.CarsDatabase('mydatavase.db')
        self.trans_db = transactions_db.TransactionsDatabase(shared.DATABASE)

    def my_transactions(self):
        """Displays customer's transactions."""
        for i in self.table.get_children():
            self.table.delete(i)
        for row in self.trans_db.search_transactions(shared.LOGGED_ID):
            self.table.insert('', tk.END, values=row)

    def back(self):
        """Turns back to Available Car List Panel."""
        self.car_app.destroy()
        self.car_app = tk.Tk()
        car_display_window = carsDisplayer.CarsDisplayer(self.car_app)
        car_display_window.init_window()
        car_display_window.populate_list()
        self.car_app.mainloop()

    def init_window(self):
        """Inits window and labels."""

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
        self.table = tkinter.ttk.Treeview(table_frame, columns=COLS, show='headings', height=10)
        self.table.grid()

        for x, y in zip(COLS, COL_SIZE):
            self.table.column(x, minwidth=y[0], width=y[1], anchor=tk.CENTER)
            self.table.heading(x, text=x)

        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_y.configure(command=self.table.yview())
        scroll_y.grid(row=0, column=3, sticky='ns')

        self.table.configure(yscrollcommand=scroll_y.set)
        self.table.bind('<ButtonRelease-1>', self.select_item)

        # buttons

        back_button = tk.Button(button_frame, text='< Back', width=12, command=self.back,
                                bg=shared.BG_COLOR)
        back_button.grid(column=1, row=0, sticky=tk.W)

        exit_button = tk.Button(button_frame, text='Exit', width=12,
                                command=self.exit, bg=shared.BG_BUTTON)
        exit_button.grid(column=2, row=0, sticky=tk.W)
