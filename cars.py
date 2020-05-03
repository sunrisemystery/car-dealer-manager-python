from tkinter import *
import tkinter.messagebox
from cars_db import CarsDatabase
import adminTransactionsGUI as atg


class Cars:
    def __init__(self,car_app):
        self.car_app=car_app
        self.car_app.geometry('750x450')
        self.car_app.title('Car Manager')


        db=CarsDatabase('mydatavase.db')
#creating functions
        def clear_text():
            brand_entry.delete(0, END)
            model_entry.delete(0, END)
            color_entry.delete(0, END)
            year_entry.delete(0, END)
            price_entry.delete(0, END)

        def populate_list():
            cars_list.delete(0,END)
            for row in db.fetch():
                 cars_list.insert(END,row)

        def add_car():
            if brand_text.get()=='' or model_text.get()=='' or color_text.get()=='' or year_text.get()=='' or price_text.get()=='':
                tkinter.messagebox.showerror( "Required Fields", "Please include all fields")
                return
            try:
                if isinstance(int(year_text.get()),int)==False:
                    tkinter.messagebox.showerror( "Year can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Year can't be a text", "Please write an integer")
                return

            try:
                if isinstance(float(price_text.get()),float)==False:
                    tkinter.messagebox.showerror( "Price can't be a text", "Please write an integer")
                    return
            except:
                tkinter.messagebox.showerror("Price can't be a text", "Please write an integer")
                return


            db.insert(brand_text.get().capitalize(),model_text.get().capitalize(),color_text.get().capitalize(),year_text.get(),price_text.get())

            #clear list
            cars_list.delete(0,END)
            cars_list.insert(END,(brand_text.get(),model_text.get(),color_text.get(),year_text.get(),price_text.get()))
            populate_list()
            clear_text()

        def select_item(event):
            global selected_item
            index=cars_list.curselection()[0]
            selected_item=cars_list.get(index)

            brand_entry.delete(0,END)
            brand_entry.insert(END, selected_item[1])

            model_entry.delete(0,END)
            model_entry.insert(END, selected_item[2])

            color_entry.delete(0,END)
            color_entry.insert(END, selected_item[3])

            year_entry.delete(0,END)
            year_entry.insert(END, selected_item[4])

            price_entry.delete(0,END)
            price_entry.insert(END, selected_item[6])

        def remove_car():
            if not cars_list.curselection():
                return
            try:
                db.remove(selected_item[0])
                clear_text()
                populate_list()
            except:
                pass
            
        def searchCar():
            cars_list.delete(0,END)
            for row in db.search(year_text.get(),price_text.get(),brand_text.get(),model_text.get(),color_text.get()):
                cars_list.insert(END,row)

        def update_car():
            try:
                db.update(selected_item[0],brand_text.get(),model_text.get(),color_text.get(),year_text.get(),price_text.get())
                populate_list()
            except:
                pass

        def iExit():
            iExit = tkinter.messagebox.askyesno("Car Dealer Management Database System", "Do you want to exit?")
            if iExit > 0:
                car_app.destroy()
                return
        def allTrans():
            cars_list.select_clear(END)

            self.car_app.destroy()
            self.car_app= Tk()
            application = atg.TransactionDisplayer(self.car_app)
            self.car_app.mainloop()







#Create window

#frames
        mainFrame=Frame(self.car_app)
        mainFrame.grid()

        dataFrame=Frame(mainFrame,bd=0,width=700,height=100,padx=100,relief=RIDGE)
        dataFrame.pack(side=TOP)
        buttonFrame=Frame(mainFrame,width=735,height=40,bd=1,relief=RIDGE)
        buttonFrame.pack(side=TOP)

        listboxFrame=Frame(mainFrame,bd=0,width=735,height=310,padx=80,pady=10,relief=RIDGE)
        listboxFrame.pack(side=TOP)

#part
        brand_text=StringVar()
        brand_label=Label(dataFrame,text='Brand Name',font=('calibri',12),pady=20)
        brand_label.grid(row=0,column=0,sticky=E)
        brand_entry=Entry(dataFrame,textvariable=brand_text,font=('calibri',12))
        brand_entry.grid(row=0,column=1)

        model_text=StringVar()
        model_label=Label(dataFrame,text='Model Name',font=('calibri',12))
        model_label.grid(row=0,column=2,sticky=E,padx=(30,0))
        model_entry=Entry(dataFrame,textvariable=model_text,font=('calibri',12))
        model_entry.grid(row=0,column=3)

        color_text=StringVar()
        color_label=Label(dataFrame,text='Car Color',font=('calibri',12))
        color_label.grid(row=1,column=0,sticky=E)
        color_entry=Entry(dataFrame,textvariable=color_text,font=('calibri',12))
        color_entry.grid(row=1,column=1)

        year_text=StringVar()
        year_label=Label(dataFrame,text='Car Year ',font=('calibri',12))
        year_label.grid(row=1,column=2,sticky=E)
        year_entry=Entry(dataFrame,textvariable=year_text,font=('calibri',12))
        year_entry.grid(row=1,column=3)

        price_text=StringVar()
        price_label=Label(dataFrame,text='Car Price',font=('calibri',12),pady=20)
        price_label.grid(row=2,column=0,sticky=E)
        price_entry=Entry(dataFrame,textvariable=price_text,font=('calibri',12))
        price_entry.grid(row=2,column=1)
#-----LISTBOX------------------
        cars_list=Listbox(listboxFrame,height=15,width=90)

        cars_list.grid(row=0,column=0,columnspan=3,rowspan=6)

        #creating scrollbar
        scrollbar=Scrollbar(listboxFrame)
        scrollbar.grid(row=3,column=3,sticky='ns')

        #set scroll to listbox

        cars_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=cars_list.yview)

        #bind select

        cars_list.bind('<<ListboxSelect>>',select_item)


        #buttons

        add_btn=Button(buttonFrame,text='Add Car',width=12,command=add_car)
        add_btn.grid(column=0,row=0,sticky=W)

        update_btn = Button(buttonFrame, text='Update', width=12,command=update_car)
        update_btn.grid(column=1, row=0, sticky=W)

        remove_btn = Button(buttonFrame, text='Remove', width=12,command=remove_car)
        remove_btn.grid(column=2, row=0, sticky=W)

        clear_btn = Button(buttonFrame, text='Clear', width=12,command=clear_text)
        clear_btn.grid(column=3, row=0, sticky=W)

        display_btn = Button(buttonFrame, text='Display', width=12,command=populate_list)
        display_btn.grid(column=4, row=0, sticky=W)
        
        search_btn = Button(buttonFrame, text='Search', width=12,command=searchCar)
        search_btn.grid(column=5, row=0, sticky=W)

        trans_btn = Button(buttonFrame, text='All Transactions', width=12,command=allTrans)
        trans_btn.grid(column=6, row=0, sticky=W)


        exit_btn = Button(buttonFrame, text='Exit', width=12,command=iExit,bg='firebrick2')
        exit_btn.grid(column=7, row=0, sticky=W)
#commands

        populate_list()



if __name__=="__main__":
    car_app=Tk()
    application=Cars(car_app)

    car_app.mainloop()
