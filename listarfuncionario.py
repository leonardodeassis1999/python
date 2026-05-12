import mysql.connector
from conexao import criar_conexao





def listar_funcionarios():
    conn = criar_conexao()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM funcionario")
    resultados = cursor.fetchall()
    
    for linha in resultados:
        print(linha)
        
    cursor.close()
    conn.close()
