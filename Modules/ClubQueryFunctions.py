class ClubQuery:
    
    def select_club(data,connection):
        """
        Busca informações de um Clube no banco com base no Nome.

        Args:
            data: Nome do Clube
            connection: Conexão com o banco de dados.

        Returns:
            Lista de resultados encontrados ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            query = 'SELECT * FROM CLUBE WHERE NOME = %s'
            
            #Executa a query com o dado passado
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar clube: {e} \nCLUBE Não Cadastrado")
            return []