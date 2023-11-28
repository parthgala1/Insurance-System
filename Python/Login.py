import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(user='root', password='#Swayam0920', host='localhost', database='insurance_company')
cursor = conn.cursor()

class Login: 
    def __init__(self, root): 
        self.root = root

        self.background_image = tk.PhotoImage(file="C:/Users/swayam shah/OneDrive/Pictures/Screenshot 2023-11-26 174603.png")  # Replace with your background image path

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.header_label = tk.Label(root, text="Company Login Page", font=("Arial", 30, "bold"), bg="#333333", fg="#FFFFFF")
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")

        self.login_frame = tk.Frame(root, bg="#FFFFFF", bd=5, relief=tk.GROOVE)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.username_label = tk.Label(self.login_frame, text="Username:", bg="#FFFFFF", font=("Arial", 12))
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self.login_frame, text="Password:", bg="#FFFFFF", font=("Arial", 12))
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.user_type_label = tk.Label(self.login_frame, text="User Type:", bg="#FFFFFF", font=("Arial", 12))
        self.user_type_label.grid(row=2, column=0, padx=10, pady=10)
        self.user_type_var = tk.StringVar(root)
        self.user_type_var.set("Employee")
        self.user_type_dropdown = tk.OptionMenu(self.login_frame, self.user_type_var, "Employee", "Customer")
        self.user_type_dropdown.config(font=("Arial", 12), bg="#FFFFFF")
        self.user_type_dropdown.grid(row=2, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.check_login, font=("Arial", 14, "bold"), bg="#4CAF50", fg="#FFFFFF")
        self.login_button.grid(row=3, columnspan=2, pady=10, padx=50)

        self.back_button = tk.Button(root, text="Back", command=self.Signup, font=("Arial", 12), bg="#FF5722", fg="#FFFFFF")
        self.back_button.place(relx=0.05, rely=0.05)

    def check_login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.user_type = self.user_type_var.get()
        #cursor.execute(select cust_name from customer)
        #cust_name=cursor.fetchone()
        #cursor.execute(select cust_pass from customer)
        #cust_pass=cursor.fetchone()
        
        cursor.execute(f"SELECT cust_name,cust_pass FROM customer where cust_name like \'{self.username}\' and cust_pass like\'{self.password}\' ;")
        user = cursor.fetchone()
        if user:
            conn.close()
            self.Car_Details()
        else:
            conn.close()
            
    def Signup(self):
        root.destroy()
        import Signup
        
    def Car_Details(self):
        root.destroy()
        from Administration import Car_Details           
        
        
        # Check credentials (replace this with your authentication logic)
        

root = tk.Tk() 
root.title("Welcome To Tkinter GUI Programme") 
root.geometry("800x600")  # Set window size

obj = Login(root) 
root.mainloop()

