from Modules.DBFunctions import DBFunctions
from Modules.Connection import Connection
import os
from psycopg2 import errors

class Interface:
    def __init__(self):
        self.dbFunctions = DBFunctions
        self.connection = Connection.connectToDB()

    def start(self):
        print('=======================================================================================================================')
        print('BEM VINDO AO FUTSTEPS, O MELHOR SOFTWARE DE MONITORAMENTO INFATIL DO MERCADO!')
        option = int(input('QUAL AÇÃO DESEJA REALIZAR: \n1 - VISUALIZAR INFORMAÇÕES \n2 - CADASTRAR INFORMAÇÕES\n3 - SAIR\n'))
        if (option == 1):
            ...
        elif(option == 2):
            self.__insertInfoInterface()

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
        #Procurar CPF na tabela atleta
        cpf = self.get_valid_input('*INSIRA O CPF DO JOGADOR CADASTRADO(FORMATO XXX.XXX.XXX-X): ', self.validate_cpf, True)

        #Gols sofridos
        goalsSuffered = self.validade_intInput('INSIRA O NUMERO DE GOLS SOFRIDOS: ')
        
        #Gols sofridos/partida
        goalsSufferedPerGame = self.validate_floatInput('INSIRA O NUMERO DE GOLS SOFRIDOS POR PARTIDA: ')
        
        #Penaltis defendidos
        defendedPenalties = self.validade_intInput('INSIRA O NUMERO DE PÊNALTIS DEFENDIDOS: ')   
    
        #Defesas/jogo
        savesPerGame = self.validate_floatInput('INSIRA O NUMERO DE DEFESAS POR JOGO: ')

        #Gols sofridos fora da área
        goalsOutsideBox = self.validade_intInput('INSIRA O NUMERO DE GOLS SOFRIDOS FORA DA ÁREA: ') 

        #Defesas
        saves =  self.validade_intInput('INSIRA O NUMERO DE DEFESAS: ')
        
        #Defesas de fora da área
        savesOutsideBox = self.validade_intInput('INSIRA O NUMERO DE DEFESAS FORA DA ÁREA: ')

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
        #Procurar CPF na tabela atleta
        cpf = self.get_valid_input('*INSIRA O CPF DO JOGADOR CADASTRADO(FORMATO XXX.XXX.XXX-X): ', self.validate_cpf, True)

        #Gols
        goals = self.validade_intInput('INSIRA O NUMERO DE GOLS: ')

        #Assistências
        assists = self.validade_intInput('INSIRA O NUMERO DE ASSISTÊNCIAS: ')

        #Mapa de calor
        heatMap = input('INSIRA O MAPA DE CALOR: ')
        os.system('cls')

        #Erros capitais
        capitalErrors = self.validade_intInput('INSIRA O NUMERO DE ERROS CAPITAIS: ')

        #Chutes por jogo
        kicksPerGame  = self.validate_floatInput('INSIRA O NUMERO DE CHUTES POR JOGO: ')
        
        #Grandes chances criadas
        bigChancesCreated =  self.validade_intInput('INSIRA O NUMERO DE GRANDES CHANCES CRIADAS: ')

        #Passes completos por jogo
        completedPassesPerGame = self.validate_floatInput('INSIRA O NUMERO DE PASSES COMPLETOS POR JOGO: ')

        #Desarmes por jogo
        teacklesPerGame = self.validate_floatInput('INSIRA O NUMERO DE DESARMES POR JOGO: ')
        
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
        cpf = self.get_valid_input('*INSIRA O CPF DO RESPONSAVEL (FORMATO XXX.XXX.XXX-X): ', self.validate_cpf, True)

        #Nome
        name = self.get_valid_input('*INSIRA O NOME DO RESPONSAVEL: ', self.validate_name, True)

        #Data de nascimento
        #Dia
        day = self.get_valid_input('*DATA NASCIMENTO (DD/MM/AAAA): \nDIA: ', self.validate_day, True)

        #Mes
        month = self.get_valid_input('MÊS: ', self.validate_month, True)

        #Ano
        year = self.get_valid_input('ANO: ', self.validate_year, True)

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
        cnpj = self.get_valid_input('*INSIRA O CNPJ DO CLUBE (FORMATO XX.XXX.XXX/XXXX-XX): ', self.validate_cnpj, True)

        #Nome
        name = self.get_valid_input('*INSIRA O NOME DO CLUBE: ', self.validate_name, True)
        
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
        cpf = self.get_valid_input('*INSIRA O CPF DO JOGADOR (FORMATO XXX.XXX.XXX-X): ', self.validate_cpf, True)

        #Nome
        name = self.get_valid_input('*INSIRA O NOME DO JOGADOR: ', self.validate_name, True)

        #Altura
        height = self.validate_floatInput('INSIRA A ALTURA DO JOGADOR (EM METROS): ')

        #Peso
        weight = self.validate_floatInput('INSIRA O PESO DO JOGADOR (EM KG): ')

        #Data de nascimento
        print('*DATA NASCIMENTO (DD/MM/AAAA): ')

        #Dia
        day = self.get_valid_input('DIA: ', self.validate_day , True)
        
        #Mes
        month = self.get_valid_input('MÊS: ', self.validate_month, True)

        #Ano
        year = self.get_valid_input('ANO: ', self.validate_year, True)

        bornDate = f'{month}/{day}/{year}'

        #Posicao
        position = self.get_valid_input('INSIRA A POSIÇÃO DO JOGADOR (LINHA/GOLEIRO): ', self.validade_position, True)

        #Numero de jogos
        numberOfGames = self.validade_intInput('NUMERO DE JOGOS: ')

        #Numero de jogos como titular
        numberOfStarterGames = self.validade_intInput('NUMERO DE JOGOS COMO TITULAR: ')

        #Clube
        club = self.get_valid_input('CNPJ DO CLUBE: ', self.validate_cnpj)

        #Responsavel
        guardian = self.get_valid_input('CPF DO RESPONSÁVEL: ', self.validate_cpf)

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

        #FK nao encontrada
        # except errors.ForeignKeyViolation as e:
        #     constraint_name = e.diag.constraint_name

        #     #Clube nao encontrado
        #     if(constraint_name == "fk_atleta_clube"):
        #         print("ERRO! O CLUBE INSERIDO NÃO ESTÁ CADASTRADO")

        #     #Responsavel nao encontrado
        #     elif(constraint_name == "fk_atleta_responsavel"):
        #         print("ERRO! O RESPONSÁVEL INSERIDO NÃO ESTÁ CADASTRADO")

        #Erros no peso/altura
        except errors.NumericValueOutOfRange as e:
            print("ERRO! ALTURA/PESO INVÁLIDOS")
        
        #Nome excedeu numero de caracteres
        except errors.StringDataRightTruncation:
            print('ERRO! O TAMANHO DO NOME EXCEDEU O LIMITE DE 50 CARACTERES')

        except errors:
            print('ERRO AO INSERIR JOGADOR, TENTE NOVAMENTE !')
            
        

    #Funcao para validar input
    def get_valid_input(self, prompt, validation_func , mandatory = False):
        value = input(prompt)
        
        if not value and not mandatory:
            return value
        
        while not validation_func(value):
            os.system('cls')
            print('VALOR INVÁLIDO, INSIRA NOVAMENTE!')
            value = input(prompt)
        
        os.system('cls')
        return value

    
    #Funcao para validar CPF
    def validate_cpf(self, cpf):
        return len(cpf) == 14

    #Funcao para validar nome
    def validate_name(self, name):
        return 1 <= len(name) <= 50
        
    #Funcao para validar altura e peso
    def validate_floatInput(self, prompt):
        floatInput = input(prompt)
        return round(float(floatInput),2) if floatInput.isdecimal() else None

    #Funcao para validar dia
    def validate_day(self, day):
        return day.isdigit() and 1 <= int(day) <= 31

    #Funcao para validar mes
    def validate_month(self, month):
        return month.isdigit() and 1 <= int(month) <= 12
        
    def validate_year(self, year):
        return year.isdigit() and len(year) == 4

    def validade_position(self, position):
        return position.upper() in ['LINHA', 'GOLEIRO']

    def validade_intInput(self, prompt):
        value = input(prompt)
        return int(value) if value.isdigit() else None

    def validate_cnpj(self, cnpj):
        #Procurar cnpj na tabela clube
        return len(cnpj) == 18
