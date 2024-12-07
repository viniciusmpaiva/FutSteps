from Modules.DBFunctions import DBFunctions
from Modules.AthleteQueryFunctions import AthleteQuery
from Modules.ClubQueryFunctions import ClubQuery
from Modules.ResponsibleQueryFunctions import ResponsibleQuery
from Modules.GoalkeeperQueryFunctions import GoalkeeperQuery
from Modules.Connection import Connection
import os

class Interface:
    ###################################################################
    # Inicializa os módulos e estabelece a conexão com o banco de dados
    ###################################################################
     
    def __init__(self):
        self.dbFunctions = DBFunctions
        self.athleteQuery = AthleteQuery
        self.clubQuery = ClubQuery
        self.responsibleQuery = ResponsibleQuery
        self.goalkeeperQuery = GoalkeeperQuery
        self.connection = Connection.connectToDB()

    def start(self):
        
        ########################################################################
        # Exibe o menu principal e direciona para as funcionalidades escolhidas.
        ########################################################################
        
        print('='*100)
        print('BEM VINDO AO FUTSTEPS, O MELHOR SOFTWARE DE MONITORAMENTO TALENTOS ESPORTIVOS DO MERCADO!\n')
        print('Aqui você pode visualizar e cadastrar informações sobre atletas, clubes e responsáveis.\n')
        
        option = int(input('QUAL AÇÃO DESEJA REALIZAR:  \
                           \n1 - VISUALIZAR INFORMAÇÕES \
                           \n2 - CADASTRAR INFORMAÇÕES \
                           \n3 - SAIR \
                           \nAÇÃO: '))
        
        if (option == 1):
            os.system('clear')
            self.__selectInfoInterface()
            
        elif (option == 2):
            os.system('clear')
            self.__insertInfoInterface()
            
        elif (option == 3):
            exit("\nSaindo...")
            
    ############################################################
    # Função que direciona para a interface de CONSULTA de dados 
    ############################################################
            
    def __selectInfoInterface(self):
        option = int(input('QUAL TABELA DESEJA VISUALIZAR OS DADOS: \
                           \n1 - TABELA ATLETA \
                           \n2 - TABELA CLUBE  \
                           \n3 - TABELA RESPONSÁVEL \
                           \nTABELA: '))
        if (option == 1):
            os.system('clear')
            self.__selectAthlete()
        
        elif (option == 2):
            os.system('clear')
            self.__selectClub()
            
        elif(option == 3):
            os.system('clear')
            self.__selectResponsible()
            
    #############################################################################
    # FUNÇÕES DE SELEÇÃO DE DADOS DOS RESPONSÁVEIS
    #############################################################################    
    def __selectResponsible(self):
        os.system('clear')
        option = int(input('QUAL ATRIBUTO DESEJA CONSULTAR O RESPONSÁVEL: \
                               \n1 - CPF \
                               \n2 - NOME \
                               \nATRIBUTO: '))
        if (option == 1):
            # Seleciona o responsável pelo CPF
                cpf = input('*INSIRA O [CPF] DO RESPONSÁVEL O QUAL DESEJA CONSULTAR (FORMATO XXX.XXX.XXX-X): ')
                
                while (self.dbFunctions.validar_cpf(cpf) == False):
                    os.system('clear')
                    print('O CAMPO "CPF" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                    cpf = input('*INSIRA O CPF DO RESPONSÁVEL: ')
                    
                # Consulta o RESPONSÁVEL no banco de dados com base no ATRIBUTO CPF    
                output = self.responsibleQuery.select_responsible(cpf, 'CPF' ,self.connection)
                
        elif (option == 2):
                # Seleciona o responsável pelo nome
                nome = input('*INSIRA O [NOME] DO RESPONSÁVEL O QUAL DESEJA CONSULTAR : ')
                
                while(not nome):
                    os.system('clear')
                    print('O CAMPO "NOME" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                    nome = input('*INSIRA O NOME DO RESPONSÁVEL: ')
                    
                # Consulta o RESPONSÁVEL no banco de dados com base no ATRIBUTO NOME
                output = self.responsibleQuery.select_responsible(nome, 'NOME' ,self.connection)
                
        if output:
            # Exibe as informações do responsável

                print("\nINFORMAÇÕES DO RESPONSÁVEL ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[0]}  
                    👤 Nome: {row[1]}  
                    🎂 Data de Nascimento: {row[2]}  
                    """
                    print(formatted_output)
                    
        else:
            print(f"\nNENHUM RESPONSAVEL ENCONTRADO COM O CPF/NOME.\n")
            
    #############################################################################
    # FUNÇÕES DE SELEÇÃO DE DADOS DOS CLUBES
    #############################################################################
    def __selectClub(self):
        os.system('clear')
        nome = input('DIGITE O NOME DO CLUBE PARA OBTER OS DADOS DO CLUBE: ')
        
        #Seleciona o clube pelo nome
        while(not nome):
            os.system('clear')
            print('O CAMPO "NOME" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
            nome = input('*INSIRA O NOME DO CLUBE: ')
        
        # Consulta o CLUBE no banco de dados com base no ATRIBUTO NOME
        output = self.clubQuery.select_club(nome, self.connection)
        
        if output:
            # Exibe as informações do clube
            
            print("\nINFORMAÇÕES DO CLUBE ENCONTRADAS:")
            
            for row in output:
                formatted_output = f"""
                CNPJ: {row[0]}  
                🏟️ Clube: {row[1]}  
                """
                print(formatted_output)
                
        else:
            print(f"\nNENHUM CLUBE ENCONTRADO COM ESSE NOME.\n")
    
    ###################################################################################################################
    # FUNÇÕES DE SELEÇÃO DE DADOS DOS ATLETAS
    ###################################################################################################################
    def __selectAthlete(self):
        os.system('clear')
        action = int(input('QUAIS AÇÕES DESEJA REALIZAR \n1 - CONSULTAR OS DADOS DO ATLETA \
                                                        \n2 - VISUALIZAR AS ESTATÍSTICAS DO ATLETA DE LINHA \
                                                        \n3 - VISUALIZAR OS ATLETAS QUE MAIS FIZERAM GOLS \
                                                        \n4 - VISUALIZAR OS GOLEIROS COM OS MAIORES NÚMEROS DE PÊNALTIS DEFENDIDOS \
                                                        \n5 - VISUALIZAR ESTATÍSTICAS DO GOLEIRO \
                                                        \nAÇÃO: '))
        # Consulta os dados do atleta
        if (action == 1):
            os.system('clear')
            option = int(input('QUAL ATRIBUTO DESEJA CONSULTAR O ATLETA: \
                               \n1 - CPF \
                               \n2 - NOME \
                               \nATRIBUTO: '))
            
            # Consulta o ATLETA no banco de dados com base no ATRIBUTO CPF
            if (option == 1):
                cpf = input('*INSIRA O [CPF] DO JOGADOR O QUAL DESEJA CONSULTAR (FORMATO XXX.XXX.XXX-X): ')
                
                # Validação do CPF
                while (self.dbFunctions.validar_cpf(cpf) == False):
                    os.system('clear')
                    print('O CAMPO "CPF" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                    cpf = input('*INSIRA O CPF DO JOGADOR: ')
                    
                output = self.athleteQuery.select_athlete_cpf_or_name(cpf, 'CPF' ,self.connection)
                
            # Consulta o ATLETA no banco de dados com base no ATRIBUTO NOME 
            elif (option == 2):
                nome = input('*INSIRA O [NOME] DO JOGADOR O QUAL DESEJA CONSULTAR : ')
                while(not nome):
                    os.system('clear')
                    print('O CAMPO "NOME" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                    nome = input('*INSIRA O NOME DO JOGADOR: ')
                    
                output = self.athleteQuery.select_athlete_cpf_or_name(nome, 'NOME' ,self.connection)
                
            if output:
                # Exibe as informações do atleta
                
                print("\nINFORMAÇÕES DO ATLETA ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[0]}  
                    👤 Nome: {row[1]}  
                    📏 Altura: {row[2]} m  
                    ⚖️ Peso: {row[3]} kg  
                    🎂 Data de Nascimento: {row[4]}  
                    🏅 Posição: {row[5]}  
                    📊 Número de Jogos: {row[6]}  
                    🔝 Jogos como Titular: {row[7]}  
                    🏟️ Clube: {row[8]}  
                    👨‍👩‍👧 Responsável: {row[9]}  
                    """
                    print(formatted_output)
            else:
                print(f"\nNENHUM ATLETA ENCONTRADO COM O CPF/NOME.\n")
        
        # Exibe as estatísticas do atleta de linha
        elif (action == 2):
            os.system('clear')
            cpf = input('*INSIRA O [CPF] DO JOGADOR QUE DESEJA VISUALIZAR AS ESTATÍSTICAS (FORMATO XXX.XXX.XXX-X): ')
            
            # Validação do CPF
            while (self.dbFunctions.validar_cpf(cpf) == False):
                os.system('clear')
                print('O CAMPO "CPF" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                cpf = input('*INSIRA O CPF DO JOGADOR: ')
                
            # Consulta as estatísticas do ATLETA DE LINHA no banco de dados com base no ATRIBUTO CPF    
            output = self.athleteQuery.select_player_statistics(cpf, self.connection)
                
            if output:
                # Exibe as estatísticas do atleta de linha

                print("\nINFORMAÇÕES DO ATLETA ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[0]}
                    ⚽ Gols: {row[1]}
                    🎯 Assistências: {row[2]}
                    🗺️ Mapa de Calor: {row[3]}
                    ❌ Erros Capitais: {row[4]}
                    🚀 Chutes por Jogo: {row[5]}
                    🌟 Grandes Chances Criadas: {row[6]}
                    🎯 Passes Certos por Partida: {row[7]}
                    🛡️ Desarmes por Jogo: {row[8]}
                    """
                    print(formatted_output)
            else:
                print(f"\nNENHUM ATLETA ENCONTRADO COM O CPF INFORMADO.\n")
                
       # Exibe os atletas que mais fizeram gols         
        elif (action == 3):
            output = self.athleteQuery.select_highest_goals_scores_players(self.connection)
            
            if output:
                # Exibe os atletas que mais fizeram gols
                
                print("\nINFORMAÇÕES DOS ATLETAS ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[1]}
                    👤 NOME: {row[0]}
                    🏟️ CLUBE: {row[2]}
                    ⚽ GOLS: {row[3]}
                    """
                    print(formatted_output)
            else:
                print(f"\nNENHUM ATLETA ENCONTRADO. \n")
        
        # Exibe os goleiros com os maiores números de pênaltis defendidos
        elif (action == 4):
            output = self.goalkeeperQuery.select_highest_penaltis_defenses_goalkeepers(self.connection)
            
            if output:
                # Exibe os goleiros com os maiores números de pênaltis defendidos
                
                print("\nINFORMAÇÕES DOS GOLEIROS ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[1]}
                    👤 NOME: {row[0]}
                    🏟️ CLUBE: {row[2]}
                    🛡️ Pênaltis Defendidos: {row[3]}
                    """
                    print(formatted_output)
            else:
                print(f"\nNENHUM GOLEIRO ENCONTRADO. \n")
                
        # Exibe as estatísticas do goleiro
        elif (action == 5):
            os.system('clear')
            cpf = input('*INSIRA O [CPF] DO JOGADOR QUE DESEJA VISUALIZAR AS ESTATÍSTICAS (FORMATO XXX.XXX.XXX-X): ')
            
            # Validação do CPF
            while (self.dbFunctions.validar_cpf(cpf) == False):
                os.system('clear')
                print('O CAMPO "CPF" É OBRIGATÓRIO, INSIRA NOVAMENTE!')
                cpf = input('*INSIRA O CPF DO JOGADOR: ')
                
            output = self.goalkeeperQuery.select_goalkeeper_statistics(cpf, self.connection)
            
            if output:
                # Exibe as estatísticas do goleiro
                print("\nINFORMAÇÕES DO GOLEIRO ENCONTRADAS:")
                
                for row in output:
                    formatted_output = f"""
                    CPF: {row[0]}
                    🛡️ Gols Sofridos: {row[1]}
                    📊 Gols Sofridos por Partida: {row[2]}
                    🥅 Pênaltis Defendidos: {row[3]}
                    🧤 Defesas por Jogo: {row[4]}
                    🔥 Gols Sofridos Fora da Área: {row[5]}
                    🚨 Defesas Realizadas: {row[6]}
                    🌍 Defesas Realizadas Fora da Área: {row[7]}
                    """
                    print(formatted_output)
            else:
                print(f"\nNENHUM GOLEIRO ENCONTRADO COM O CPF INFORMADO.\n")
                        

        


        