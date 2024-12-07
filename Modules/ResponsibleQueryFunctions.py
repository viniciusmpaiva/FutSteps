class ResponsibleQuery:

    def select_responsible(data, atribute ,connection):
        """
        Busca informações de um responsável no banco com base no CPF ou Nome.

        Args:
            data: Valor do atributo (CPF ou Nome).
            atribute: Tipo de atributo ('CPF' ou 'NOME').
            connection: Conexão com o banco de dados.

        Returns:
            Lista de resultados encontrados ou uma lista vazia em caso de erro.
        """
        
        try:
            # Cria um cursor para executar comandos SQL
            cursor = connection.cursor()
            if(atribute == 'CPF'):
                query = 'SELECT * FROM RESPONSAVEL WHERE CPF = %s'
            elif(atribute == 'NOME'):
                query = 'SELECT * FROM RESPONSAVEL WHERE NOME = %s'
                
            #Executa a query com o dado passado
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar responsavel: {e} \nCPF/NOME Não Cadastrado")
            return []
        