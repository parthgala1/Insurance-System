import tkinter as tk
import mysql.connector

# Establish MySQL connection
conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
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
        
       

        self.f = tk.Frame(root)
        self.f.pack()

        self.inner_frame = tk.Frame(self.f, bg="#F0F0F0")
        self.inner_frame.pack(padx=50, pady=30)

        self.l1 = tk.Label(self.inner_frame, text='Insurance Coverage Plans', fg="#2B2B2B", font=("Arial", 28, "bold"), bg="#F0F0F0")
        self.l1.grid(row=0, column=0, columnspan=3, pady=20)

        self.radio_buttons = []
        self.amount_entries = []
        self.duration_labels = []

        for i, (plan, info) in enumerate(coverage_info.items()):
            rb = tk.Radiobutton(self.inner_frame, text=plan, variable=self.selected_coverage, value=plan, bg="#F0F0F0", font=("Arial", 14), anchor='w',
                                command=lambda p=plan: self.show_description(p))
            rb.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)
            self.radio_buttons.append(rb)

            amount_var = tk.DoubleVar(value=info['amount'])
            amount_entry = tk.Entry(self.inner_frame, textvariable=amount_var, font=("Arial", 12), state='readonly')
            amount_entry.grid(row=i+1, column=1, padx=10, pady=5)
            self.amount_entries.append((amount_var, amount_entry))

            duration_label = tk.Label(self.inner_frame, text=info['duration'], bg="#F0F0F0", fg="#444444", font=("Arial", 12))
            duration_label.grid(row=i+1, column=2, padx=10, pady=5)
            self.duration_labels.append(duration_label)

        self.description_label = tk.Label(self.inner_frame, text="", wraplength=400, bg="#F0F0F0", fg="#444444", font=("Arial", 12))
        self.description_label.grid(row=len(coverage_info)+1, column=0, columnspan=3, pady=20)

        self.b1 = tk.Button(self.inner_frame, text="Submit", command=self.display_and_close, bg="#4CAF50", fg="#FFFFFF", font=("Arial", 18, "bold"))
        self.b1.grid(row=len(coverage_info)+2, column=0, columnspan=3, pady=30)

        # Adding Back Button
        self.back_button = tk.Button(self.inner_frame, text="Back", command=self.check_payment, bg="#FF5722", fg="#FFFFFF", font=("Arial", 14, "bold"))
        self.back_button.grid(row=len(coverage_info)+3, column=0, columnspan=3, pady=10)

    def show_description(self, plan):
        self.description_label.config(text=coverage_info[plan]['description'])

    def display_and_close(self):
        selected_coverage = self.selected_coverage.get()

        if selected_coverage:
            print("Selected Coverage:", selected_coverage)
            # Perform database operations here using selected_coverage and its amount from coverage_info
            try:
                cursor.execute("INSERT INTO insurance (ip_amt,ip_plan,ip_date) VALUES (%s, %s, %s)",
                               (coverage_info[selected_coverage]['amount'],selected_coverage, coverage_info[selected_coverage]['duration']))
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
    
    root.geometry("700x550")  # Set window size
    
    root.mainloop()

# Call the function to create the GUI
create_insurance_gui()
