from tkinter import *
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(user='root', password='%Rachit404%', host='localhost', database='insurance_company')
cursor = conn.cursor()

class Display: 
    def __init__(self, root, canvas): 
        self.canvas = canvas        
        self.background_image = PhotoImage(file="Insurance-System/images/blue.png")  # Replace with your background image path
        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.95)
        
        file_path = "Insurance-System\Python\Administration\custid.txt"
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            self.cus_id = file.read(-1)
        
        self.f = Frame(root, bg="#E0F4FF", highlightbackground="#000", bd=5, relief=SOLID)
        self.f.place(relx=0.5, rely=0.45, anchor= "center")
        
        self.company = Label(self.f, text="Car Insurance Company", font=('Times', 32, "bold", "italic"), bg="#E0F4FF")
        self.company.grid(row=0, column=2, columnspan=5, pady=10)
        
        # Client Information - Label
        self.client = Label(self.f, text="Client Information", font=('Times', 24, "bold"), bg="#E0F4FF")
        self.client.grid(row=1, column=2, columnspan=4)
        
        self.code = Label(self.f, text="Code", font=('Times'), bg="#E0F4FF")
        self.code.grid(row=3, column=0, sticky="W") 
        self.e1 = Entry(self.f, width=28)
        self.e1.grid(row=3, column=1, columnspan=3)
        
        self.name = Label(self.f, text="Name", font=('Times'), bg="#E0F4FF")
        self.name.grid(row=4, column=0, sticky="W") 
        self.e2 = Entry(self.f, width=28)
        self.e2.grid(row=4, column=1, columnspan=3)
        
        self.licnum = Label(self.f, text="License Number", font=('Times'), bg="#E0F4FF")
        self.licnum.grid(row=3, column=4, sticky="W")
        self.e3 = Entry(self.f, width=28)
        self.e3.grid(row=3, column=5, columnspan=3)
        
        self.mob = Label(self.f, text="Contact", font=('Times'), bg="#E0F4FF")
        self.mob.grid(row=4, column=4, sticky="W") 
        self.e4 = Entry(self.f, width=28)
        self.e4.grid(row=4, column=5, columnspan=3)
        
        # Car Information Details
        self.car = Label(self.f, text="Car Information", font=('Times', 24, "bold"), bg="#E0F4FF")
        self.car.grid(row=6, column=2, columnspan=4)
        # self.canvas.create_line(0, 237, 9000, 237, width=1)
        
        self.c_no = Label(self.f, text="Car Number", font=('Times'), bg="#E0F4FF")
        self.c_no.grid(row=7, column=0, sticky="W") 
        self.c1 = Entry(self.f, width=28)
        self.c1.grid(row=7, column=1, columnspan=3)
        
        self.c_model = Label(self.f, text="Car Model", font=('Times'), bg="#E0F4FF")
        self.c_model.grid(row=8, column=0, sticky="W") 
        self.c2 = Entry(self.f, width=28)
        self.c2.grid(row=8, column=1, columnspan=3)
        
        self.c_type = Label(self.f, text="Car Type", font=('Times'), bg="#E0F4FF")
        self.c_type.grid(row=7, column=4, sticky="W")
        self.c3 = Entry(self.f, width=28)
        self.c3.grid(row=7, column=5, columnspan=3)
        
        self.c_owner = Label(self.f, text="Car Owner", font=('Times'), bg="#E0F4FF")
        self.c_owner.grid(row=8, column=4, sticky="W") 
        self.c4 = Entry(self.f, width=28)
        self.c4.grid(row=8, column=5, columnspan=3)

        # Inspection Information Details
        self.ip = Label(self.f, text="Insurance Report", font=('Times', 24, "bold"), bg="#E0F4FF")
        self.ip.grid(row=11, column=0, columnspan=4)
        # self.canvas.create_line(0, 361, 9000, 361, width=1)
        
        self.ip1 = Text(self.f, height=7, width=50)
        self.ip1.grid(row=12, column=0, columnspan=4)
        
        # Accident Information Details
        self.ac = Label(self.f, text="Accident Report", font=('Times', 24, "bold"), bg="#E0F4FF")
        self.ac.grid(row=11, column=5, columnspan=4)
        # self.canvas.create_line(0, 501, 9000, 501, width=1)
        
        self.ac1 = Text(self.f, height=7, width=50)
        self.ac1.grid(row=12, column=5, columnspan=4)
        
        
        # Bill Information
        self.bill = Label(self.f, text="Payment Information", font=('Times', 24, "bold"), bg="#E0F4FF")
        self.bill.grid(row=13, column=2, columnspan=4)    
        
        self.bill_amount = self.get_insurance_amount()
        self.gst_percentage = 18  # Replace with your actual GST percentage
 
        # Calculating GST and Final Amount
        gst_amount = (self.bill_amount * self.gst_percentage) / 100
        final_amount = self.bill_amount + gst_amount
        
        #Bill Details Frame
        self.bill_frame = Frame(self.f, bd=1, bg="#E0F4FF", relief=SOLID)
        self.bill_frame.grid(row=14, column=2, columnspan=4, pady=20, padx=50)
 
        
        self.bill_label = Label(self.bill_frame, text='Bill Details', font=("Times New Roman", 18, "bold"), bg="#E0F4FF", fg="black")
        self.bill_label.grid(row=0, column=0, columnspan=2, pady=10)
 
        self.bill_amount_label = Label(self.bill_frame, text=f'Amount: ', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")
        self.bill_amount_label.grid(row=1, column=0, sticky="e", pady=5)
 
        self.bill_amount_value_label = Label(self.bill_frame, text=f'₹ {self.bill_amount:.2f}', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")
        self.bill_amount_value_label.grid(row=1, column=1, sticky="w", pady=5, padx=20)
 
        self.gst_label = Label(self.bill_frame, text=f'GST ({self.gst_percentage}%): ', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")
        self.gst_label.grid(row=2, column=0, sticky="e", pady=5)
 
        self.gst_value_label = Label(self.bill_frame, text=f'₹ {gst_amount:.2f}', font=("Times New Roman", 14), bg="#E0F4FF", fg="black")
        self.gst_value_label.grid(row=2, column=1, sticky="w", pady=5, padx=20)
 
        self.final_amount_label = Label(self.bill_frame, text=f'Final Amount: ', font=("Times New Roman", 14, "bold"), bg="#E0F4FF", fg="black")
        self.final_amount_label.grid(row=3, column=0, sticky="e", pady=5)
 
        self.final_amount_value_label = Label(self.bill_frame, text=f'₹ {final_amount:.2f}', font=("Times New Roman", 14, "bold"), bg="#E0F4FF", fg="black")
        self.final_amount_value_label.grid(row=3, column=1, sticky="w", pady=5, padx=20)
        
        
        self.display()
        self.close_connection()
        
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
    
    # def get_insurance_report(self):
    #     try: 
    #         cursor.execute("SELECT ip_plan FROM insurance where cust_id = 123 LIMIT 1")
    #         plan = cursor.fetchone()
    #         cursor.execute("SELECT ip_date FROM insurance where cust_id = 123 LIMIT 1")
    #         date = cursor.fetchone()
    #         if date and plan:
    #             str = 
    #             return 
    #     except:
    #         print("Error")
    #         cursor.close()
        
    def display(self): 
        print("----------View records-----------")
        uid = 123
        cursor.execute(f"SELECT * FROM customer where cust_id = {self.cus_id}")
        rows = cursor.fetchall() 
        
        cursor.execute(f"SELECT * FROM car where cust_id = {self.cus_id}")
        car_row = cursor.fetchall() 
        
        try:
            cursor.execute(f"SELECT * FROM accident a, car c where c.car_no = a.car_no and c.car_no =(SELECT car_no FROM car where cust_id={self.cus_id})")
            result = cursor.fetchone()
            if result:
                report_text = f"Accident Date: {result[1]}\nAccident Time: {result[2]}\nAccident Place: {result[3]}\nAddOn Services: {result[4]}\nCustomer Services: {result[5]}"
                self.ip1.insert(END, report_text)
        except Exception as e:
            print(f"Error fetching inspection report: {e}")
        
        try: 
            if len(rows) != 0:
                # User Contact Info
                for row in rows:
                    self.e1.insert(END, f"{row[0]}\n")
                    self.e2.insert(END, f"{row[1]}\n")
                    self.e3.insert(END, f"{row[2]}\n")
                    
                    cursor.execute(f"SELECT * FROM custmob where cust_id={row[0]}")
                    row_mob = cursor.fetchall()
                    for row in row_mob:
                        self.e4.insert(END, f"{row[1]}\n")
                        
                self.e1.config(state="readonly")
                self.e2.config(state="readonly")
                self.e3.config(state="readonly")
                self.e4.config(state="readonly")
                
                # Car Info:
                for row in car_row:
                    self.c1.insert(END, f"{row[0]}\n")
                    self.c2.insert(END, f"{row[2]}\n")
                    self.c3.insert(END, f"{row[3]}\n")
                    self.c4.insert(END, f"{row[1]}\n")
                    print(row)
                        
                self.c1.config(state="readonly")
                self.c2.config(state="readonly")
                self.c3.config(state="readonly")
                self.c4.config(state="readonly")
                
        except Exception as e: 
            print(f"Error: {e}") 

    def close_connection(self):
        try:
            cursor.close()
            conn.close()
            print("Connection closed")
        except Exception as e:
            print(f"Error closing connection: {e}")

root = Tk()

canvas = Canvas(root)
canvas.grid(row=0, column=0) 
root.title("Your Details") 
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")
obj = Display(root, canvas) 
root.mainloop() 
