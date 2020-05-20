import tkinter as tk
from tkinter import messagebox
import cars_db
import adminTransactionsGUI
import shared

GEOMETRY_SIZE = '750x450'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class Cars:
    def __init__(self, car_app):
        self.car_app = car_app
        self.car_app.geometry(GEOMETRY_SIZE)
        self.car_app.title('Car Manager')
        self.car_app.configure(bg=shared.BG_COLOR)

        db = cars_db.CarsDatabase(DATABASE)

        # creating functions
        def clear_text():
            brand_entry.delete(0, tk.END)
            model_entry.delete(0, tk.END)
            color_entry.delete(0, tk.END)
            year_entry.delete(0, tk.END)
            price_entry.delete(0, tk.END)

        def populate_list():
            cars_list.delete(0, tk.END)
            for row in db.fetch():
                cars_list.insert(tk.END, row)

        def add_car():
            for field in TEXT_FIELDS:
                if field.get() == '':
                    messagebox.showerror("Required Fields", "Please include all fields")
                    return
            try:
                if not isinstance(int(year_text.get()), int):
                    messagebox.showerror("Year can't be a text", "Please write an integer")
                    return
            except:
                messagebox.showerror("Year can't be a text", "Please write an integer")
                return

            try:
                if not isinstance(float(price_text.get()), float):
                    messagebox.showerror("Price can't be a text", "Please write an integer")
                    return
            except:
                messagebox.showerror("Price can't be a text", "Please write an integer")
                return

            db.insert(*[f.get().capitalize() for f in TEXT_FIELDS])

            # clear list
            cars_list.delete(0, tk.END)
            cars_list.insert(tk.END, *[f.get() for f in TEXT_FIELDS])
            populate_list()
            clear_text()

        def select_item_fun(event):
            global selected_item

            index = cars_list.curselection()[0]
            selected_item = cars_list.get(index)

            brand_entry.delete(0, tk.END)
            brand_entry.insert(tk.END, selected_item[1])

            model_entry.delete(0, tk.END)
            model_entry.insert(tk.END, selected_item[2])

            color_entry.delete(0, tk.END)
            color_entry.insert(tk.END, selected_item[3])

            year_entry.delete(0, tk.END)
            year_entry.insert(tk.END, selected_item[4])

            price_entry.delete(0, tk.END)
            price_entry.insert(tk.END, selected_item[6])

        def remove_car():
            if not cars_list.curselection():
                return
            try:
                db.remove(selected_item[0])
                clear_text()
                populate_list()
            except:
                pass

        def search_car():
            cars_list.delete(0, tk.END)
            for row in db.search(year_text.get(), price_text.get(), brand_text.get(),
                                 model_text.get(), color_text.get()):
                cars_list.insert(tk.END, row)

        def update_car():
            try:
                db.update(selected_item[0], brand_text.get(), model_text.get(),
                          color_text.get(), year_text.get(), price_text.get())
                populate_list()
            except:
                pass

        def i_exit_fun():
            i_exit = messagebox.askyesno("Car Dealer Management Database System",
                                         "Do you want to exit?")
            if i_exit > 0:
                car_app.destroy()
                return

        def all_trans():
            cars_list.select_clear(tk.END)

            self.car_app.destroy()
            self.car_app = tk.Tk()
            adminTransactionsGUI.TransactionDisplayer(self.car_app)
            self.car_app.mainloop()

        # Create window

        # frames
        main_frame = tk.Frame(self.car_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=100, relief=tk.RIDGE,bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=735, height=40, bd=1, relief=tk.RIDGE,bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        listbox_frame = tk.Frame(main_frame, bd=0, width=735, height=310, padx=80, pady=10,
                                 relief=tk.RIDGE,bg=shared.BG_COLOR)
        listbox_frame.pack(side=tk.TOP)

        # part
        brand_text = tk.StringVar()
        brand_label = tk.Label(data_frame, text='Brand Name', font=FONT_SIZE, pady=20,bg=shared.BG_COLOR)
        brand_label.grid(row=0, column=0, sticky=tk.E)
        brand_entry = tk.Entry(data_frame, textvariable=brand_text, font=FONT_SIZE,bg=shared.LISTBOX_COLOR)
        brand_entry.grid(row=0, column=1)

        model_text = tk.StringVar()
        model_label = tk.Label(data_frame, text='Model Name', font=FONT_SIZE,bg=shared.BG_COLOR)
        model_label.grid(row=0, column=2, sticky=tk.E, padx=(30, 0))
        model_entry = tk.Entry(data_frame, textvariable=model_text, font=FONT_SIZE,bg=shared.LISTBOX_COLOR)
        model_entry.grid(row=0, column=3)

        color_text = tk.StringVar()
        color_label = tk.Label(data_frame, text='Car Color', font=FONT_SIZE,bg=shared.BG_COLOR)
        color_label.grid(row=1, column=0, sticky=tk.E)
        color_entry = tk.Entry(data_frame, textvariable=color_text, font=FONT_SIZE,bg=shared.LISTBOX_COLOR)
        color_entry.grid(row=1, column=1)

        year_text = tk.StringVar()
        year_label = tk.Label(data_frame, text='Car Year ', font=FONT_SIZE,bg=shared.BG_COLOR)
        year_label.grid(row=1, column=2, sticky=tk.E)
        year_entry = tk.Entry(data_frame, textvariable=year_text, font=FONT_SIZE,bg=shared.LISTBOX_COLOR)
        year_entry.grid(row=1, column=3)

        price_text = tk.StringVar()
        price_label = tk.Label(data_frame, text='Car Price', font=FONT_SIZE, pady=20,bg=shared.BG_COLOR)
        price_label.grid(row=2, column=0, sticky=tk.E)
        price_entry = tk.Entry(data_frame, textvariable=price_text, font=FONT_SIZE,bg=shared.LISTBOX_COLOR)
        price_entry.grid(row=2, column=1)
        # -----LISTBOX------------------
        cars_list = tk.Listbox(listbox_frame, height=15, width=90,bg=shared.LISTBOX_COLOR)

        cars_list.grid(row=0, column=0, columnspan=3, rowspan=6)

        # creating scrollbar
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.grid(row=3, column=3, sticky='ns')

        # set scroll to listbox

        cars_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=cars_list.yview)

        # bind select

        cars_list.bind('<<ListboxSelect>>', select_item_fun)

        # buttons

        add_btn = tk.Button(button_frame, text='Add Car', width=12, command=add_car,bg=shared.BG_COLOR)
        add_btn.grid(column=0, row=0, sticky=tk.W)

        update_btn = tk.Button(button_frame, text='Update', width=12, command=update_car,bg=shared.BG_COLOR)
        update_btn.grid(column=1, row=0, sticky=tk.W)

        remove_btn = tk.Button(button_frame, text='Remove', width=12, command=remove_car,bg=shared.BG_COLOR)
        remove_btn.grid(column=2, row=0, sticky=tk.W)

        clear_btn = tk.Button(button_frame, text='Clear', width=12, command=clear_text,bg=shared.BG_COLOR)
        clear_btn.grid(column=3, row=0, sticky=tk.W)

        display_btn = tk.Button(button_frame, text='Display', width=12, command=populate_list,bg=shared.BG_COLOR)
        display_btn.grid(column=4, row=0, sticky=tk.W)

        search_btn = tk.Button(button_frame, text='Search', width=12, command=search_car,bg=shared.BG_COLOR)
        search_btn.grid(column=5, row=0, sticky=tk.W)

        trans_btn = tk.Button(button_frame, text='All Transactions', width=12, command=all_trans,bg=shared.BG_COLOR)
        trans_btn.grid(column=6, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12, command=i_exit_fun,
                             bg=BG_BUTTON)
        exit_btn.grid(column=7, row=0, sticky=tk.W)

        TEXT_FIELDS = [brand_text, model_text, color_text, year_text, price_text]
        # commands

        populate_list()


if __name__ == "__main__":
    car_app2 = tk.Tk()
    application = Cars(car_app2)

    car_app2.mainloop()
