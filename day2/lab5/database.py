import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joseph9",
    database="company_db"
)

cursor = connection.cursor()