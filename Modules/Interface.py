from Modules.DBFunctions import DBFunctions
from Modules.Connection import Connection
import os

class Interface:
    def __init__(self):
        self.dbFunctions = DBFunctions
        self.connection = Connection

    def start(self):
        print('=======================================================================================================================')
        print('Bem vindo ao FutSteps, o melhor software de monitoramento infatil do mercado!')
        option = int(input('Qual ação deseja realizar: \n1 - Visualizar Informações \n2 - Cadastrar Informações\n3 - Sair\n'))
        if (option == 1):
            ...
        elif(option == 2):
            self.__insertInfoInterface()

    def __insertInfoInterface(self):
        option = int(input('Qual tabela deseja inserir: \n1 - Inserir Jogador \n2 - Inserir Lesão\n3 - Inserir Treino\n'))
        if (option == 1 ):
            self.__insertJogador()
        elif(option == 2):
            # self.__insertLesao()
            ...
        elif(option == 3):
            # self.__insertTreino()
            ...
        else:
            ...
    
    def __insertJogador(self):
        os.system('cls')
        print("Insira os dados do jogador (*Obrigatório)")
        cpf = input('*Insira o CPF do jogador (formato xxx.xxx.xxx-x): ')
        while (not cpf):
            os.system('cls')
            print('O campo "CPF" é obrigatório, insira novamente!')
            cpf = input('*Insira o CPF do jogador: ')
        name = input('*Insira o nome do jogador: ')
        while(not name):
            print('O campo "Nome" é obrigatório, insira novamente!')
            name = input('*Insira o nome do jogador: ')
        height = float(input('Insira a altura do jogador: '))
        weight = float(input('Insira o peso do jogador: '))
        bornDate = input('*Data nascimento (dd/mm/aaaa): ')
        while(not bornDate):
            print('O campo "Data de nascimento" é obrigatório, insira novamente!')
            bornDate = input('*Data nascimento (dd/mm/aaaa): ')
        position = input('*Posição: ')
        while(not position):
            print('O campo "Posição" é obrigatório, insira novamente!')
            position = input('*Posição: ')
        numberOfGames = int(input('Numero de jogos: '))
        numberOfStarterGames = int(input('Numero de jogos como titular: '))
        club = input('Clube: ')
        guardian =  input('Responsavel: ')

        self.dbFunctions.insert('atleta',(cpf,name,height, weight, bornDate, position, numberOfGames, numberOfStarterGames, club,guardian), self.connection)
        
        


        