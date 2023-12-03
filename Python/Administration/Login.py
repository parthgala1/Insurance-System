import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
cursor = conn.cursor()

class Login: 
    def __init__(self, root): 
        self.root = root

        self.background_image = tk.PhotoImage(file="images/orange.png")  # Replace with your background image path

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.login_frame = tk.Frame(root, bg="#FFF6F4", highlightbackground="#525FE1", bd=3, relief=tk.SOLID)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        self.header_label = tk.Label(root, text="Car Insurance Company", font=("Times", 30, "bold"), bg="#FD6C1D", fg="#FFF6F4")
        self.header_label.place(relx=0.5, rely=0.1, anchor="center")

        self.login_label = tk.Label(self.login_frame, text="Login Deatils", bg="#FFF6F4",fg="#525FE1", font=("Times", 24, "bold", "italic"))
        self.login_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="w")
    
        self.username_label = tk.Label(self.login_frame, text="Username:", bg="#FFF6F4",fg="#525FE1", font=("Times", 14, "bold"))
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.login_frame, font=("Times", 14))
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self.login_frame, text="Password:", bg="#FFF6F4",fg="#525FE1", font=("Times", 14, "bold"))
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.login_frame, show="●", font=("Times", 14))
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.user_type_label = tk.Label(self.login_frame, text="User Type:", bg="#FFF6F4",fg="#525FE1", font=("Times", 14, "bold"))
        self.user_type_label.grid(row=3, column=0, padx=10, pady=10)
        self.user_type_var = tk.StringVar(root)
        self.user_type_var.set("Employee")
        self.user_type_dropdown = tk.OptionMenu(self.login_frame, self.user_type_var, "Employee", "Customer")
        self.user_type_dropdown.config(font=("Times", 14), bg="#FFF6F4")
        self.user_type_dropdown.grid(row=3, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.check_login, font=("Times", 14, "bold"), bg="#FD7926", fg="#FFF6F4")
        self.login_button.grid(row=4, columnspan=2, pady=10, padx=50)

        self.signup_btn = tk.Button(root, text="Sign Up", command=self.Signup, font=("Times", 14, "bold", "italic"), bg="#FFF6F4", fg="#FD7926")
        self.signup_btn.place(relx=0.025, rely=0.025)

    def check_login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.user_type = self.user_type_var.get()
        #cursor.execute(select cust_name from customer)
        #cust_name=cursor.fetchone()
        #cursor.execute(select cust_pass from customer)
        #cust_pass=cursor.fetchone()
        
        cursor.execute(f"SELECT cust_id FROM customer where cust_name like \'{self.username}\' and cust_pass like\'{self.password}\' ;")
        custid = cursor.fetchone()[0]
        
        file_path = "Python/Administration/custid.txt"
        with open(file_path, 'w') as file:
        # Write content to the file
            file.write(custid)
            # The file is automatically closed when the 'with' block is exited

        cursor.execute(f"SELECT cust_name,cust_pass FROM customer where cust_name like \'{self.username}\' and cust_pass like\'{self.password}\' ;")
        user = cursor.fetchone()
        if user:
            conn.close()
            self.Car_Details()
        else:
            messagebox.showerror('Error', 'Incorrect Username or Password')
            
    def Signup(self):
        root.destroy()
        import Signup
        
    def Car_Details(self):
        root.destroy()
        import Car_Details           
        
        
        # Check credentials (replace this with your authentication logic)
        

root = tk.Tk() 
root.title("Welcome To Tkinter GUI Programme") 
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")  
obj = Login(root) 
root.mainloop()

