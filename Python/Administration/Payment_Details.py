from tkinter import *
import mysql.connector
import uuid
 
conn = mysql.connector.connect(user='root', password='%Rachit404%', host='localhost', database='insurance_company')
cursor = conn.cursor()
 
class Payment:
 
    def __init__(self, root):
        self.root = root
        self.root.title("Step 4: Payment Options")
        self.root.geometry("700x700")  # Increased height for the table
        self.center_window()
        self.root.configure(bg="#e67e22")  # Orange background color
 
        self.background_image = PhotoImage(file="Insurance-System/images/blue.png")  # Replace with your background image path

        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.95)
        
        self.f = Frame(root, bg="#E0F4FF", highlightbackground="#000", bd=5, relief=SOLID)  # Orange background color
        self.f.place(relx=0.5, rely=0.5, anchor="center")
 
        # Company Name Heading
        self.company_heading = Label(root, text='Car Insurance Company', font=("Times New Roman", 36, "bold"), bg="#0081B3", fg="#000")
        self.company_heading.place(relx=0.505, rely=0.1, anchor="center")
 
        # Fetching insurance amount from the database
        self.bill_amount = self.get_insurance_amount()
        self.gst_percentage = 18  # Replace with your actual GST percentage
 
        # Calculating GST and Final Amount
        gst_amount = (self.bill_amount * self.gst_percentage) / 100
        self.final_amount = int(self.bill_amount + gst_amount)
 
        # Bill Details Label
        self.bill_details_label = Label(self.f, text='Bill Details', font=("Times New Roman", 30, "bold", "italic"), bg="#E0F4FF", fg="black")
        self.bill_details_label.grid(row=1, column=0, columnspan=2, pady=10)
 
        # Bill Details Frame
        self.bill_frame = Frame(self.f, bg="#E0F4FF")  # Blue background color
        self.bill_frame.grid(row=2, column=0, columnspan=2, pady=20, padx=50)
 
        # Bill Details
        self.bill_amount_label = Label(self.bill_frame, text=f'Amount: ', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")  # Blue background color
        self.bill_amount_label.grid(row=0, column=0, sticky="w", pady=5)
 
        self.bill_amount_value_label = Label(self.bill_frame, text=f'₹ {self.bill_amount:.2f}', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")  # Blue background color
        self.bill_amount_value_label.grid(row=0, column=1, sticky="w", pady=5)
 
        self.gst_label = Label(self.bill_frame, text=f'GST ({self.gst_percentage}%): ', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")  # Blue background color
        self.gst_label.grid(row=1, column=0, sticky="w", pady=5)
 
        self.gst_value_label = Label(self.bill_frame, text=f' ₹ {gst_amount:.2f}', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")  # Blue background color
        self.gst_value_label.grid(row=1, column=1, sticky="w", pady=5)
 
        self.final_amount_label = Label(self.bill_frame, text=f'Total Amount: ', font=("Times New Roman", 14, "bold"), bg="#E0F4FF", fg="black")  # Blue background color
        self.final_amount_label.grid(row=2, column=0, sticky="w", pady=5)
 
        self.final_amount_value_label = Label(self.bill_frame, text=f'₹ {self.final_amount}', font=("Times New Roman", 14, "bold"), bg="#E0F4FF", fg="black")  # Blue background color
        self.final_amount_value_label.grid(row=2, column=1, sticky="w", pady=5)
 
        # Online/Offline Buttons
        self.payment_var = IntVar()
        self.online_radio = Radiobutton(self.bill_frame, text="Online", variable=self.payment_var, value=1, command=self.show_online_options, bg="#E0F4FF", fg="black", font=("Times New Roman", 14))  # Blue background color
        self.offline_radio = Radiobutton(self.bill_frame, text="Offline", variable=self.payment_var, value=2, command=self.show_offline_options, bg="#E0F4FF", fg="black", font=("Times New Roman", 14))  # Blue background color
        self.online_radio.grid(row=3, column=0, pady=10, sticky='w')
        self.offline_radio.grid(row=3, column=1, pady=10, sticky='w')
 
        # Payment Options Dropdown
        self.payment_options = StringVar()
        self.payment_menu = OptionMenu(self.bill_frame, self.payment_options, "")
        self.payment_menu.grid(row=4, column=0, columnspan=2, pady=5, sticky='ew')
        self.payment_menu.config(state=DISABLED)
 
        # Submit Button
        self.b1 = Button(self.f, text="Submit", command=self.display, font=("Times", 16, "bold"), bg="#525FE1", fg="#FFF6F4")
        self.b1.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")  # Changed sticky to "n" for centering below the table

        file_path = "Insurance-System\Python\Administration\custid.txt"
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            cus_id = file.read(-1)
            
    def center_window(self):
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.geometry("+{}+{}".format(position_right, position_down))
 
    def get_insurance_amount(self):
        try:
            cursor.execute("SELECT ip_amt FROM insurance LIMIT 1")
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return 0  # Default value if no insurance amount is found
        except Exception as e:
            print("Error fetching insurance amount:", e)
            return 0
 
    def show_online_options(self):
        self.payment_menu.config(state=NORMAL)
        options = ["Card", "Netbanking", "UPI"]
        self.payment_options.set(options[0])
        self.payment_menu['menu'].delete(0, 'end')
        for option in options:
            self.payment_menu['menu'].add_command(label=option, command=lambda value=option: self.payment_options.set(value))
 
    def show_offline_options(self):
        self.payment_menu.config(state=NORMAL)
        options = ["Cheque", "Cash"]
        self.payment_options.set(options[0])
        self.payment_menu['menu'].delete(0, 'end')
        for option in options:
            self.payment_menu['menu'].add_command(label=option, command=lambda value=option: self.payment_options.set(value))
 
    def display(self):
        payment_type = "Online" if self.payment_var.get() == 1 else "Offline"
        selected_option = self.payment_options.get()
 
        try:
            print(f"Inserting into 'payment' table with p_id")
            cursor.execute("SELECT p_id from payment LIMIT 1")
            sel = cursor.fetchmany()
            print(sel)
            cursor.execute(f"UPDATE payment SET p_amt = {self.final_amount}")
            conn.commit()
           
            print(f"Inserted into 'payment' table with p_id: {payment_type}")
 
            if payment_type == "Online":
                print(f"Inserting into 'Online' table with p_id: {payment_type}")
                cursor.execute(f"INSERT INTO Online ( on_UPI, on_card, on_netb) VALUES ('UPI_value', 'Card_value', 'Netbanking_value')")
            else:
                cursor.execute(f"INSERT INTO Offline ( of_cheque, of_cash) VALUES ('Cheque_value', 'Cash_value')")
 
            conn.commit()
 
            print("Data Inserted")
            self.Display_Details()
 
        except Exception as e:
            print("Error:", e)
            conn.rollback()
 
    def Display_Details(self):
        self.root.destroy()
        import Display_Details
 
root = Tk()
obj = Payment(root)
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")
root.mainloop()
 