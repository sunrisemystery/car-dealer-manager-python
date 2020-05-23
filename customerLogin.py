import tkinter as tk
import tkinter.messagebox
import customers_db
import carsDisplayer
import cars
import shared
import mainTest2

GEOMETRY_SIZE = '420x200'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class CustomerLogin:
    def __init__(self, cust_app):
        self.cust_app = cust_app
        self.cust_app.geometry(GEOMETRY_SIZE)
        self.cust_app.configure(bg=shared.BG_COLOR)
        self.cust_app.title('Customer Login Panel')

        db = customers_db.CustomersDatabase(DATABASE)

        # creating functions
        def clear_text():

            email_entry.delete(0, tk.END)
            access_key_entry.delete(0, tk.END)

        def add_cust():
            if email_text.get() == '' or access_key_text.get() == '':
                tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                return

            search_cust()

        def search_cust():

            row = db.search_user(email_text.get(), access_key_text.get())
            if not row:

                tkinter.messagebox.showerror("Error", "Wrong email or access key!")
                return
            else:
                row2 = db.is_admin(email_text.get(), access_key_text.get())

                if not row2:
                    tkinter.messagebox.showinfo("Login Successful", "Success!")

                    shared.logged_id = db.get_id(email_text.get(), access_key_text.get())

                    self.cust_app.destroy()
                    self.cust_app = tk.Tk()
                    carsDisplayer.CarsDisplayer(self.cust_app)
                    self.cust_app.mainloop()
                else:
                    tkinter.messagebox.showinfo("Login Successful", "Success! - Admin Permission")
                    self.cust_app.destroy()
                    self.cust_app = tk.Tk()
                    cars.Cars(self.cust_app)
                    self.cust_app.mainloop()

        def back():
            self.cust_app.destroy()
            self.cust_app = tk.Tk()
            mainTest2.MainTest(self.cust_app)

            self.cust_app.mainloop()

        def i_exit_fun():
            i_exit = tkinter.messagebox.askyesno("Registration Panel", "Do you want to exit?")
            if i_exit > 0:
                cust_app.destroy()
                return

        # Create window

        # frames
        main_frame = tk.Frame(self.cust_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        data_frame = tk.Frame(main_frame, bd=0, width=700, height=100, padx=50, relief=tk.RIDGE,
                              bg=shared.BG_COLOR)
        data_frame.pack(side=tk.TOP)
        button_frame = tk.Frame(main_frame, width=420, height=40, bd=1, padx=22,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        # part

        email_text = tk.StringVar()
        email_label = tk.Label(data_frame, text='Email', font=FONT_SIZE, pady=10, padx=10,
                               bg=shared.BG_COLOR)
        email_label.grid(row=1, column=0, sticky=tk.E)
        email_entry = tk.Entry(data_frame, textvariable=email_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        email_entry.grid(row=1, column=1)

        access_key_text = tk.StringVar()
        access_key_label = tk.Label(data_frame, text='Access Key', font=FONT_SIZE, pady=20,
                                    bg=shared.BG_COLOR)
        access_key_label.grid(row=2, column=0, sticky=tk.E)
        access_key_entry = tk.Entry(data_frame, textvariable=access_key_text, font=FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        access_key_entry.grid(row=2, column=1)

        # buttons

        add_btn = tk.Button(button_frame, text='Login', width=12, command=add_cust, padx=0,
                            bg=shared.BG_COLOR)
        add_btn.grid(column=0, row=0, sticky=tk.W)

        clear_btn = tk.Button(button_frame, text='Clear', width=12, command=clear_text,
                              bg=shared.BG_COLOR)
        clear_btn.grid(column=1, row=0, sticky=tk.W)

        menu_btn = tk.Button(button_frame, text='Menu', width=12, command=back, bg=shared.BG_COLOR)
        menu_btn.grid(column=2, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12, command=i_exit_fun,
                             bg=BG_BUTTON)
        exit_btn.grid(column=3, row=0, sticky=tk.W)
