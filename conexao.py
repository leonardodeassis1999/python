import mysql.connector 

def criar_conexao():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='csv_db 9'
    )