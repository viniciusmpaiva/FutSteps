class DBFunctions:
    def insert(table, data, connection):
        try:
            cursor = connection.cursor()
            placeholders = ", ".join(["%s" for _ in data])
            query = f'INSERT INTO {table} VALUES ({placeholders})'
            cursor.execute(query, data)
            connection.commit()
            return 200
        except Exception as e :
            return e
        
        