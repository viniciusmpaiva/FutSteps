# from Modules.Connection import Connection
from Modules.Interface import Interface
# connection = Connection.connectToDB()
# cursor = connection.cursor();
interface = Interface()
while True:
    interface.start()
    