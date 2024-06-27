# python

In this project some aspects of programming in Python will be seen, the programs executed are in a Windows environment.

You need a virtual Python environment, the following command must be executed from a terminal

python -m venv venv

To activate the virtual environment, the following command must be executed

venv\Scripts\activate

You need to run the following command to install all Python packages

pip install -r requirements.txt

To deactivate the virtual environment, the following command must be executed

venv\Scripts\deactivate

You need to install a SQL server and run the databaseTables.sql script located in the database folder

You need to create an .env file in the main folder of this project, with the SQL Server connection parameters

```
DB_HOST = localhost
DB_NAME = your_database_name
DB_USR = your_database_user
DB_PWD = your_database_password
```
