from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='insurance_company')
cursor = conn.cursor()
class Inspection: 
    def __init__(self, root): 
        self.f = Frame(root, height=500, width=500, bg='#87CEEB')  # Sky Blue background
        self.f.pack()
        
        # Set Times New Roman font
        font_times_new_roman = ('Times New Roman', 12)
        
        # Accident Details
        self.l_accident = Label(self.f, text='Accident Details', font=('Times New Roman', 16, 'bold'), bg='#87CEEB', fg='black')  # Bold and black text
        self.l_date = Label(self.f, text='Date:', font=font_times_new_roman, bg='#87CEEB', fg='black')
        self.e_date = Entry(self.f, font=font_times_new_roman, bg='#B0C4DE', fg='black')  # Light Steel Blue entry background
        self.l_time = Label(self.f, text='Time:', font=font_times_new_roman, bg='#87CEEB', fg='black')
        self.e_time = Entry(self.f, font=font_times_new_roman, bg='#B0C4DE', fg='black')
        self.l_place = Label(self.f, text='Place:', font=font_times_new_roman, bg='#87CEEB', fg='black')
        self.e_place = Entry(self.f, font=font_times_new_roman, bg='#B0C4DE', fg='black')
        
        # Services
        self.l_services = Label(self.f, text='Services:', font=('Times New Roman', 14, 'underline'), bg='#87CEEB', fg='black')
        self.l_addon = Label(self.f, text='AddOns', font=font_times_new_roman, bg='#87CEEB', fg='black')
        self.addon_options = ['Car Wash', 'Polishing', 'Alignment']
        self.addon_var = StringVar()
        self.addon_menu = OptionMenu(self.f, self.addon_var, *self.addon_options)
        self.l_customer_services = Label(self.f, text='Customer Services:', font=font_times_new_roman, bg='#87CEEB', fg='black')
        self.customer_services_var = BooleanVar()
        self.cb_customer_services = Checkbutton(self.f, text=' ', variable=self.customer_services_var, font=font_times_new_roman, bg='#87CEEB', fg='black')
        
        # Inspection Report
        self.l_inspection_report = Label(self.f, text='Accident Report', font=('Times New Roman', 16, 'bold'), bg='#87CEEB', fg='black')
        self.t_inspection_report = Text(self.f, height=5, width=30, font=font_times_new_roman, bg='#B0C4DE', fg='black')  # Light Steel Blue text area background
        
        # Submit Button
        self.b_submit = Button(self.f, text="Submit", command=self.display, font=font_times_new_roman, bg='#4682B4', fg='white')  # Steel Blue button
        
        # Placing widgets on the frame
        self.l_accident.place(x=50, y=30)
        self.l_date.place(x=50, y=60)
        self.e_date.place(x=150, y=60)
        self.l_time.place(x=50, y=90)
        self.e_time.place(x=150, y=90)
        self.l_place.place(x=50, y=120)
        self.e_place.place(x=150, y=120)
        
        self.l_services.place(x=50, y=160)
        self.l_addon.place(x=50, y=190)
        self.addon_menu.place(x=100, y=185)
        self.l_customer_services.place(x=50, y=220)
        self.cb_customer_services.place(x=160, y=220)
        
        self.l_inspection_report.place(x=50, y=300)
        self.t_inspection_report.place(x=50, y=330)
        
        self.b_submit.place(x=50, y=260)
       
    def display(self):
        accident_date = self.e_date.get()
        accident_time = self.e_time.get()
        accident_place = self.e_place.get()
        
        addon_services = self.addon_var.get()
        customer_services = self.customer_services_var.get()
        
        try: 
            # Assuming you have a table named 'inspection_report'
            cursor.execute("INSERT INTO inspection_report (accident_date, accident_time, accident_place, addon_services, customer_services) VALUES (%s, %s, %s, %s, %s)", (accident_date, accident_time, accident_place, addon_services, customer_services))
            conn.commit() 
            print("Data Inserted") 
        except Exception as e: 
            print(f"Error: {e}")
            conn.rollback() 
        
        conn.close() 
        self.inspection_report()
 
    def inspection_report(self): 
        try:
            cursor.execute("SELECT * FROM inspection_report ORDER BY id DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                report_text = f"Accident Date: {result[1]}\nAccident Time: {result[2]}\nAccident Place: {result[3]}\nAddOn Services: {result[4]}\nCustomer Services: {result[5]}"
                self.t_inspection_report.delete(1.0, END)
                self.t_inspection_report.insert(INSERT, report_text)
        except Exception as e:
            print(f"Error fetching inspection report: {e}")

root = Tk() 
root.title("Step 2: Inspection and Accident") 
obj = Inspection(root) 
root.mainloop()
