import tkinter as tk
import tkinter.messagebox
import customers_db
import carsDisplayer
import shared
import mainTest2

GEOMETRY_SIZE = '600x200'
DATABASE = 'mydatavase.db'
FONT_SIZE = ('calibri', 12)
BG_BUTTON = 'HotPink3'


class CustomerEditAcc:
    def __init__(self, cust_app):
        self.cust_app = cust_app
        self.cust_app.geometry(GEOMETRY_SIZE)
        self.cust_app.configure(bg=shared.BG_COLOR)
        self.cust_app.title('Customer Edit Panel')

        db = customers_db.CustomersDatabase(DATABASE)
        customerdata = db.user_data(shared.logged_id)

        def update_cust():
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
                    tkinter.messagebox.showerror("Number can't include characters",
                                                 "Please write your number using.. numbers :)")
                    return
            except:
                tkinter.messagebox.showerror("Number can't include characters",
                                             "Please write your number using.. numbers :)")
                return
            if len(access_key_text.get()) < 3:
                tkinter.messagebox.showerror("Access key fail",
                                             "Access key must have at least 3 digits")
                return

            # TODO: nie dziala z list comprehension
            db.update(shared.logged_id, name_text.get().capitalize(),
                      lastname_text.get().capitalize(),
                      email_text.get(),
                      access_key_text.get(), phone_text.get())
            # db.update(shared.logged_id, *[f for f in TEXT_FIELDS_CAPITALIZED])
            tkinter.messagebox.showinfo("Update Successful", "Success!")

            self.cust_app.destroy()
            self.cust_app = tk.Tk()
            carsDisplayer.CarsDisplayer(self.cust_app)
            self.cust_app.mainloop()

        def back():
            self.cust_app.destroy()
            self.cust_app = tk.Tk()
            carsDisplayer.CarsDisplayer(self.cust_app)
            self.cust_app.mainloop()

        def delete_acc():
            important = tkinter.messagebox.askyesno("Registration Panel",
                                                    "Do you want to delete your account? You "
                                                    "can't undo this")
            if important > 0:
                db.remove(shared.logged_id)
                cust_app.destroy()
                return

        def back_menu():
            self.cust_app.destroy()
            self.cust_app = tk.Tk()
            mainTest2.MainTest(self.cust_app)

            self.cust_app.mainloop()

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
        name_text = tk.StringVar(value=customerdata[1])

        name_label = tk.Label(data_frame, text='Name', font=FONT_SIZE, pady=20, bg=shared.BG_COLOR)
        name_label.grid(row=0, column=0, sticky=tk.E)
        name_entry = tk.Entry(data_frame, textvariable=name_text, font=FONT_SIZE,
                              bg=shared.LISTBOX_COLOR)
        name_entry.grid(row=0, column=1)

        lastname_text = tk.StringVar(value=customerdata[2])

        lastname_label = tk.Label(data_frame, text='Lastname', font=FONT_SIZE, bg=shared.BG_COLOR)
        lastname_label.grid(row=0, column=2, sticky=tk.E, padx=(30, 0))
        lastname_entry = tk.Entry(data_frame, textvariable=lastname_text, font=FONT_SIZE,
                                  bg=shared.LISTBOX_COLOR)
        lastname_entry.grid(row=0, column=3)

        email_text = tk.StringVar(value=customerdata[3])

        email_label = tk.Label(data_frame, text='Email', font=FONT_SIZE, bg=shared.BG_COLOR)
        email_label.grid(row=1, column=0, sticky=tk.E)
        email_entry = tk.Entry(data_frame, textvariable=email_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        email_entry.grid(row=1, column=1)

        access_key_text = tk.StringVar(value=customerdata[4])

        access_key_label = tk.Label(data_frame, text='Access Key', font=FONT_SIZE,
                                    bg=shared.BG_COLOR)
        access_key_label.grid(row=1, column=2, sticky=tk.E)
        access_key_entry = tk.Entry(data_frame, textvariable=access_key_text, font=FONT_SIZE,
                                    bg=shared.LISTBOX_COLOR)
        access_key_entry.grid(row=1, column=3)

        phone_text = tk.StringVar(value=customerdata[6])

        phone_label = tk.Label(data_frame, text='Phone Number', font=FONT_SIZE, pady=20,
                               bg=shared.BG_COLOR)
        phone_label.grid(row=2, column=0, sticky=tk.E)
        phone_entry = tk.Entry(data_frame, textvariable=phone_text, font=FONT_SIZE,
                               bg=shared.LISTBOX_COLOR)
        phone_entry.grid(row=2, column=1)

        # buttons

        back_btn = tk.Button(button_frame, text='<Back', width=12, command=back, bg=shared.BG_COLOR)
        back_btn.grid(column=0, row=0, sticky=tk.W)

        add_btn = tk.Button(button_frame, text='Update Account', width=12, command=update_cust,
                            bg=shared.BG_COLOR)
        add_btn.grid(column=1, row=0, sticky=tk.W)

        delete_btn = tk.Button(button_frame, text='Delete Account', width=12, command=delete_acc,
                               bg=shared.BG_COLOR)
        delete_btn.grid(column=2, row=0, sticky=tk.W)

        exit_btn = tk.Button(button_frame, text='Log out', width=12,
                             command=back_menu, bg=BG_BUTTON)
        exit_btn.grid(column=3, row=0, sticky=tk.W)
        TEXT_FIELDS = [name_text, lastname_text, email_text, access_key_text, phone_text]
