from Modules.Connection import Connection

connection = Connection.connectToDB()

connection.execute('SELECT * FROM ATLETA')
output = connection.fetchall()
print(*output, sep = '\n')