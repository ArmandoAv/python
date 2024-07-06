import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

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
print("\nCreating an excel file with payments.")
df_merge_columns.to_excel(output_file, sheet_name = output_sheet, index = False)

# Load the workbook
wb = load_workbook(output_file)
ws = wb[output_sheet]

# Define the range of the table
tb_range = f"A1:{chr(65+len(df_merge_columns.columns)-1)}{len(df_merge_columns)+1}"

# Create a table
tb = Table(displayName="TablaPagos", ref=tb_range)

# Define the table style
tb_style = TableStyleInfo(
    # Predefined table style in Excel
    name="TableStyleMedium9",
    showFirstColumn=False,
    showLastColumn=False,
    showRowStripes=True,
    showColumnStripes=False
)
tb.tableStyleInfo = tb_style

# Add the table to the worksheet
ws.add_table(tb)

# Save the workbook
wb.save(output_file)
print(f"The table has been created in the Excel file: {output_file}")
