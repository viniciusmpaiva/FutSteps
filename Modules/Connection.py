import psycopg2
import json

class Connection:
    def connectToDB(): 
        try:
            file = open("config.json","r")
            config = json.load(file)
            
            connection = psycopg2.connect(
                host=config["host"],
                port=config["port"],
                database=config["dbname"],
                user=config["user"],
                password=config["password"]
            )    
            cursor = connection.cursor()
            return cursor

        except Exception as e:
            print(f"Error connecting to the database !")