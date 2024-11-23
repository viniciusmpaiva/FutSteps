from Modules.Connection import Connection

def select_athlete(cpf):
    """
    Busca informações de um atleta pelo CPF.
    """
    try:
        # Conecta ao banco de dados
        connection = Connection.connectToDB()
        if not connection:
            return []

        # Cria o cursor
        cursor = connection.cursor()

        # Executa a consulta
        query = 'SELECT * FROM ATLETA WHERE CPF = %s'
        cursor.execute(query, (cpf,))

        # Obtém os resultados
        output = cursor.fetchall()

        # Retorna os resultados
        return output
    except Exception as e:
        print(f"Erro ao buscar atleta: {e}")
        return []
    finally:
        # Fecha o cursor e a conexão, se estiverem abertos
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
