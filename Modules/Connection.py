import psycopg2
import json

class Connection:
    @staticmethod
    def connectToDB(): 
        try:
            # Abre e lê o arquivo de configuração
            with open("config.json", "r") as file:
                config = json.load(file)
            
            # Cria a conexão com o banco de dados
                connection = psycopg2.connect(
                host=config["host"],
                port=config["port"],
                database=config["dbname"],
                user=config["user"],
                password=config["password"]
            )
            return connection
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
            return None
