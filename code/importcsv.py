import csv
import mysql.connector

# MySQL connection parameters
cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='zomoto')
cursor = cnx.cursor()

# CSV file path
csv_file_path = 'C:\Users\kj\.vscode\customers.csv'

with open(csv_file_path, mode='r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO customers (column1, column2) VALUES (%s, %s)", row)

cnx.commit()
cursor.close()
cnx.close()