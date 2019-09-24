from tabulate import tabulate
import pymysql

db_connection = pymysql.connect("localhost","root", "Sai@123","LibraryManagement")
cursor = db_connection.cursor()
sql_query = "select *from book;"
cursor.execute(sql_query)
data = cursor.fetchall()
db_connection.commit()
try:
    if data is not None:
        names = [row[0] for row in cursor.description]
        print (tabulate(data, headers=names))
except Exception as e:
    raise e
db_connection.close()