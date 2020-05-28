"""Defines class responsible for log in to the application. """
import tkinter as tk
import tkinter.messagebox
import customers_db
import carsDisplayer
import mainTest2
import cars
import shared

GEOMETRY_SIZE = '420x200'


class CustomerBase:
    """Base class for displaying customers."""

    def __init__(self, customer_app):
        self.customer_app = customer_app

    def back(self):
        """Turns back to login/registration panel."""
        self.customer_app.destroy()
        self.customer_app = tk.Tk()
        main_window = mainTest2.MainTest(self.customer_app)
        main_window.window_init()

        self.customer_app.mainloop()

    def exit_fun(self):
        """Finishes program."""
        i_exit = tkinter.messagebox.askyesno("Registration Panel", "Do you want to exit?")
        if i_exit > 0:
            self.customer_app.destroy()
            return


class CustomerLogin(CustomerBase):
    """This class displays Customer Login Panel and contains
        functionality for buttons."""

    def __init__(self, customer_app):
        """Inits CustomerLogin."""
        super().__init__(customer_app)
        self.customer_app.geometry(GEOMETRY_SIZE)
        self.customer_app.configure(bg=shared.BG_COLOR)
        self.customer_app.title('Customer Login Panel')

        self.d_base = customers_db.CustomersDatabase(shared.DATABASE)
        self.email_entry = None
        self.access_key_entry = None

        self.email_text = tk.StringVar()
        self.access_key_text = tk.StringVar()

    def clear_text(self):
        """Clears all entries."""
        self.email_entry.delete(0, tk.END)
        self.access_key_entry.delete(0, tk.END)

    def add_customer(self):
        """Checks if all fields are filled."""
        if not self.email_text.get() or not self.access_key_text.get():
            tkinter.messagebox.showerror("Required Fields", "Please include all fields")
            return

        self.search_customer()

    def search_customer(self):
        """Checks if user is an admin or a customer and redirects user to specific window. """
        row = self.d_base.search_user(self.email_text.get(), self.access_key_text.get())
        if not row:

            tkinter.messagebox.showerror("Error", "Wrong email or access key!")
            return
        else:
            row_2 = self.d_base.is_admin(self.email_text.get(), self.access_key_text.get())

            if not row_2:
                tkinter.messagebox.showinfo("Login Successful", "Success!")

                shared.LOGGED_ID = self.d_base.get_id(self.email_text.get(),
                                                      self.access_key_text.get())

                self.customer_app.destroy()
                self.customer_app = tk.Tk()
                car_display_window = carsDisplayer.CarsDisplayer(self.customer_app)
                car_display_window.init_window()
                car_display_window.populate_list()
                self.customer_app.mainloop()
            else:
                tkinter.messagebox.showinfo("Login Successful", "Success! - Admin Permission")
                self.customer_app.destroy()
                self.customer_app = tk.Tk()
                admin_display = cars.Cars(self.customer_app)
                admin_display.init_window()
                admin_display.populate_list()
                self.customer_app.mainloop()

    def init_window(self):
        """Inits frames and labels."""
        # frames
        main_frame = tk.Frame(self.customer_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=50, relief=tk.RIDGE,
                              bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=420, height=40, bd=1, padx=22,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        email_label = tk.Label(data_frame, text='Email', font=shared.FONT_SIZE, pady=10, padx=10,
                               bg=shared.BG_COLOR)
        email_label.grid(row=1, column=0, sticky=tk.E)
        self.email_entry = tk.Entry(data_frame, textvariable=self.email_text, font=shared.FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        self.email_entry.grid(row=1, column=1)

        access_key_label = tk.Label(data_frame, text='Access Key', font=shared.FONT_SIZE, pady=20,
                                    bg=shared.BG_COLOR)
        access_key_label.grid(row=2, column=0, sticky=tk.E)
        self.access_key_entry = tk.Entry(data_frame, textvariable=self.access_key_text,
                                         font=shared.FONT_SIZE, bg=shared.LISTBOX_COLOR)
        self.access_key_entry.grid(row=2, column=1)

        # buttons

        add_button = tk.Button(button_frame, text='Login', width=12, command=self.add_customer,
                               padx=0, bg=shared.BG_COLOR)
        add_button.grid(column=0, row=0, sticky=tk.W)

        clear_button = tk.Button(button_frame, text='Clear', width=12, command=self.clear_text,
                                 bg=shared.BG_COLOR)
        clear_button.grid(column=1, row=0, sticky=tk.W)

        menu_button = tk.Button(button_frame, text='Menu', width=12, command=self.back,
                                bg=shared.BG_COLOR)
        menu_button.grid(column=2, row=0, sticky=tk.W)

        exit_button = tk.Button(button_frame, text='Exit', width=12, command=self.exit_fun,
                                bg=shared.BG_BUTTON)
        exit_button.grid(column=3, row=0, sticky=tk.W)
