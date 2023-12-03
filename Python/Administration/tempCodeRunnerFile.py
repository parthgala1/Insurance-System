ecute(f"SELECT * FROM accident a, car c where c.car_no = a.car_no and c.car_no =(SELECT car_no FROM car where cust_id={self.cus_id})")
            result = cursor.fetchone()
            
            if result:
                cursor.execute(f"SELECT * FROM accident a, car c where c.car_no = a.car_no and c.car_no =(SELECT car_no FROM car where cust_id={self.cus_id})")
                result = cursor.fetchone()
                report_text = f"Accident Date: {result[1]}\nAccident Time: {result[2]}\nAccident Place: {result[3]}\n"
                self.ac1.insert(END, report_text)