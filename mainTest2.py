from tkinter import *
import customerLogin as cl
import customersRegister as cr



class MainTest:

    def __init__(self, mainapp):
        self.mainapp = mainapp
        self.mainapp.geometry('400x150')
        self.mainapp.title('Main Panel')



        def Login():

            self.mainapp.destroy()
            self.mainapp=Tk()
            application=cl.CustomerLogin(self.mainapp)

            self.mainapp.mainloop()


        def Register():
            self.mainapp.destroy()
            self.mainapp=Tk()
            application=cr.CustomerRegister(self.mainapp)
            self.mainapp.mainloop()





        mainFrame = Frame(self.mainapp)
        mainFrame.grid()

        labelFrame=Frame(mainFrame,bd=0,relief=RIDGE,width=440,height=60,padx=100,pady=10,bg='light grey')
        labelFrame.pack(side=TOP)

        buttonFrame=Frame(mainFrame,bd=0,width=400,height=100,padx=20,pady=30)
        buttonFrame.pack(side=BOTTOM)

        label=Label(labelFrame,text="Customer Login and Registration Panel",bg='light grey')
        label.grid(row=0,column=0)
        cars_btn = Button(buttonFrame, text='Register', width=12,padx=3, command=Register)
        cars_btn.grid(column=9, row=5)


        login_btn=Button(buttonFrame, text='Login', width=12, command=Login)
        login_btn.grid(column=6,row=5)


if __name__=="__main__":
    car_app=Tk()
    application=MainTest(car_app)

    car_app.mainloop()

