import mysql.connector
from mysql.connector import Error
class DbHelper:
                
    def get_maximum_salary(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="5817@papanishU",port=3306, database='datagokr')
            if conn.is_connected():
                print('Connected to MySQL database')
                cursor = conn.cursor()
                cursor.execute("Select MAX(Salary) as maxsalary from pythondb")
                rows = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            if conn is not None and conn.is_connected():
                 conn.close
        
    def get_minimum_salary(self):
        conn = None
        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="5817@papanishU",port=3306, database='datagokr')
            if conn.is_connected():
                print('Connected to MySQL database')
                cursor = conn.cursor()
                cursor.execute("Select MIN(Salary) as minsalary from pythondb")
                rows = cursor.fetchall()
        except Error as e:
            print(e)
        finally:
            if conn is not None and conn.is_connected():
                conn.close

if __name__ == "__main__":
    db_helper = DbHelper()
    db_helper.get_minimum_salary()
    db_helper.get_maximum_salary()
