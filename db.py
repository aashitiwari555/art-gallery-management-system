import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',         
        password='password',         
        database='art_gallery_db'
    )
    return connection
