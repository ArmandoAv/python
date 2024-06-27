import pandas as pd
from decouple import config
from sqlalchemy import create_engine, exc

# Input file
input_file = '../../data/uber_data.csv'

# Output file
output_file = '../../data/driver.csv'

# Connection to the SQL Server database
server = str(config('DB_HOST'))
database = str(config('DB_NAME'))
username = str(config('DB_USR'))
password = str(config('DB_PWD'))

conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn_str)

# SQL script
table_name = 'TB_DRIVER'
query = f'SELECT * FROM {table_name}'

# Load table
def loadTable(input_file, table_name):
    try:
        # Load data from DataFrame to SQL Server
        df = pd.read_csv(input_file, header = 0)
        df.to_sql(table_name, con = engine, if_exists ='replace', index = False)
        print(f'Data successfully loaded into table {table_name} in SQL Server.')
    
    except exc.SQLAlchemyError as e:
        # Closing connection
        print(f'SQLAlchemy error: {str(e)}')
        engine.dispose()

# Read table
def readTable(query, table_name, output_file):
    try:
        # Read data from SQL Server
        df = pd.read_sql_query(query, con=engine)
        df.to_csv(output_file, index = False)
        print(f'The data was read from the table {table_name} in SQL Seerver.')
    
    except exc.SQLAlchemyError as e:
        # Closing connection
        print(f'SQLAlchemy error: {str(e)}')
        engine.dispose()

# Load TB_DRIVER table
loadTable(input_file=input_file,
          table_name=table_name)

# Read TB_DRIVER table
readTable(query=query,
          table_name=table_name,
          output_file=output_file)

# Closing connection
engine.dispose()
