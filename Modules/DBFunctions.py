import re
class DBFunctions:
    
    def validar_cpf(cpf):
        padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(padrao_cpf, cpf))
        
    