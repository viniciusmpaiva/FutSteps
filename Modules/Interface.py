from Modules.DBFunctions import DBFunctions
from Modules.AthleteQueryFunctions import AthleteQuery
from Modules.ClubQueryFunctions import ClubQuery
from Modules.ResponsibleQueryFunctions import ResponsibleQuery
from Modules.GoalkeeperQueryFunctions import GoalkeeperQuery
from Modules.Connection import Connection
from Modules.ValidateFunctions import ValidateFunctions
import os
from psycopg2 import errors

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
        self.validateFunctions = ValidateFunctions

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
        
        else:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
            self.start()


    ############################################################
    # Função que direciona para a interface de INSERCAO de dados 
    ############################################################
    def __insertInfoInterface(self):
        os.system('cls')
        option = int(input('QUAL TABELA DESEJA INSERIR: \n1 - INSERIR JOGADOR\n2 - INSERIR CLUBE\n3 - INSERIR RESPONSAVEL\n4 - INSERIR ESTATISTICAS ATLETA LINHA\n5 - INSERIR ESTATISTICAS ATLETA GOLEIRO\n'))
        if (option == 1 ):
            self.__insertJogador()
        elif(option == 2):
            self.__insertClube()
        elif(option == 3):
            self.__insertResponsavel()
        elif(option == 4):
            self.__insertLinha()
        elif(option == 5):
            self.__insertGoleiro()


    #Funcao para inserir estatisticas de goleiro
    def __insertGoleiro(self):
        print('INSIRA AS ESTATÍSTICAS DO GOLEIRO (*OBRIGATÓRIO)')
        
        #CPF
        cpf = self.validateFunctions.get_valid_input('*INSIRA O CPF DO JOGADOR CADASTRADO(FORMATO XXX.XXX.XXX-X): ', self.validateFunctions.validate_cpf, True)
        output = self.athleteQuery.select_athlete_cpf_or_name(cpf, 'CPF' ,self.connection)
        if(len(output) == 0):
            print('ERRO! CPF DO JOGADOR NÃO ENCONTRADO')
            return

        #Gols sofridos
        goalsSuffered = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE GOLS SOFRIDOS: ')
        
        #Gols sofridos/partida
        goalsSufferedPerGame = self.validateFunctions.validate_floatInput('INSIRA O NUMERO DE GOLS SOFRIDOS POR PARTIDA: ')
        
        #Penaltis defendidos
        defendedPenalties = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE PÊNALTIS DEFENDIDOS: ')   
    
        #Defesas/jogo
        savesPerGame = self.validateFunctions.validate_floatInput('INSIRA O NUMERO DE DEFESAS POR JOGO: ')

        #Gols sofridos fora da área
        goalsOutsideBox = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE GOLS SOFRIDOS FORA DA ÁREA: ') 

        #Defesas
        saves =  self.validateFunctions.validate_intInput('INSIRA O NUMERO DE DEFESAS: ')
        
        #Defesas de fora da área
        savesOutsideBox = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE DEFESAS FORA DA ÁREA: ')

        #Tratamento de excessoes
        try:
            self.dbFunctions.insert('goleiro',(cpf,goalsSuffered,goalsSufferedPerGame, defendedPenalties, savesPerGame,goalsOutsideBox,saves,savesOutsideBox), self.connection)

            print("DADOS INSERIDOS COM SUCESSO!")
        #PK duplicada
        except errors.UniqueViolation:
            print('ERRO! CPF DO JOGADOR JÁ INSERIDO!')

        #FK nao encontrada
        except errors.ForeignKeyViolation:
            print('ERRO! CPF DO JOGADOR NÃO ENCONTRADO')

        #Erros gerais
        except errors:
            print('ERRO AO INSERIR ESTATÍSTICAS DO ATLETA DE GOLEIRO, TENTE NOVAMENTE !')


    #Funcao para inserir estatisticas de linha
    def __insertLinha(self):
        print('INSIRA AS ESTATÍSTICAS DO ATLETA DE LINHA (*OBRIGATÓRIO)')

        #CPF
        cpf = self.validateFunctions.get_valid_input('*INSIRA O CPF DO JOGADOR CADASTRADO(FORMATO XXX.XXX.XXX-X): ', self.validateFunctions.validate_cpf, True)
        output = self.athleteQuery.select_athlete_cpf_or_name(cpf, 'CPF' ,self.connection)
        if(len(output) == 0):
            print('ERRO! CPF DO JOGADOR NÃO ENCONTRADO')
            return

        #Gols
        goals = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE GOLS: ')

        #Assistências
        assists = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE ASSISTÊNCIAS: ')

        #Mapa de calor
        heatMap = input('INSIRA O MAPA DE CALOR: ')
        os.system('cls')

        #Erros capitais
        capitalErrors = self.validateFunctions.validate_intInput('INSIRA O NUMERO DE ERROS CAPITAIS: ')

        #Chutes por jogo
        kicksPerGame  = self.validateFunctions.validate_floatInput('INSIRA O NUMERO DE CHUTES POR JOGO: ')
        
        #Grandes chances criadas
        bigChancesCreated =  self.validateFunctions.validate_intInput('INSIRA O NUMERO DE GRANDES CHANCES CRIADAS: ')

        #Passes completos por jogo
        completedPassesPerGame = self.validateFunctions.validate_floatInput('INSIRA O NUMERO DE PASSES COMPLETOS POR JOGO: ')

        #Desarmes por jogo
        teacklesPerGame = self.validateFunctions.validate_floatInput('INSIRA O NUMERO DE DESARMES POR JOGO: ')
            
        #Tratamento de excessoes
        try:
            self.dbFunctions.insert('linha',(cpf,goals, assists, heatMap, capitalErrors, kicksPerGame, bigChancesCreated, completedPassesPerGame, teacklesPerGame), self.connection)

            print('DADOS INSERIDOS COM SUCESSO!')
        #PK duplicada
        except errors.UniqueViolation:
            print('ERRO! CPF DO JOGADOR JÁ INSERIDO!')

        #FK nao encontrada
        except errors.ForeignKeyViolation:
            print('ERRO! CPF DO JOGADOR NÃO ENCONTRADO')

        #Erros gerais
        except errors:
            print('ERRO AO INSERIR ESTATÍSTICAS DO ATLETA DE LINHA, TENTE NOVAMENTE !')
            

    def __insertResponsavel(self):
        print('INSIRA OS DADOS DO RESPONSAVEL (*OBRIGATÓRIO)')

        #CPF
        cpf = self.validateFunctions.get_valid_input('*INSIRA O CPF DO RESPONSAVEL (FORMATO XXX.XXX.XXX-X): ', self.validateFunctions.validate_cpf, True)
        output = self.athleteQuery.select_athlete_cpf_or_name(cpf, 'CPF' ,self.connection)
        if(len(output) != 0):
            print('ERRO! CPF JA INSERIDO!')
            return
        
        #Nome
        name = self.validateFunctions.get_valid_input('*INSIRA O NOME DO RESPONSAVEL: ', self.validate_name, True)

        #Data de nascimento
        #Dia
        day = self.validateFunctions.get_valid_input('*DATA NASCIMENTO (DD/MM/AAAA): \nDIA: ', self.validate_day, True)

        #Mes
        month = self.validateFunctions.get_valid_input('MÊS: ', self.validate_month, True)

        #Ano
        year = self.validateFunctions.get_valid_input('ANO: ', self.validate_year, True)

        bornDate = f'{month}/{day}/{year}'

        #Tratamento de excessoes
        try:
            self.dbFunctions.insert('responsavel',(cpf,name,bornDate), self.connection)
            print('DADOS INSERIDOS COM SUCESSO!')

        #PK duplicada
        except errors.UniqueViolation:
            print('ERRO! CPF DO RESPONSÁVEL JÁ INSERIDO')

        #Data mal formatada
        except errors.DatetimeFieldOverflow:
            print('ERRO! DATA MAL FORMATADA !')
        
        #Nome excedeu numero de caracteres
        except errors.StringDataRightTruncation:
            print('ERRO! O TAMANHO DO NOME EXCEDEU O LIMITE DE 50 CARACTERES')

        #Erros gerais
        except errors:
            print('ERRO AO INSERIR RESPONSÁVEL, TENTE NOVAMENTE !')


    
    def __insertClube(self):
        os.system('cls')
        print('INSIRA OS DADOS DO CLUBE (*OBRIGATÓRIO)')

        #CNPJ
        cnpj = self.validateFunctions.get_valid_input('*INSIRA O CNPJ DO CLUBE (FORMATO XX.XXX.XXX/XXXX-XX): ', self.validate_cnpj, True)

        #Nome
        name = self.validateFunctions.get_valid_input('*INSIRA O NOME DO CLUBE: ', self.validate_name, True)
        
        #Tratamento de excessoes
        try:
            self.dbFunctions.insert('clube',(cnpj,name), self.connection)
            print('DADOS INSERIDOS COM SUCESSO!')

        #PK duplicada
        except errors.UniqueViolation:
            print('ERRO! CNPJ DO CLUBE JÁ INSERIDO')

        #CNPJ mal formatado
        except errors.CheckViolation:
            print('ERRO! CNPJ MAL FORMATADO')

        #Nome excedeu numero de caracteres
        except errors.StringDataRightTruncation:
            print('ERRO! O TAMANHO DO NOME EXCEDEU O LIMITE DE 50 CARACTERES')
            
        #Erros gerais
        except errors:
            print('ERRO AO INSERIR CLUBE, TENTE NOVAMENTE !')
        
    

    def __insertJogador(self):
        os.system('cls')
        print("INSIRA OS DADOS DO JOGADOR (*OBRIGATÓRIO)")

        #CPF
        cpf = self.validateFunctions.get_valid_input('INSIRA O CPF DO JOGADOR (FORMATO XXX.XXX.XXX-X): ', self.validateFunctions.validate_cpf, True)
        output = self.athleteQuery.select_athlete_cpf_or_name(cpf, 'CPF' ,self.connection)
        if(len(output) != 0):
            print('ERRO! CPF JA INSERIDO!')
            return

        #Nome
        name = self.validateFunctions.get_valid_input('*INSIRA O NOME DO JOGADOR: ', self.validateFunctions.validate_name, True)

        #Altura
        height = self.validateFunctions.validate_floatInput('INSIRA A ALTURA DO JOGADOR (EM METROS): ')

        #Peso
        weight = self.validateFunctions.validate_floatInput('INSIRA O PESO DO JOGADOR (EM KG): ')

        #Data de nascimento
        print('*DATA NASCIMENTO (DD/MM/AAAA): ')

        #Dia
        day = self.validateFunctions.get_valid_input('DIA: ', self.validateFunctions.validate_day , True)
        
        #Mes
        month = self.validateFunctions.get_valid_input('MÊS: ', self.validateFunctions.validate_month, True)

        #Ano
        year = self.validateFunctions.get_valid_input('ANO: ', self.validateFunctions.validate_year, True)

        bornDate = f'{month}/{day}/{year}'

        #Posicao
        position = self.validateFunctions.get_valid_input('INSIRA A POSIÇÃO DO JOGADOR (LINHA/GOLEIRO): ', self.validateFunctions.validate_position, True)

        #Numero de jogos
        numberOfGames = self.validateFunctions.validate_intInput('NUMERO DE JOGOS: ')

        #Numero de jogos como titular
        numberOfStarterGames = self.validateFunctions.validate_intInput('NUMERO DE JOGOS COMO TITULAR: ')

        #Clube
        club = self.validateFunctions.get_valid_input('CNPJ DO CLUBE: ', self.validateFunctions.validate_cnpj)
        if(len(club) >0):
            print('Entrou aqui')
            output = self.clubQuery.select_club(club, self.connection, 'CNPJ')
            if(len(output) == 0):
                print('ERRO! CNPJ DO CLUBE NÃO ENCONTRADO')
                return
        else:
            club = None

       
        #Responsavel
        guardian = self.validateFunctions.get_valid_input('CPF DO RESPONSÁVEL: ', self.validateFunctions.validate_cpf)
        if(len(guardian) > 0):
            output = self.responsibleQuery.select_responsible(guardian, 'CPF' ,self.connection)
            if(len(output) == 0):
                print('ERRO! CPF DO RESPONSÁVEL NÃO ENCONTRADO')
                return
        else:
            guardian = None
    
        
        #Tratamento de excessoes
        try:
            self.dbFunctions.insert('atleta',(cpf,name,height, weight, bornDate, position, numberOfGames, numberOfStarterGames, club,guardian), self.connection)

            print('DADOS INSERIDOS COM SUCESSO!')

        #PK duplicada
        except errors.UniqueViolation:
            print('ERRO! CPF DO JOGADOR JÁ INSERIDO!')

        #Data mal formatada
        except errors.DatetimeFieldOverflow:
            print('ERRO! DATA MAL FORMATADA !')

        #Erros Checks
        except errors.CheckViolation as e:
            constraint_name = e.diag.constraint_name

            #CPF mal formatado
            if(constraint_name == "ck_cpf_atleta"):
                print('ERRO! CPF MAL FORMATADO!')

            #Posicao invalida
            elif(constraint_name == "ck_posicao_atleta"):
                print("ERRO! POSIÇÃO INVÁLIDA")

       # FK nao encontrada
        except errors.ForeignKeyViolation as e:
            constraint_name = e.diag.constraint_name

            #Clube nao encontrado
            if(constraint_name == "fk_atleta_clube"):
                print("ERRO! O CLUBE INSERIDO NÃO ESTÁ CADASTRADO")

            #Responsavel nao encontrado
            elif(constraint_name == "fk_atleta_responsavel"):
                print("ERRO! O RESPONSÁVEL INSERIDO NÃO ESTÁ CADASTRADO")

        #Erros no peso/altura
        except errors.NumericValueOutOfRange as e:
            print("ERRO! ALTURA/PESO INVÁLIDOS")
        
        #Nome excedeu numero de caracteres
        except errors.StringDataRightTruncation:
            print('ERRO! O TAMANHO DO NOME EXCEDEU O LIMITE DE 50 CARACTERES')

        except errors:
            print('ERRO AO INSERIR JOGADOR, TENTE NOVAMENTE !')
            
            
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

