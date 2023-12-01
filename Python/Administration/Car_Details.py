import tkinter as tk
from tkinter import *
import mysql.connector


 
conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
cursor = conn.cursor()
 
class Car:
    def __init__(self,root):
        self.root=root
        self.background_image = PhotoImage(file="D:/College Notes/Car Insurance System/images/blue.png")  # Replace with your background image path
        self.background_label = Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
       
        self.login_frame = Frame(root, bg="#E0F4FF", highlightbackground="#000", bd=5, relief=tk.SOLID)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
       
        self.header_label = Label(self.login_frame, text="Car Details", font=("Times New Roman", 30, "bold", "italic"), bg="#E0F4FF", fg="#000")
        self.header_label.grid(row=0, column=0,columnspan=3, padx=5, pady=5, sticky="n")
       
        self.carno = Label(self.login_frame, text="Car No:", bg="#E0F4FF", font=("Times", 16, "bold"), fg="#000")
        self.carno.grid(row=1, column=0, padx=50, pady=5, sticky="w")
        
        self.en_carno = Entry(self.login_frame, font=("Times", 16, "bold"))
        self.en_carno.grid(row=1, column=2, padx=5, pady=5)
       
        self.car_owner = Label(self.login_frame, text="Car Owner:", bg="#E0F4FF", font=("Times", 16, "bold"), fg="#000")
        self.car_owner.grid(row=2, column=0, padx=50, pady=5, sticky="w")
        self.en_car_owner = Entry(self.login_frame, font=("Times", 16, "bold"))
        self.en_car_owner.grid(row=2, column=2, padx=5, pady=5)
       
        self.car_model = Label(self.login_frame, text="Car Model:", bg="#E0F4FF", font=("Times", 16, "bold"), fg="#000")
        self.car_model.grid(row=3, column=0, padx=50, pady=5, sticky="w")
        self.en_car_model = Entry(self.login_frame, font=("Times", 16, "bold"))
        self.en_car_model.grid(row=3, column=2, padx=5, pady=5)
       
        self.car_type = Label(self.login_frame, text="Car Type:", bg="#E0F4FF", font=("Times", 16, "bold"), fg="#000")
        self.car_type.grid(row=4, column=0, padx=50, pady=5, sticky="w")
        self.en_car_type = Entry(self.login_frame, font=("Times", 16, "bold"))
        self.en_car_type.grid(row=4, column=2, padx=5, pady=5)
       
        self.custid = Label(self.login_frame, text="Customer ID:", bg="#E0F4FF", font=("Times", 16, "bold"), fg="#000")
        self.custid.grid(row=5, column=0, padx=50, pady=5, sticky="w")
        self.en_cust_id = Entry(self.login_frame,  font=("Times", 16, "bold"))
        #self.en_cust_id.insert(0,instance.en_cust_id)
        #self.en_cust_id.config(state = "readonly")
        self.en_cust_id.grid(row=5, column=2, padx=5, pady=5)
       
        self.submit = tk.Button(self.login_frame, text="Submit", command=self.on_submit, font=("Times", 16, "bold"), bg="#525FE1", fg="#FFF6F4")
        self.submit.grid(row=7, columnspan=3, pady=5, padx=50)
 
        self.login_btn = tk.Button(root, text="Login", command=self.login, font=("Times", 16, "bold", "italic"), bg="#525FE1", fg="#FFF6F4")
        self.login_btn.place(relx=0.025, rely=0.025)
       
    def login(self):
        root.destroy()
        import Login
       
    def on_submit(self):
        c_no = self.en_carno.get()
        c_own = self.en_car_owner.get()
        c_model = self.en_car_model.get()
        c_type = self.en_car_type.get()
        cust_id = self.en_cust_id.get()
        
        root.destroy()
        import Inspection_Details
       
       
       
root=Tk()
root.title("Enter Car Details")
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0") # Or ("600x500")
app=Car(root)
root.mainloop()