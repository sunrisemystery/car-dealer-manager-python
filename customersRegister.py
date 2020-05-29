"""Defines class responsible for registration to the app. """
import tkinter as tk
import tkinter.messagebox

import carsDisplayer
import customerLogin
import customers_db
import shared

GEOMETRY_SIZE = '650x200'


class CustomerRegister(customerLogin.CustomerBase):
    """This class displays Customer Registration Panel and contains
        functionality for buttons."""

    def __init__(self, customer_app):
        """Inits CustomerRegister."""
        self.customer_app = customer_app
        self.customer_app.geometry(GEOMETRY_SIZE)
        self.customer_app.configure(bg=shared.BG_COLOR)
        self.customer_app.title('Customer Registration Panel')
        self.name_entry = None
        self.lastname_entry = None
        self.email_entry = None
        self.access_key_entry = None
        self.phone_entry = None

        self.name_text = tk.StringVar()
        self.lastname_text = tk.StringVar()
        self.email_text = tk.StringVar()
        self.access_key_text = tk.StringVar()
        self.phone_text = tk.StringVar()

        self.text_fields = [self.name_text, self.lastname_text, self.email_text,
                            self.access_key_text, self.phone_text]

        self.d_base = customers_db.CustomersDatabase(shared.DATABASE)

    def clear_text(self):
        """Clears all entries."""
        self.name_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.access_key_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def add_customer(self):
        """Adds customer and checks if given data are correct. """
        for field in self.text_fields:
            if not field.get():
                tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                return
        try:
            if not isinstance(int(self.access_key_text.get()), int):
                tkinter.messagebox.showerror("Access Key can't be a text",
                                             "Please write a numeric key")
                return
        except ValueError:
            tkinter.messagebox.showerror("Access Key can't be a text",
                                         "Please write a numeric key")
            return

        try:
            if not isinstance(int(self.phone_text.get()), int):
                tkinter.messagebox.showerror("Number can't include characters",
                                             "Please write your number using.. numbers :)")
                return
        except ValueError:
            tkinter.messagebox.showerror("Number can't include characters",
                                         "Please write your number using.. numbers :)")
            return
        if len(self.access_key_text.get()) < shared.ACCESS_KEY_LENGTH:
            tkinter.messagebox.showerror("Access key fail",
                                         "Access key must have at least 3 digits")
            return

        if self.search_customer() != -1:
            self.d_base.insert(self.name_text.get().capitalize(),
                               self.lastname_text.get().capitalize(),
                               self.email_text.get(),
                               self.access_key_text.get(), self.phone_text.get())

            tkinter.messagebox.showinfo("Registration Successful", "Success!")
            shared.LOGGED_ID = self.d_base.get_id(self.email_text.get(), self.access_key_text.get())

            self.customer_app.destroy()
            self.customer_app = tk.Tk()
            car_display_window = carsDisplayer.CarsDisplayer(self.customer_app)
            car_display_window.init_window()
            car_display_window.populate_list()
            self.customer_app.mainloop()

    def search_customer(self):
        """Checks if user with given email exists in database."""
        for row in self.d_base.search_email(self.email_text.get()):
            if row:
                tkinter.messagebox.showerror("Error", "This email is in this database")
                return -1
            return None

    def init_window(self):
        """Inits window and labels."""
        # frames
        main_frame = tk.Frame(self.customer_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=50, relief=tk.RIDGE,
                              bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=735, height=40, bd=1, relief=tk.RIDGE,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        # entries

        name_label = tk.Label(data_frame, text='Name', font=shared.FONT_SIZE, pady=20,
                              bg=shared.BG_COLOR)
        name_label.grid(row=0, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(data_frame, textvariable=self.name_text, font=shared.FONT_SIZE,
                                   bg=shared.LISTBOX_COLOR)
        self.name_entry.grid(row=0, column=1)

        lastname_label = tk.Label(data_frame, text='Lastname', font=shared.FONT_SIZE,
                                  bg=shared.BG_COLOR)
        lastname_label.grid(row=0, column=2, sticky=tk.E, padx=(30, 0))
        self.lastname_entry = tk.Entry(data_frame, textvariable=self.lastname_text,
                                       font=shared.FONT_SIZE, bg=shared.LISTBOX_COLOR)
        self.lastname_entry.grid(row=0, column=3)

        email_label = tk.Label(data_frame, text='Email', font=shared.FONT_SIZE, bg=shared.BG_COLOR)
        email_label.grid(row=1, column=0, sticky=tk.E)
        self.email_entry = tk.Entry(data_frame, textvariable=self.email_text, font=shared.FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        self.email_entry.grid(row=1, column=1)

        access_key_label = tk.Label(data_frame, text='Access Key', font=shared.FONT_SIZE,
                                    bg=shared.BG_COLOR)
        access_key_label.grid(row=1, column=2, sticky=tk.E)
        self.access_key_entry = tk.Entry(data_frame, textvariable=self.access_key_text,
                                         font=shared.FONT_SIZE, bg=shared.LISTBOX_COLOR)
        self.access_key_entry.grid(row=1, column=3)

        phone_label = tk.Label(data_frame, text='Phone Number', font=shared.FONT_SIZE, pady=20,
                               bg=shared.BG_COLOR)
        phone_label.grid(row=2, column=0, sticky=tk.E)
        self.phone_entry = tk.Entry(data_frame, textvariable=self.phone_text, font=shared.FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        self.phone_entry.grid(row=2, column=1)

        # buttons

        add_button = tk.Button(button_frame, text='Create Account', width=12,
                               command=self.add_customer, bg=shared.BG_COLOR)
        add_button.grid(column=0, row=0, sticky=tk.W)

        clear_button = tk.Button(button_frame, text='Clear', width=12, command=self.clear_text,
                                 bg=shared.BG_COLOR)
        clear_button.grid(column=1, row=0, sticky=tk.W)

        menu_button = tk.Button(button_frame, text='Menu', width=12, command=self.back,
                                bg=shared.BG_COLOR)
        menu_button.grid(column=2, row=0, sticky=tk.W)

        exit_button = tk.Button(button_frame, text='Exit', width=12,
                                command=self.exit, bg=shared.BG_BUTTON)
        exit_button.grid(column=3, row=0, sticky=tk.W)
