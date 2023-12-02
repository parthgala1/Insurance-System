import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(user='root', password='%Rachit404%', host='localhost', database='insurance_company')
cursor = conn.cursor()
class Inspection: 
    def __init__(self, root):
        self.root = root
        self.root.title("Insurance Company - Inspection and Accident")
        
        file_path = "Insurance-System\Python\Administration\custid.txt"
        # Open the file in read mode ('r')
        with open(file_path, 'r') as file:
            self.cus_id = file.read(-1)
        
        self.background_image = tk.PhotoImage(file="Insurance-System/images/blue.png")  # Replace with your background image path

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=0.95)

        self.acc_frame = tk.Frame(root, bg="#E0F4FF", highlightbackground="#F86F03", bd=5, relief=tk.SOLID)
        self.acc_frame.place(relx=0.5, rely=0.5, anchor="center")

        font_times_new_roman = ('Times New Roman', 14)

        self.l_accident = tk.Label(self.acc_frame, text='Accident Details', font=('Times New Roman', 30, 'bold', 'italic'),
                                bg='#E0F4FF', fg='#000')
        self.l_date = tk.Label(self.acc_frame, text='Date:', font=font_times_new_roman, bg='#E0F4FF', fg='#000')
        self.e_date = tk.Entry(self.acc_frame, font=font_times_new_roman, bg='#B0C4DE', fg='#000')
        self.l_time = tk.Label(self.acc_frame, text='Time:', font=font_times_new_roman, bg='#E0F4FF', fg='#000')
        self.e_time = tk.Entry(self.acc_frame, font=font_times_new_roman, bg='#B0C4DE', fg='#000')
        self.l_place = tk.Label(self.acc_frame, text='Place:', font=font_times_new_roman, bg='#E0F4FF', fg='#000')
        self.e_place = tk.Entry(self.acc_frame, font=font_times_new_roman, bg='#B0C4DE', fg='#000')

        self.l_services = tk.Label(self.acc_frame, text='Services:', font=('Times New Roman', 14, 'underline'),
                                bg='#E0F4FF', fg='#000')
        self.l_addon = tk.Label(self.acc_frame, text='AddOns', font=font_times_new_roman, bg='#E0F4FF', fg='#000')
        self.addon_options = ['Car Wash', 'Polishing', 'Alignment']
        self.addon_var = tk.StringVar(root)
        self.addon_menu = tk.OptionMenu(self.acc_frame, self.addon_var, *self.addon_options)
        self.l_customer_services = tk.Label(self.acc_frame, text='Customer Services:', font=font_times_new_roman,
                                         bg='#E0F4FF', fg='#000')
        self.addon_var.trace("w", self.on_dropdown_change)
        self.customer_services_var = tk.BooleanVar()
        self.cb_customer_services = tk.Checkbutton(self.acc_frame, text=' ', variable=self.customer_services_var,
                                                 font=font_times_new_roman, bg='#E0F4FF', fg='#000')

        self.b_create = tk.Button(self.acc_frame, text="Create Report", command=self.inspection_report(), font=font_times_new_roman,
                                bg='#4682B4', fg='white')
        
        self.l_inspection_report = tk.Label(self.acc_frame, text='Accident Report', font=('Times New Roman', 16, 'bold'),
                                         bg='#E0F4FF', fg='#000')
        self.accident_report_text = tk.StringVar()
        self.l_accident_report_text = tk.Label(self.acc_frame, textvariable=self.accident_report_text, font=('Times New Roman', 14),
                                          bg='#E0F4FF', fg='#000')
        self.l_accident_report_text.grid(row=11, column=0, columnspan=2, padx=10)

        self.b_submit = tk.Button(self.acc_frame, text="Submit", command=self.display, font=font_times_new_roman,
                                bg='#4682B4', fg='white')

        self.grid_widgets()
        
    def on_dropdown_change(self, *args):
        selected_value = self.addon_var.get()
        print("Selected value:", selected_value)

    def grid_widgets(self):
        self.l_accident.grid(row=0, column=0, columnspan=2)
        self.l_date.grid(row=2, column=0, sticky='e')
        self.e_date.grid(row=2, column=1, padx=10)
        self.l_time.grid(row=3, column=0, sticky='e')
        self.e_time.grid(row=3, column=1, padx=10)
        self.l_place.grid(row=4, column=0, sticky='e')
        self.e_place.grid(row=4, column=1, padx=10)

        self.l_services.grid(row=5, column=0, columnspan=2, pady=10)
        self.l_addon.grid(row=6, column=0, sticky='e')
        self.addon_menu.grid(row=6, column=1, padx=10)
        self.l_customer_services.grid(row=7, column=0, columnspan=2, pady=10, sticky="w", padx=10)
        self.cb_customer_services.grid(row=7, column=1, padx=10, sticky="s")

        self.b_create.grid(row=9, column=0, columnspan=2, pady=10)
        self.l_inspection_report.grid(row=10, column=0, columnspan=2, pady=10)
        self.l_accident_report_text.grid(row=11, column=0, columnspan=2, padx=10)
        self.b_submit.grid(row=12, column=0, columnspan=2, pady=10)
        
        
               
    def display(self):
        accident_date = self.e_date.get()
        accident_time = self.e_time.get()
        accident_place = self.e_place.get()
        
        addon_services = self.addon_var.get()
        customer_services = self.customer_services_var.get()
        company_id = 1
        
        print(self.addon_var)

        
        try: 
            # Assuming you have a table named 'inspection_report'
            car_no = cursor.execute("SELECT car_no FROM car where cust_id = 101")
            cursor.execute("INSERT INTO accident(a_place, a_time, a_date, car_no) VALUES (%s, %s, %s, %s)", (accident_place, accident_time, accident_date, car_no))
            cursor.execute("INSERT INTO services(s_addOn, s_cust, c_id) VALUES (%s, %s, %d)",(addon_services, customer_services, company_id))
            conn.commit() 
            print("Data Inserted") 
        except Exception as e: 
            print(f"Error: {e}")
            conn.rollback() 
        
        conn.close() 
        root.destroy()
        import Insurance_Details
 
    def inspection_report(self): 
        try:
            cursor.execute(f"SELECT * FROM accident a, car c where c.car_no = a.car_no and c.car_no =(SELECT car_no FROM car where cust_id={self.cus_id})")
            result = cursor.fetchone()
            if result:
                report_text = f"Accident Date: {result[1]}\nAccident Time: {result[2]}\nAccident Place: {result[3]}\nAddOn Services: {result[4]}\nCustomer Services: {result[5]}"
                self.accident_report_text.set(report_text)
        except Exception as e:
            print(f"Error fetching inspection report: {e}")

root = tk.Tk() 
root.title("Step 2: Inspection and Accident") 
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry(f"{width}x{height}+0+0")
obj = Inspection(root) 
root.mainloop()
