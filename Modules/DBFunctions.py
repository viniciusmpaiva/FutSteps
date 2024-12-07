class DBFunctions:
    def insert(table, data, connection):
        cursor = connection.cursor()
        placeholders = ", ".join(["%s" for _ in data])
        query = f'INSERT INTO {table} VALUES ({placeholders})'
        cursor.execute(query, data)
        connection.commit()
     
    def validar_cpf(cpf):
        padrao_cpf = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
        return bool(re.match(padrao_cpf, cpf))
