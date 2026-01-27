import pyodbc

server = r'DESKTOP-M4RNLP7\SQLEXPRESS'
database = 'dbSifacPOS'
username = 'sa'
password = 'sa'
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_db_connection():
    try:
        connection = pyodbc.connect(connection_string)
        return connection
    except pyodbc.Error as e:
        print("Error connecting to database: ", e)
        return None
    
def close_db_connection(connection):
    if connection:
        connection.close()