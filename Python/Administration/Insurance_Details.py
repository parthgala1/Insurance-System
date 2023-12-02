import tkinter as tk
import mysql.connector
from datetime import datetime

# Establish MySQL connection
conn = mysql.connector.connect(user='root', password='%Rachit404%', host='localhost', database='insurance_company')
cursor = conn.cursor()

# Dictionary containing coverage plans, descriptions, amounts, and durations
coverage_info = {
    "Basic Coverage": {"description": "Covers essential liabilities and damages.", "amount": 100000, "duration": "1 year"},
    "Standard Coverage": {"description": "Offers moderate protection for various incidents.", "amount": 150000, "duration": "2 years"},
    "Comprehensive Coverage": {"description": "Covers almost all possible damages to the car.", "amount": 200000, "duration": "3 years"},
    "Collision Coverage": {"description": "Pays for damages caused by collision with another vehicle or object.", "amount": 300000, "duration": "1 year"},
    "Personal Injury Protection": {"description": "Covers medical expenses for injuries sustained in an accident.", "amount": 180000, "duration": "2 years"}
}


class Insurance: 
    def __init__(self, root): 
        self.root = root
        self.selected_coverage = tk.StringVar(value=None)
        
        file_path = "Insurance-System\Python\Administration\custid.txt"
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            self.cus_id = file.read(-1)
        
        self.background_image = tk.PhotoImage(file="Insurance-System/images/blue.png")  # Replace with your background image path

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.95)

        self.f = tk.Frame(root, bg="#E0F4FF", highlightbackground="#000", bd=5, relief=tk.SOLID)
        self.f.place(relx=0.5, rely=0.5, anchor="center")


        self.l1 = tk.Label(self.f, text='Insurance Coverage Plans', fg="#2B2B2B", font=("Times", 30, "bold", "italic"), bg="#E0F4FF")
        self.l1.grid(row=0, column=0, columnspan=3, pady=20)

        self.radio_buttons = []
        self.amount_entries = []
        self.duration_labels = []

        for i, (plan, info) in enumerate(coverage_info.items()):
            rb = tk.Radiobutton(self.f, text=plan, variable=self.selected_coverage, value=plan, bg="#E0F4FF", font=("Times", 14), anchor='w',
                                command=lambda p=plan: self.show_description(p))
            rb.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)
            self.radio_buttons.append(rb)

            amount_var = tk.DoubleVar(value=info['amount'])
            amount_entry = tk.Entry(self.f, textvariable=amount_var, font=("Times", 14), state='readonly')
            amount_entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.amount_entries.append((amount_var, amount_entry))

            duration_label = tk.Label(self.f, text=info['duration'], bg="#E0F4FF", fg="#444444", font=("Times", 14))
            duration_label.grid(row=i+1, column=2, padx=10, pady=5)
            self.duration_labels.append(duration_label)

        self.description_label = tk.Label(self.f, text="", wraplength=400, bg="#E0F4FF", fg="#444444", font=("Times", 16))
        self.description_label.grid(row=len(coverage_info)+1, column=0, columnspan=3, pady=20)

        self.b1 = tk.Button(self.f, text="Submit", command=self.display_and_close, font=("Times", 16, "bold"), bg="#525FE1", fg="#FFF6F4")
        self.b1.grid(row=len(coverage_info)+2, column=0, columnspan=3, pady=30)

        # Adding Back Button
        self.back_button = tk.Button(self.f, text="Back", command=self.check_payment, bg="#87C4FF", fg="#FFF6F4", font=("Times", 14, "bold"))
        self.back_button.grid(row=len(coverage_info)+3, column=0, columnspan=3, pady=10)
        
        

    def show_description(self, plan):
        self.description_label.config(text=coverage_info[plan]['description'])

    def display_and_close(self):
        selected_coverage = self.selected_coverage.get()

        if selected_coverage:
            # Perform database operations here using selected_coverage and its amount from coverage_info
            try:
                current_time = datetime.now().strftime('%H:%M')
                print(type(coverage_info[selected_coverage]['amount']))
                print(type(current_time))
                
                cursor.execute("INSERT INTO insurance (ip_amt,ip_plan,ip_date, cust_id) VALUES (%s, %s, %s, %s)",
                               (coverage_info[selected_coverage]['amount'],selected_coverage, coverage_info[selected_coverage]['duration'], self.cus_id))
                print("Selected Coverage:", selected_coverage)
                cursor.execute("INSERT INTO payment(p_amt, p_time, p_dur, cust_id) values(%s,%s,%s,%s)",
                               (coverage_info[selected_coverage]['amount'], current_time, coverage_info[selected_coverage]['duration'], self.cus_id))
                conn.commit()
                print("Data Inserted")
            except mysql.connector.Error as error:
                conn.rollback()
                print(f"Failed to insert data: {error.msg}")
            else:
                conn.close()
                self.Payment_Details()
        else:
            print("No coverage selected.")
    def check_payment(self):
        self.root.destroy()
        import Inspection_Details
        
    def Payment_Details(self):
        self.root.destroy()
        import Payment_Details
        
        
        
def create_insurance_gui():
    root = tk.Tk() 
    root.title("Insurance Coverage") 
    obj = Insurance(root) 
    
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry(f"{width}x{height}+0+0")  # Set window size
    
    root.mainloop()

# Call the function to create the GUI
create_insurance_gui()
