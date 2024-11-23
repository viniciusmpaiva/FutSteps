from Modules.DBFunctions import select_athlete

# CPF do atleta para consulta
cpf = '123.456.789-02'

# Consulta o atleta pelo CPF
output = select_athlete(cpf)

# Imprime o resultado
if output:
    print("Informações do atleta:")
    for row in output:
        print(row)
else:
    print("Nenhum atleta encontrado ou erro na consulta.")
