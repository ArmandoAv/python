import pandas as pd

# Input files
input_file1 = '../../data/uber_date1.xlsx'
input_file2 = '../../data/uber_date2.xlsx'
input_sheet = 'Sheet1'

# Output files
output_clean_file = '../../data/uber_clean_data.xlsx'
output_ok_file = '../../data/uber_ok_data.xlsx'
output_error_file = '../../data/uber_error_data.xlsx'
output_sheet = 'Sheet1'

# Default data
default_date = '1900-01-01 00:00:00'
default_longitude = 0
default_latitude = 0
default_passenger = -1
default_amount = -9999

# Check columns
check_columns = ['tpep_pickup_datetime', 'passenger_count', 'pickup_longitude', 'pickup_latitude',
                 'dropoff_longitude', 'dropoff_latitude', 'total_amount']

# Read inpur files
df1 = pd.read_excel(input_file1, sheet_name = input_sheet, header = 0)
df2 = pd.read_excel(input_file2, sheet_name = input_sheet, header = 0)

# Convert dates
df1['tpep_pickup_datetime'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
df2['tpep_pickup_datetime'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Concatenate files
dftotal = pd.concat([df1, df2], ignore_index = True)

# Create error and ok data files
dfok = dftotal[dftotal[check_columns].notnull().all(axis=1)]
dferror = dftotal[dftotal[check_columns].isnull().any(axis=1)]

# Clean data
dftotal['tpep_pickup_datetime'] = dftotal['tpep_pickup_datetime'].fillna(default_date)
dftotal['passenger_count'] = dftotal['passenger_count'].fillna(default_passenger)
dftotal['pickup_longitude'] = dftotal['pickup_longitude'].fillna(default_longitude)
dftotal['pickup_latitude'] = dftotal['pickup_latitude'].fillna(default_latitude)
dftotal['dropoff_longitude'] = dftotal['dropoff_longitude'].fillna(default_longitude)
dftotal['dropoff_latitude'] = dftotal['dropoff_latitude'].fillna(default_latitude)
dftotal['total_amount'] = dftotal['total_amount'].fillna(default_amount)

# Load outpuf file
print("Loading the final excel files.")
dftotal.to_excel(output_clean_file, sheet_name = output_sheet, index = False)
dfok.to_excel(output_ok_file, sheet_name = output_sheet, index = False)
dferror.to_excel(output_error_file, sheet_name = output_sheet, index = False)
