class AthleteQuery:
    
    def select_athlete_cpf_or_name(data, atribute ,connection):
        """
        Busca informações de um atleta no banco com base no CPF ou Nome.

        Args:
            data: CPF ou Nome do atleta.
            attribute: Indica se a busca será feita pelo 'CPF' ou 'NOME'.
            connection: Conexão com o banco de dados.

        Returns:
            Lista de resultados encontrados ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            if(atribute == 'CPF'):
                query = 'SELECT * FROM ATLETA WHERE CPF = %s'
            elif(atribute == 'NOME'):
                query = 'SELECT * FROM ATLETA WHERE NOME = %s'
            
            # Executa a query
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar atleta: {e} \nCPF/NOME Não Cadastrado")
            return []
        
    def select_player_statistics(data,connection):
        """
        Busca estatísticas de um jogador de linha no banco com base no CPF.

        Args:
            data: CPF do jogador.
            connection: Conexão com o banco de dados.

        Returns:
            Lista de estatísticas do jogador ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            query = 'SELECT * FROM LINHA WHERE CPF = %s' 
                                
            # Executa a query
            cursor.execute(query, (data,))
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar estatísticas: {e} \nCPF Não Cadastrado")
            return []
        
    def select_highest_goals_scores_players(connection):
        """
        Busca jogadores com número de gols acima da média.

        Args:
            connection: Conexão com o banco de dados.

        Returns:
            Lista de jogadores com número de gols acima da média ou uma lista vazia em caso de erro.
        """
        try:
            cursor = connection.cursor()
            query = 'SELECT A.NOME, A.CPF, A.CLUBE, L.GOLS FROM ATLETA A JOIN LINHA L \
	                    ON A.CPF = L.CPF WHERE L.GOLS > \
		                    (SELECT AVG(GOLS) FROM LINHA);' 
                      
            # Executa a query
            cursor.execute(query)
            output = cursor.fetchall()
            return output
        
        except Exception as e :
            print(f"Erro ao buscar estatísticas: {e}")
            return []     