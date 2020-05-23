import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
import cars_db
import transactions_db
import customerTransactionGUI
import customerEditAccount
import shared

global selected_item

GEOMETRY_SIZE = '735x450'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class CarsDisplayer:
    def __init__(self, car_app):
        self.car_app = car_app
        self.car_app.geometry(GEOMETRY_SIZE)
        self.car_app.title('Available Car List')
        self.car_app.configure(bg=shared.BG_COLOR)

        db = cars_db.CarsDatabase(DATABASE)
        trans_db = transactions_db.TransactionsDatabase(DATABASE)

        # creating functions
        def clear_text():
            brand_entry.delete(0, tk.END)
            model_entry.delete(0, tk.END)
            color_entry.delete(0, tk.END)
            year_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)

        def populate_list():
            for i in table.get_children():
                table.delete(i)
            for record in db.fetch_available():
                table.insert('', tk.END,
                             values=[record[0], record[1], record[2], record[3], record[4],
                                     record[6]])

        def select_item(event):

            global selected_item
            if table.selection() != ():
                selected_item = table.set(table.selection())

                brand_entry.delete(0, tk.END)
                brand_entry.insert(tk.END, selected_item[cols[1]])

                model_entry.delete(0, tk.END)
                model_entry.insert(tk.END, selected_item[cols[2]])

                color_entry.delete(0, tk.END)
                color_entry.insert(tk.END, selected_item[cols[3]])

                year_entry.delete(0, tk.END)
                year_entry.insert(tk.END, selected_item[cols[4]])

                price_entry.delete(0, tk.END)
                price_entry.insert(tk.END, selected_item[cols[5]])

        def search_car():
            """Displays cars that met given criteria. """
            for i in table.get_children():
                table.delete(i)

            for row in db.search(*[f.get() for f in DB_FIELDS]):
                table.insert('', tk.END,
                             values=[row[0], row[1], row[2], row[3], row[4],
                                     row[6]])

        def my_trans():
            self.car_app.destroy()
            self.car_app = tk.Tk()
            customerTransactionGUI.TransactionCustomerDisplayer(self.car_app)
            self.car_app.mainloop()

        def book_car():
            try:
                is_car = db.isout(selected_item[cols[0]])
                if is_car[0] == 0:
                    pass
                else:
                    db.outofstock(selected_item[cols[0]])
                    tkinter.messagebox.showinfo("Book Successful", "Book Successful")
                    populate_list()
                    trans_db.insert_transaction(shared.logged_id, selected_item[cols[0]])
            except:
                pass

        def edit_acc():
            self.car_app.destroy()
            self.car_app = tk.Tk()
            customerEditAccount.CustomerEditAcc(self.car_app)
            self.car_app.mainloop()

        def i_exit_fun():
            i_exit = tkinter.messagebox.askyesno("Car Dealer Management Database System",
                                                 "Do you want to exit?")
            if i_exit > 0:
                car_app.destroy()
                return

        # Create window

        # frames
        main_frame = tk.Frame(self.car_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=100, relief=tk.RIDGE,
                              bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=700, height=40, bd=1, relief=tk.RIDGE,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        table_frame = tk.Frame(main_frame, bd=0, width=735, height=310, padx=80,
                               pady=10, relief=tk.RIDGE, bg=shared.BG_COLOR)
        table_frame.pack(side=tk.TOP)

        # part
        brand_text = tk.StringVar()
        brand_label = tk.Label(data_frame, text='Brand Name', font=FONT_SIZE, pady=20,
                               bg=shared.BG_COLOR)
        brand_label.grid(row=0, column=0, sticky=tk.E)
        brand_entry = tk.Entry(data_frame, textvariable=brand_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        brand_entry.grid(row=0, column=1)

        model_text = tk.StringVar()
        model_label = tk.Label(data_frame, text='Model Name', font=FONT_SIZE, bg=shared.BG_COLOR)
        model_label.grid(row=0, column=2, sticky=tk.E, padx=(30, 0))
        model_entry = tk.Entry(data_frame, textvariable=model_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        model_entry.grid(row=0, column=3)

        color_text = tk.StringVar()
        color_label = tk.Label(data_frame, text='Car Color', font=FONT_SIZE, bg=shared.BG_COLOR)
        color_label.grid(row=1, column=0, sticky=tk.E)
        color_entry = tk.Entry(data_frame, textvariable=color_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        color_entry.grid(row=1, column=1)

        year_text = tk.StringVar()
        year_label = tk.Label(data_frame, text='Car Year ', font=FONT_SIZE, bg=shared.BG_COLOR)
        year_label.grid(row=1, column=2, sticky=tk.E)
        year_entry = tk.Entry(data_frame, textvariable=year_text, font=FONT_SIZE,
                              bg=shared.LISTBOX_COLOR)
        year_entry.grid(row=1, column=3)

        price_text = tk.StringVar()
        price_label = tk.Label(data_frame, text='Car Price', font=FONT_SIZE, pady=20,
                               bg=shared.BG_COLOR)
        price_label.grid(row=2, column=0, sticky=tk.E)
        price_entry = tk.Entry(data_frame, textvariable=price_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        price_entry.grid(row=2, column=1)
        # -----LISTBOX------------------
        cols = ('ID', 'BRAND', 'MODEL', 'COLOR', 'YEAR', 'PRICE (PLN)')
        col_size = [(25, 25), (100, 100), (100, 100), (90, 90), (50, 50), (80, 80)]
        table = tkinter.ttk.Treeview(table_frame, columns=cols, show='headings', height=10)
        table.grid()

        for x, y in zip(cols, col_size):
            table.column(x, minwidth=y[0], width=y[1], anchor=tk.CENTER)
            table.heading(x, text=x)

        scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        scroll_x.configure(command=table.xview())

        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_y.configure(command=table.yview())
        scroll_y.grid(row=0, column=3, sticky='ns')

        table.configure(xscrollcommand=scroll_x.set)
        table.configure(yscrollcommand=scroll_y.set)
        table.bind('<ButtonRelease-1>', select_item)

        # buttons

        clear_btn = tk.Button(button_frame, text='Clear', width=12, command=clear_text,
                              bg=shared.BG_COLOR)
        clear_btn.grid(column=0, row=0, sticky=tk.W)

        display_btn = tk.Button(button_frame, text='Display', width=12, command=populate_list,
                                bg=shared.BG_COLOR)
        display_btn.grid(column=1, row=0, sticky=tk.W)

        search_btn = tk.Button(button_frame, text='Search', width=12, command=search_car,
                               bg=shared.BG_COLOR)
        search_btn.grid(column=2, row=0, sticky=tk.W)

        book_btn = tk.Button(button_frame, text='Book A Car', width=12, command=book_car,
                             bg=shared.BG_COLOR)
        book_btn.grid(column=3, row=0, sticky=tk.W)

        menu_btn = tk.Button(button_frame, text='My Transactions', width=12, command=my_trans,
                             bg=shared.BG_COLOR)
        menu_btn.grid(column=4, row=0, sticky=tk.W)

        edit_btn = tk.Button(button_frame, text='Edit Account', width=12,
                             command=edit_acc, bg=shared.BG_COLOR)
        edit_btn.grid(column=5, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12, command=i_exit_fun, bg=BG_BUTTON)
        exit_btn.grid(column=6, row=0, sticky=tk.W)

        DB_FIELDS = [year_text, price_text, brand_text, model_text, color_text]
        # commands

        populate_list()
