import mysql.connector
from conexao import criar_conexao


def inserir_funcionario():
    # Coleta os dados do usuário aqui
    matricula = int(input("Qual é sua matricula? "))
    nome = input("Qual é o seu nome? ")
    data_nascimento = input("Qual é a sua data de nascimento (AAAA-MM-DD)? ")
    cargo = input("Qual é o seu cargo? ")

    conn = criar_conexao()
    cursor = conn.cursor()

    sql = "INSERT INTO funcionario (matricula, nome, data_nascimento, cargo) VALUES (%s, %s, %s, %s)"
    valores = (matricula, nome, data_nascimento, cargo)
    
    cursor.execute(sql, valores)
    conn.commit()
    
    print("Funcionário inserido com sucesso!")
    cursor.close()
    conn.close()
