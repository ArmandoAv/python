import pandas as pd

# Input files
input_file1 = '../../data/uber_data1.xlsx'
input_file2 = '../../data/uber_data2.xlsx'
input_sheet = 'Sheet1'

# Output files
output_csv_file = '../../data/uber_data.csv'
output_excel_file = '../../data/uber_data.xlsx'
sheet_file = 'data'
output_excel_several_sheet_file = '../../data/uber_several_data.xlsx'
sheet_several_file1 = 'data1'
sheet_several_file2 = 'data2'

# Read the files with headers
df1 = pd.read_excel(input_file1, sheet_name = input_sheet, header = 0)
df2 = pd.read_excel(input_file2, sheet_name = input_sheet, header = 0)

# Show rows
print("The first DataFrame is:")
print(df1.head())
print("\nThe second DataFrame is:")
print(df2.head())

# Concatenate DataFrames
df = pd.concat([df1, df2], ignore_index = True)

# Create a new csv file
df.to_csv(output_csv_file, index = False)

# Create a new excel file
df.to_excel(output_excel_file, sheet_name = sheet_file, index=False)

#  Create a new excel file with two sheet
with pd.ExcelWriter(output_excel_several_sheet_file) as writer:
    # Write each DataFrame to a different sheet
    df1.to_excel(writer, sheet_name=sheet_several_file1, index=False)
    df2.to_excel(writer, sheet_name=sheet_several_file2, index=False)
