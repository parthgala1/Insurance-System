from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='')
cursor = conn.cursor()

class Insurance: 
 
    def __init__(self,root): 
       self.f=Frame(root,height=500,width=500) 
       self.f.pack()
       self.l1=Label(text='Insurance Details')
       self.b1=Button(self.f,text="Submit",command=self.display)
       self.l1.place(x=50,y=30)
       self.b1.place(x=200,y=150)
       
    def display(self):
        try: 
            cursor.execute() 
            conn.commit() 
        except: 
            conn.rollback() 
        print("Data Inserted") 
        conn.close()  
        self.Payment_Details() 
 
    def Payment_Details(self): 
       root.destroy() 
       from Administration import Payment_Details 
 
 
root=Tk() 
root.title("Step 3: Insurance Selection") 
obj=Insurance(root) 
root.mainloop()