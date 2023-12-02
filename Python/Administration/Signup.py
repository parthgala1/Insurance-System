import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector
 
conn = mysql.connector.connect(user='root', password='%Rachit404%', host='localhost', database='insurance_company')
cursor = conn.cursor()
 
class Sign:
 
    def __init__(self,root):
        self.root=root
        self.background_image = tk.PhotoImage(file="Insurance-System\images\orange.png")  # Replace with your background image path

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.95)
        
        self.login_frame = Frame(root, bg="#FFF6F4", highlightbackground="#000", bd=3, relief=SOLID )
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
       
        self.header_label = Label(self.login_frame, text="SignUp Details", font=("Times New Roman", 30, "bold", "italic"), bg="#FFF6F4", fg="#000", anchor="center")
        self.header_label.grid(row=0,column=0, padx=5, pady=5)
       
        self.cust_id = Label(self.login_frame, text="Unique ID:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.cust_id.grid(row=1, column=0, padx=5, pady=5)
        self.en_cust_id = Entry(self.login_frame, font=("Times", 14, "bold"))
        self.en_cust_id.grid(row=1, column=1, padx=5, pady=5)
       
        self.cust_name = Label(self.login_frame, text="Name:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.cust_name.grid(row=2, column=0, padx=5, pady=5)
        self.en_cust_name = Entry(self.login_frame, font=("Times", 14, "bold"))
        self.en_cust_name.grid(row=2, column=1, padx=5, pady=5)
       
        self.cust_license = Label(self.login_frame, text="License:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.cust_license.grid(row=3, column=0, padx=5, pady=5)
        self.en_cust_license = Entry(self.login_frame, font=("Times", 14, "bold"))
        self.en_cust_license.grid(row=3, column=1, padx=5, pady=5)
       
        self.cust_mob = Label(self.login_frame, text="Mobile No:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.cust_mob.grid(row=4, column=0, padx=5, pady=5)
        self.en_cust_mob = Entry(self.login_frame, font=("Times", 14, "bold"))
        self.en_cust_mob.grid(row=4, column=1, padx=5, pady=5)
       
        self.cust_pass = Label(self.login_frame, text="Password:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.cust_pass.grid(row=5, column=0, padx=5, pady=5)
        self.en_cust_pass = Entry(self.login_frame, font=("Times", 14, "bold"), show = '●')
        self.en_cust_pass.grid(row=5, column=1, padx=5, pady=5)
       
        self.recust_pass = Label(self.login_frame, text="Retype Password:", bg="#FFF6F4", font=("Times", 14, "bold"), fg="#000")
        self.recust_pass.grid(row=6, column=0, padx=5, pady=5)
        self.en_recust_pass = Entry(self.login_frame, font=("Times", 14, "bold"), show = '●')
        self.en_recust_pass.grid(row=6, column=1, padx=5, pady=5)
       
        self.submit = tk.Button(self.login_frame, text="Sign Up", command=self.check_submit, font=("Times", 14, "bold"), bg="#FD7926", fg="#FFFFFF")
        self.submit.grid(row=7, columnspan=2, pady=5, padx=50)
 
        self.login_btn = tk.Button(root, text="Login", command=self.login, font=("Times", 14, "bold", "italic"), bg="#FFF6F4", fg="#FD7926")
        self.login_btn.place(relx=0.025, rely=0.025)
        
        file_path = "Insurance-System\Python\Administration\custid.txt"
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            cus_id = file.read(-1)
       
    def check_submit(self):
        passw = self.en_cust_pass.get()
        repass = self.en_recust_pass.get()
       
        if(passw == repass):
            self.on_submit()
        else:
            messagebox.showerror('Error', 'Passwords do not match!')
           
    def on_submit(self):
        uid = self.en_cust_id.get()
        name = self.en_cust_name.get()
        license1 = self.en_cust_license.get()
        mob = self.en_cust_mob.get()
        passw = self.en_cust_pass.get()  
        cid = 1  
        sql="Insert into customer(cust_id, cust_name, cust_license, cust_pass, c_id) values('%s','%s','%s','%s', %s)"%(uid,name,license1,passw,cid)
        sql2="Insert into custmob(cust_id, cust_mob) values('%s','%s')"%(uid,mob)
 
        try:
            cursor.execute(sql)
            cursor.execute(sql2)
            conn.commit()
            print("Data Inserted")
        except Exception as e:
            conn.rollback()
            print("Error", e)
        self.login()
           
    def login(self):
        root.destroy()
        import Login
       
       
root=Tk()
root.title("Signup Page")
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")
obj=Sign(root)
root.mainloop()