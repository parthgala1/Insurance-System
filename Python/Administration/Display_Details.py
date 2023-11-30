from tkinter import *
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
cursor = conn.cursor()

class Display: 
    def __init__(self, root, canvas): 
        self.canvas = canvas
        self.f = Frame(root)
        self.f.place(relx=0.5, rely=0.5, anchor= "center")
        
        self.company = Label(self.f, text="Car Insurance Company", font=('Times', 32))
        self.company.grid(row=0, column=2, columnspan=5, pady=10)
        
        # Client Information - Label
        self.client = Label(self.f, text="Client Information", font=('Times', 24))
        self.client.grid(row=1, column=2, columnspan=4)
        
        self.code = Label(self.f, text="Code", font=('Times'))
        self.code.grid(row=3, column=0, sticky="W") 
        self.e1 = Entry(self.f, width=28)
        self.e1.grid(row=3, column=1, columnspan=3)
        
        self.name = Label(self.f, text="Name", font=('Times'))
        self.name.grid(row=4, column=0, sticky="W") 
        self.e2 = Entry(self.f, width=28)
        self.e2.grid(row=4, column=1, columnspan=3)
        
        self.licnum = Label(self.f, text="License Number", font=('Times'))
        self.licnum.grid(row=3, column=4, sticky="W")
        self.e3 = Entry(self.f, width=28)
        self.e3.grid(row=3, column=5, columnspan=3)
        
        self.mob = Label(self.f, text="Contact", font=('Times'))
        self.mob.grid(row=4, column=4, sticky="W") 
        self.e4 = Entry(self.f, width=28)
        self.e4.grid(row=4, column=5, columnspan=3)
        
        # Car Information Details
        self.car = Label(self.f, text="Car Information", font=('Times', 24))
        self.car.grid(row=6, column=2, columnspan=4)
        # self.canvas.create_line(0, 237, 9000, 237, width=1)
        
        self.c_no = Label(self.f, text="Car Number", font=('Times'))
        self.c_no.grid(row=7, column=0, sticky="W") 
        self.c1 = Entry(self.f, width=28)
        self.c1.grid(row=7, column=1, columnspan=3)
        
        self.c_model = Label(self.f, text="Car Model", font=('Times'))
        self.c_model.grid(row=8, column=0, sticky="W") 
        self.c2 = Entry(self.f, width=28)
        self.c2.grid(row=8, column=1, columnspan=3)
        
        self.c_type = Label(self.f, text="Car Type", font=('Times'))
        self.c_type.grid(row=7, column=4, sticky="W")
        self.c3 = Entry(self.f, width=28)
        self.c3.grid(row=7, column=5, columnspan=3)
        
        self.c_owner = Label(self.f, text="Car Owner", font=('Times'))
        self.c_owner.grid(row=8, column=4, sticky="W") 
        self.c4 = Entry(self.f, width=28)
        self.c4.grid(row=8, column=5, columnspan=3)

        # Inspection Information Details
        self.ip = Label(self.f, text="Insurance Report", font=('Times', 24))
        self.ip.grid(row=11, column=0, columnspan=4)
        # self.canvas.create_line(0, 361, 9000, 361, width=1)
        
        self.ip1 = Text(self.f, height=7, width=50)
        self.ip1.grid(row=12, column=0, columnspan=4)
        
        # Accident Information Details
        self.ac = Label(self.f, text="Accident Report", font=('Times', 24))
        self.ac.grid(row=11, column=5, columnspan=4)
        # self.canvas.create_line(0, 501, 9000, 501, width=1)
        
        self.ac1 = Text(self.f, height=7, width=50)
        self.ac1.grid(row=12, column=5, columnspan=4)
        
        
        # Bill Information
        
        

        self.display()
        self.close_connection()
        
    def display(self): 
        print("----------View records-----------")
        cursor.execute("SELECT * FROM customer")
        rows = cursor.fetchall() 
        
        cursor.execute("SELECT * FROM car")
        car_row = cursor.fetchall() 
        
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
                    self.c2.insert(END, f"{row[1]}\n")
                    self.c3.insert(END, f"{row[2]}\n")
                    self.e4.insert(END, f"{row[1]}\n")
                        
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
