import tkinter as tk
import tkinter.messagebox
import customers_db
import carsDisplayer
import shared
import mainTest2

GEOMETRY_SIZE = '650x200'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class CustomerRegister:
    def __init__(self, cust_app):
        self.cust_app = cust_app
        self.cust_app.geometry(GEOMETRY_SIZE)
        self.cust_app.configure(bg=shared.BG_COLOR)
        self.cust_app.title('Customer Registration Panel')

        db = customers_db.CustomersDatabase(DATABASE)

        # creating functions
        def clear_text():
            name_entry.delete(0, tk.END)
            lastname_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            access_key_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)

        def add_cust():
            for field in TEXT_FIELDS:
                if field.get() == '':
                    tkinter.messagebox.showerror("Required Fields", "Please include all fields")
                    return
            try:
                if not isinstance(int(access_key_text.get()), int):
                    tkinter.messagebox.showerror("Access Key can't be a text",
                                                 "Please write a numeric key")
                    return
            except:
                tkinter.messagebox.showerror("Access Key can't be a text",
                                             "Please write a numeric key")
                return

            try:
                if not isinstance(int(phone_text.get()), int):
                    tkinter.messagebox.showerror("Nuber can't include characters",
                                                 "Please write your number using.. numbers :)")
                    return
            except:
                tkinter.messagebox.showerror("Nuber can't include characters",
                                             "Please write your number using.. numbers :)")
                return
            if len(access_key_text.get()) < 3:
                tkinter.messagebox.showerror("Access key fail",
                                             "Access key must have at least 3 digits")
                return

            if search_cust() != -1:
                db.insert(name_text.get().capitalize(), lastname_text.get().capitalize(),
                          email_text.get(),
                          access_key_text.get(), phone_text.get())

                tkinter.messagebox.showinfo("Registration Successful", "Success!")
                shared.logged_id = db.get_id(email_text.get(), access_key_text.get())

                self.cust_app.destroy()
                self.cust_app = tk.Tk()
                carsDisplayer.CarsDisplayer(self.cust_app)
                self.cust_app.mainloop()

        def search_cust():

            for row in db.search_email(email_text.get()):
                if row:
                    tkinter.messagebox.showerror("Error", "This email is in this database")
                    return -1

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
        button_frame = tk.Frame(main_frame, width=735, height=40, bd=1, relief=tk.RIDGE,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.TOP)

        # part
        name_text = tk.StringVar()
        name_label = tk.Label(data_frame, text='Name', font=FONT_SIZE, pady=20, bg=shared.BG_COLOR)
        name_label.grid(row=0, column=0, sticky=tk.E)
        name_entry = tk.Entry(data_frame, textvariable=name_text, font=FONT_SIZE,
                              bg=shared.LISTBOX_COLOR)
        name_entry.grid(row=0, column=1)

        lastname_text = tk.StringVar()
        lastname_label = tk.Label(data_frame, text='Lastname', font=FONT_SIZE, bg=shared.BG_COLOR)
        lastname_label.grid(row=0, column=2, sticky=tk.E, padx=(30, 0))
        lastname_entry = tk.Entry(data_frame, textvariable=lastname_text, font=FONT_SIZE,
                                  bg=shared.LISTBOX_COLOR)
        lastname_entry.grid(row=0, column=3)

        email_text = tk.StringVar()
        email_label = tk.Label(data_frame, text='Email', font=FONT_SIZE, bg=shared.BG_COLOR)
        email_label.grid(row=1, column=0, sticky=tk.E)
        email_entry = tk.Entry(data_frame, textvariable=email_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        email_entry.grid(row=1, column=1)

        access_key_text = tk.StringVar()
        access_key_label = tk.Label(data_frame, text='Access Key', font=FONT_SIZE,
                                    bg=shared.BG_COLOR)
        access_key_label.grid(row=1, column=2, sticky=tk.E)
        access_key_entry = tk.Entry(data_frame, textvariable=access_key_text, font=FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        access_key_entry.grid(row=1, column=3)

        phone_text = tk.StringVar()
        phone_label = tk.Label(data_frame, text='Phone Number', font=FONT_SIZE, pady=20,
                               bg=shared.BG_COLOR)
        phone_label.grid(row=2, column=0, sticky=tk.E)
        phone_entry = tk.Entry(data_frame, textvariable=phone_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        phone_entry.grid(row=2, column=1)

        # buttons

        add_btn = tk.Button(button_frame, text='Create Account', width=12, command=add_cust,
                            bg=shared.BG_COLOR)
        add_btn.grid(column=0, row=0, sticky=tk.W)

        clear_btn = tk.Button(button_frame, text='Clear', width=12, command=clear_text,
                              bg=shared.BG_COLOR)
        clear_btn.grid(column=1, row=0, sticky=tk.W)

        menu_btn = tk.Button(button_frame, text='Menu', width=12, command=back, bg=shared.BG_COLOR)
        menu_btn.grid(column=2, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Exit', width=12,
                             command=i_exit_fun, bg=BG_BUTTON)
        exit_btn.grid(column=3, row=0, sticky=tk.W)
        TEXT_FIELDS = [name_text, lastname_text, email_text, access_key_text, phone_text]
