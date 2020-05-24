"""Defines class responsible for Main Panel Window. """
import tkinter as tk
import customerLogin
import customersRegister
import shared

GEOMETRY_SIZE = '400x150'


class MainTest:
    """This class displays Main Panel Window for customer and contains
        functionality for buttons."""

    def __init__(self, main_app):
        """Inits MainTest."""
        self.main_app = main_app
        self.main_app.geometry(GEOMETRY_SIZE)
        self.main_app.title('Main Panel')
        self.main_app.configure(bg=shared.BG_COLOR)
        self.application = 0

        def login():
            """Displays Login Window."""
            self.main_app.destroy()
            self.main_app = tk.Tk()
            self.application = customerLogin.CustomerLogin(self.main_app)

            self.main_app.mainloop()

        def register():
            """Displays Registration Window."""
            self.main_app.destroy()
            self.main_app = tk.Tk()
            self.application = customersRegister.CustomerRegister(self.main_app)
            self.main_app.mainloop()

        main_frame = tk.Frame(self.main_app)
        main_frame.configure(bg=shared.BG_COLOR)
        main_frame.grid()

        label_frame = tk.Frame(main_frame, bd=0, relief=tk.RIDGE, width=440, height=60,
                               padx=100, pady=10, bg=shared.BG_COLOR2)

        label_frame.pack(side=tk.TOP)

        button_frame = tk.Frame(main_frame, bd=0, width=400, height=100, padx=20, pady=30,
                                bg=shared.BG_COLOR)
        button_frame.pack(side=tk.BOTTOM)

        label = tk.Label(label_frame, text="Customer Login and Registration Panel",
                         bg=shared.BG_COLOR2)
        label.grid(row=0, column=0)
        cars_btn = tk.Button(button_frame, text='Register', width=12, padx=3, command=register,
                             bg=shared.BG_COLOR)
        cars_btn.grid(column=9, row=5)

        login_btn = tk.Button(button_frame, text='Login', width=12, command=login,
                              bg=shared.BG_COLOR)
        login_btn.grid(column=6, row=5)


if __name__ == "__main__":
    car_app = tk.Tk()
    application = MainTest(car_app)

    car_app.mainloop()
