class GoalkeeperQuery:
    def select_goalkeeper_statistics(data,connection):
        """
        Busca as Estatítiscas de um Goleiro no banco com base no CPF.

        Args:
            data: CPF do Goleiro.
            connection: Conexão com o banco de dados.

        Returns:
            Lista de resultados encontrados ou uma lista vazia em caso de erro.
        """
        
        try:
            cursor = connection.cursor()
            query = 'SELECT * FROM GOLEIRO WHERE CPF = %s' 
            
             # Executa a consulta com o CPF fornecido
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar estatísticas: {e} \nCPF Não Cadastrado")
            return []       

    def select_highest_penaltis_defenses_goalkeepers(connection):
        """
        Busca goleiros com número de pênaltis defendidos acima da média.

        Args:
            connection: Conexão com o banco de dados.

        Returns:
            Lista de goleiros que defendem pênaltis acima da média ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            query = 'SELECT A.NOME, A.CPF, A.CLUBE, G.PENALTISDEFENDIDOS \
                        FROM ATLETA A JOIN GOLEIRO G ON A.CPF = G.CPF \
                            WHERE G.PENALTISDEFENDIDOS > (SELECT AVG(PENALTISDEFENDIDOS) FROM GOLEIRO);' 
                            
            # Executa a consulta
            cursor.execute(query)
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar estatísticas: {e}")
            return []