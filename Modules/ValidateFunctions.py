import os
from Modules.DBFunctions import DBFunctions


class ValidateFunctions:
    
    def get_valid_input(prompt, validation_func , mandatory = False):
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
    def validate_cpf(cpf):
        dbFunctions = DBFunctions
        return len(cpf) == 14 and dbFunctions.validar_cpf(cpf)

    #Funcao para validar nome
    def validate_name(name):
        return 1 <= len(name) <= 50
        
    #Funcao para validar altura e peso
    def validate_floatInput(prompt):
        floatInput = input(prompt)
        return round(float(floatInput),2) if floatInput.isdecimal() else None

    #Funcao para validar dia
    def validate_day(day):
        return day.isdigit() and 1 <= int(day) <= 31

    #Funcao para validar mes
    def validate_month(month):
        return month.isdigit() and 1 <= int(month) <= 12
        
    #Funcao para validar ano
    def validate_year(year):
        return year.isdigit() and len(year) == 4

    #Funcao para validar posicao
    def validate_position(position):
        return position.upper() in ['LINHA', 'GOLEIRO']

    #Funcao para validar numero
    def validate_intInput(prompt):
        value = input(prompt)
        return int(value) if value.isdigit() else None

    #Funcao para validar cnpj
    def validate_cnpj(cnpj):
        #Procurar cnpj na tabela clube
        return len(cnpj) == 18