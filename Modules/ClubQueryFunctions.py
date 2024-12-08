class ClubQuery:
    
    def select_club(data,connection, attribute):
        """
        Busca informações de um Clube no banco com base no Nome ou CNPJ.

        Args:
            data: Nome do Clube ou CNPJ
            connection: Conexão com o banco de dados.
            attribute: Atributo a ser buscado (Nome ou CNPJ)

        Returns:
            Lista de resultados encontrados ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            
            if attribute == 'CNPJ':
                query = 'SELECT * FROM CLUBE WHERE CNPJ = %s'
            else:
                query = 'SELECT * FROM CLUBE WHERE NOME = %s'
            
            #Executa a query com o dado passado
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar clube: {e} \nCLUBE Não Cadastrado")
            return []