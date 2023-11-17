from tkinter import *
import mysql.connector

conn = mysql.connector.connect(user='root', password='pass@123', host='localhost', database='')
cursor = conn.cursor()

class Car: 
 
    def __init__(self,root): 
       self.f=Frame(root,height=500,width=500) 
       self.f.pack()
       self.l1=Label(text='Car Details')
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
        self.Inspection_Details() 
 
    def Inspection_Details(self): 
       root.destroy() 
       import Inspection_Details 
 
 
root=Tk() 
root.title("Welcome To Tkinter GUI Programme") 
obj=Car(root) 
root.mainloop()