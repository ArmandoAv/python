import pandas as pd

# Input files
input_csv = '../../data/uber_data.xlsx'
input_txt = '../../data/payment.txt'

# Output_file
output_file = '../../data/payment.xlsx'
output_sheet = 'dataPayments'

# DataFrame columns
columns = ['DriverID','tpep_pickup_datetime','tpep_dropoff_datetime',
           'passenger_count','payment_type','total_amount']
columns_merge = ['DriverID','tpep_pickup_datetime','tpep_dropoff_datetime',
                 'passenger_count','payment_type','payment','total_amount']

# Create DataFrame
df_txt = pd.read_csv(input_txt, sep=',', header = 0)
df_csv = pd.read_excel(input_csv, header = 0)

# Create DataFrame with some columns
df_csv_columns = df_csv[columns]

# Merge DataFrames
df_merge = pd.merge(df_csv_columns, df_txt, on='payment_type', how='left', left_index = False, right_index = False)
df_merge_columns = df_merge[columns_merge]
print("The merged DataFrame has the following columns:")
print(df_merge_columns.head())

# Create excel file
print("\nCreating a excel file with payments.")
df_merge_columns.to_excel(output_file, sheet_name = output_sheet, index = False)
