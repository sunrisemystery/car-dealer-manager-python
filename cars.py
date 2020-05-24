"""Defines class responsible for Car Manager Window for Admin. """

import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
import cars_db
import adminTransactionsGUI
import shared

GEOMETRY_SIZE = '750x450'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class Cars:
    """This class displays Car Manager Window for Admin and contains
        functionality for buttons."""

    def __init__(self, car_app):
        """Inits Cars."""
        self.car_app = car_app
        self.car_app.geometry(GEOMETRY_SIZE)
        self.car_app.title('Car Manager')
        self.car_app.configure(bg=shared.BG_COLOR)

        db = cars_db.CarsDatabase(DATABASE)

        def clear_text():
            """Clears all entries."""
            brand_entry.delete(0, tk.END)
            model_entry.delete(0, tk.END)
            color_entry.delete(0, tk.END)
            year_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)

        def populate_list():
            """Displays all cars which are in database."""
            for i in table.get_children():
                table.delete(i)
            for row in db.fetch():
                table.insert('', tk.END,
                             values=[row[0], row[1], row[2], row[3], row[4], row[5],
                                     row[6]])

        def add_car():
            """Adds a car to database."""
            for field in TEXT_FIELDS:
                if field.get() == '':
                    tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                    return
            try:
                if not isinstance(int(year_text.get()), int):
                    tkinter.messagebox.showerror("Year can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Year can't be a text", "Please write an integer")
                return

            try:
                if not isinstance(float(price_text.get()), float):
                    tkinter.messagebox.showerror("Price can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Price can't be a text", "Please write an integer")
                return

            db.insert(*[f.get().capitalize() for f in TEXT_FIELDS])

            # clear list
            for i in table.get_children():
                table.delete(i)

            populate_list()
            clear_text()

        def select_item_fun(event):
            """Fills fields with selected car's data."""
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

        def remove_car():
            """Removes car from database and updates listbox."""
            if not table.selection() != ():
                return
            try:
                db.remove(selected_item[cols[0]])
                clear_text()
                populate_list()
            except:
                pass

        def search_car():
            """Displays cars that met given criteria. """
            for i in table.get_children():
                table.delete(i)

            for row in db.search(*[f.get() for f in DB_FIELDS]):
                table.insert('', tk.END,
                             values=[row[0], row[1], row[2], row[3], row[4], row[5],
                                     row[6]])

        def update_car():
            """Updates car's data."""
            for field in TEXT_FIELDS:
                if field.get() == '':
                    tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                    return
            try:
                if not isinstance(int(year_text.get()), int):
                    tkinter.messagebox.showerror("Year can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Year can't be a text", "Please write an integer")
                return

            try:
                if not isinstance(float(price_text.get()), float):
                    tkinter.messagebox.showerror("Price can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Price can't be a text", "Please write an integer")
                return
            try:
                db.update(selected_item[cols[0]], *[f.get().capitalize() for f in TEXT_FIELDS])
                populate_list()
            except:
                pass

        def i_exit_fun():
            """Finishes program."""
            i_exit = tkinter.messagebox.askyesno("Car Dealer Management Database System",
                                                 "Do you want to exit?")
            if i_exit > 0:
                car_app.destroy()
                return

        def all_trans():
            """Turns to Transactions Panel."""

            self.car_app.destroy()
            self.car_app = tk.Tk()
            adminTransactionsGUI.TransactionDisplayer(self.car_app)
            self.car_app.mainloop()

        # Creating window

        # frames
        main_frame = tk.Frame(self.car_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=100, relief=tk.RIDGE,
                              bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=735, height=40, bd=1, relief=tk.RIDGE,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        table_frame = tk.Frame(main_frame, bd=0, width=735, height=310, padx=80, pady=10,
                               relief=tk.RIDGE, bg=shared.BG_COLOR)
        table_frame.pack(side=tk.TOP)

        # entries
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
        # creating table

        cols = ('ID', 'BRAND', 'MODEL', 'COLOR', 'YEAR', 'AVAILABLE (0/1)', 'PRICE (PLN)')
        col_size = [(25, 25), (100, 100), (100, 100), (90, 90), (50, 50), (100, 100), (80, 80)]
        table = tkinter.ttk.Treeview(table_frame, columns=cols, show='headings', height=10)

        table.grid()

        for x, y in zip(cols, col_size):
            table.column(x, minwidth=y[0], width=y[1], anchor=tk.CENTER)
            table.heading(x, text=x)

        scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_y.configure(command=table.yview())
        scroll_y.grid(row=0, column=3, sticky='ns')

        table.configure(yscrollcommand=scroll_y.set)
        table.bind('<ButtonRelease-1>', select_item_fun)

        # buttons

        add_btn = tk.Button(button_frame, text='Add Car', width=12, command=add_car,
                            bg=shared.BG_COLOR)
        add_btn.grid(column=0, row=0, sticky=tk.W)

        update_btn = tk.Button(button_frame, text='Update', width=12, command=update_car,
                               bg=shared.BG_COLOR)
        update_btn.grid(column=1, row=0, sticky=tk.W)

        remove_btn = tk.Button(button_frame, text='Remove', width=12, command=remove_car,
                               bg=shared.BG_COLOR)
        remove_btn.grid(column=2, row=0, sticky=tk.W)

        clear_btn = tk.Button(button_frame, text='Clear', width=12, command=clear_text,
                              bg=shared.BG_COLOR)
        clear_btn.grid(column=3, row=0, sticky=tk.W)

        display_btn = tk.Button(button_frame, text='Display', width=12, command=populate_list,
                                bg=shared.BG_COLOR)
        display_btn.grid(column=4, row=0, sticky=tk.W)

        search_btn = tk.Button(button_frame, text='Search', width=12, command=search_car,
                               bg=shared.BG_COLOR)
        search_btn.grid(column=5, row=0, sticky=tk.W)

        trans_btn = tk.Button(button_frame, text='All Transactions', width=12, command=all_trans,
                              bg=shared.BG_COLOR)
        trans_btn.grid(column=6, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12, command=i_exit_fun,
                             bg=BG_BUTTON)
        exit_btn.grid(column=7, row=0, sticky=tk.W)

        TEXT_FIELDS = [brand_text, model_text, color_text, year_text, price_text]
        DB_FIELDS = [year_text, price_text, brand_text, model_text, color_text]

        # commands

        populate_list()
