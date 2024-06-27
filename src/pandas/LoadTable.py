import pandas as pd
from decouple import config
from sqlalchemy import create_engine, exc

# Input files
input_amount_more_file = '../../data/amount_more40.csv'
input_amount_less_file = '../../data/amount_less40.csv'
input_pass_more_file = '../../data/passenger_more4.csv'
input_pass_less_file = '../../data/passenger_less4.csv'
input_time_pm_file = '../../data/time_pm.csv'
input_time_am_file = '../../data/time_am.csv'

# Connection to the SQL Server database
server = str(config('DB_HOST'))
database = str(config('DB_NAME'))
username = str(config('DB_USR'))
password = str(config('DB_PWD'))

conn_str = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(conn_str)

# Tables in SQL Server
amount_more_table = 'TB_AMOUNT_40'
amount_less_table = 'TB_AMOUNT'
pass_more_table = 'TB_PASSENGER_4'
pass_less_table = 'TB_PASSENGER'
time_pm_table = 'TB_TIME_PM'
time_am_table = 'TB_TIME_AM'

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

# Load TB_AMOUNT_40 table
loadTable(input_file=input_amount_more_file,
          table_name=amount_more_table)

# Load TB_AMOUNT table
loadTable(input_file=input_amount_less_file,
          table_name=amount_less_table)

# Load TB_PASSENGER_4 table
loadTable(input_file=input_pass_more_file,
          table_name=pass_more_table)

# Load TB_PASSENGER table
loadTable(input_file=input_pass_less_file,
          table_name=pass_less_table)

# Load TB_TIME_PM table
loadTable(input_file=input_time_pm_file,
          table_name=time_pm_table)

# Load TB_TIME_PM table
loadTable(input_file=input_time_am_file,
          table_name=time_am_table)

# Closing connection
engine.dispose()
