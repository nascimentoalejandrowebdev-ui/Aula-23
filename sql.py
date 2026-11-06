import mysql.connector
import pandas as pd
from mysql.connector import Error

try:
    #Estabelece a conexão
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola'
    )

    if conexao.is_connected():
        print("Conectado com sucesso!")

        #Cria um cursor (objeto que permite executar comandos)
        cursor = conexao.cursor()

        #Executa uma consulta
        cursor.execute("SELECT * FROM alunos LIMIT 5")


        #Busca os resultados
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)
            

except Error as e:
    print(f"Erro ao conectar ou executar: {e}")

finally:
    #Fecha a conexão (se foi criada e ainda está conectada
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada")
