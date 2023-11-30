from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
cursor = conn.cursor()

class Payment: 
 
    def __init__(self, root): 
        self.root = root
        self.root.title("Step 4: Payment Options")
        self.root.geometry("500x500")
        self.center_window()  # Center the window on the screen
        self.root.configure(bg="#3498db")  # Blue background color
        
        self.f = Frame(root, height=500, width=500, bg="#3498db")  # Blue background color
        self.f.pack()

        self.l1 = Label(self.f, text='Payment Details', font=("Times New Roman", 20, "bold"), bg="#3498db", fg="black")  # Times New Roman font, larger size
        self.b1 = Button(self.f, text="Submit", command=self.display, bg="#2ecc71", fg="white")  # Green button
        self.l1.place(relx=0.5, rely=0.1, anchor="center")  # Center the label
        self.b1.place(relx=0.5, rely=0.6, anchor="center")  # Center the button

        # Radio buttons for online and offline payment
        self.payment_var = IntVar()
        self.online_radio = Radiobutton(self.f, text="Online", variable=self.payment_var, value=1, command=self.show_online_options, bg="#3498db", fg="black", font=("Times New Roman", 14))
        self.offline_radio = Radiobutton(self.f, text="Offline", variable=self.payment_var, value=2, command=self.show_offline_options, bg="#3498db", fg="black", font=("Times New Roman", 14))
        self.online_radio.place(relx=0.5, rely=0.35, anchor="center")  # Center the radio button
        self.offline_radio.place(relx=0.5, rely=0.45, anchor="center")  # Center the radio button

        # Dropdown menu for payment options
        self.payment_options = StringVar()
        self.payment_options.set("Select Payment Option")
        self.payment_menu = OptionMenu(self.f, self.payment_options, "")
        self.payment_menu.place(relx=0.5, rely=0.5, anchor="center")  # Center the dropdown below radio buttons
        self.payment_menu.config(state=DISABLED)

    def center_window(self):
        # Center the window on the screen
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry("+{}+{}".format(position_right, position_down))

    def show_online_options(self):
        self.payment_menu.config(state=NORMAL)
        options = ["Card", "Netbanking", "UPI"]
        self.payment_options.set(options[0])  # Default selection
        self.payment_menu['menu'].delete(0, 'end')  # Clear previous options
        for option in options:
            self.payment_menu['menu'].add_command(label=option, command=lambda value=option: self.payment_options.set(value))

    def show_offline_options(self):
        self.payment_menu.config(state=NORMAL)
        options = ["Cheque", "Cash"]
        self.payment_options.set(options[0])  # Default selection
        self.payment_menu['menu'].delete(0, 'end')  # Clear previous options
        for option in options:
            self.payment_menu['menu'].add_command(label=option, command=lambda value=option: self.payment_options.set(value))

    def display(self):
        payment_type = "Online" if self.payment_var.get() == 1 else "Offline"
        selected_option = self.payment_options.get()

        # Add your database insertion logic here using payment_type and selected_option
        try:
            # Your MySQL connection details
            conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
            cursor = conn.cursor()

            # Your MySQL insertion query
            query = "INSERT INTO payment (payment_type, payment_option) VALUES (%s, %s)"
            data = (payment_type, selected_option)
            cursor.execute(query, data)

            conn.commit()
            conn.close()

            print("Data Inserted")
            self.Display_Details()

        except Exception as e:
            print("Error:", e)
            conn.rollback()
        print("Data Inserted")
        conn.close()
        self.Display_Details()

    def Display_Details(self): 
        self.root.destroy() 
        # Add your code to navigate to the next page


root = Tk() 
obj = Payment(root) 
root.mainloop()
