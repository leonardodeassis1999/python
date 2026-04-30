# Importa a biblioteca
# Serve para conectar o banco de dados ao python
import mysql.connector 

# Executa uma funcao na lib que realiza a conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pessoas"
)

print("conectado")

# Funcao cursor() da lib
# Serve para manipular os dados
cursor = conexao.cursor()

# Comandos e valores para envio de dados em SQL
sql = "INSERT INTO funcionario(nome, data_nascimento, cargo) VALUES (%s, %s, %s)"
values = ("Ana Silva", '1990-05-15', "Analista de Sistemas")

cursor.execute(sql, values)
conexao.commit()

cursor.execute("SELECT * FROM funcionario")
resultados = cursor.fetchall()

for i in resultados:
    print(i)