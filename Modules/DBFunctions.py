
class DBFunctions:
    def insert(table, data, connection):
        cursor = connection.cursor()
        placeholders = ", ".join(["%s" for _ in data])
        query = f'INSERT INTO {table} VALUES ({placeholders})'
        cursor.execute(query, data)
        connection.commit()
    

        