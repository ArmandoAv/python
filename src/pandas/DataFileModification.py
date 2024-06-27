import pandas as pd

input_excel_file = '../../data/uber_several_data.xlsx'
input_sheet1 = 'data1'
input_sheet2 = 'data2'
output_pass_more_csv_file = '../../data/passenger_more4.csv'
output_pass_less_csv_file = '../../data/passenger_less4.csv'
output_amount_more_csv_file = '../../data/amount_more40.csv'
output_amount_less_csv_file = '../../data/amount_less40.csv'
output_time_pm_csv_file = '../../data/time_pm.csv'
output_time_am_csv_file = '../../data/time_am.csv'
output_excel_file = '../../data/data_topics.xlsx'
output_sheet_pass_more4 = 'passMoreFour'
output_sheet_pass_less4 = 'passLessFour'
output_sheet_amount_more40 = 'amountMoreForty'
output_sheet_amount_less40 = 'amountLessForty'
output_sheet_time_pm = 'timePM'
output_sheet_time_am = 'timeAM'

# Read excel file with two sheets
df1 = pd.read_excel(input_excel_file, sheet_name = input_sheet1, header = 0)
print("The first sheet from the excel file is:")
print(df1.head())

df2 = pd.read_excel(input_excel_file, sheet_name = input_sheet2, header = 0)
print("The second sheet from the excel file is:")
print(df2.head())

# Cancatenate the DataFrames
df = pd.concat([df1, df2], ignore_index = True)

# Filter the DataFrame
# By passenger
df_pass_more = df[df['passenger_count'] > 4]
df_pass_less = df[df['passenger_count'] <= 4]

# By amount
df_amount_more = df[df['total_amount'] > 40]
df_amount_less = df[df['total_amount'] <= 40]

# By time tpep_pickup_datetime
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df_time_pm = df[df['tpep_pickup_datetime'].dt.strftime('%H:%M:%S') >= '12:00:00']
df_time_am = df[df['tpep_pickup_datetime'].dt.strftime('%H:%M:%S') < '12:00:00']

# Create csv files
df_pass_more.to_csv(output_pass_more_csv_file, index = False)
df_pass_less.to_csv(output_pass_less_csv_file, index = False)
df_amount_more.to_csv(output_amount_more_csv_file, index = False)
df_amount_less.to_csv(output_amount_less_csv_file, index = False)
df_time_pm.to_csv(output_time_pm_csv_file, index = False)
df_time_am.to_csv(output_time_am_csv_file, index = False)

# Create excel file with several sheets
with pd.ExcelWriter(output_excel_file) as writer:
    df_pass_more.to_excel(writer, sheet_name = output_sheet_pass_more4, index = False)
    df_pass_less.to_excel(writer, sheet_name = output_sheet_pass_less4, index = False)
    df_amount_more.to_excel(writer, sheet_name = output_sheet_amount_more40, index = False)
    df_amount_less.to_excel(writer, sheet_name = output_sheet_amount_less40, index = False)
    df_time_pm.to_excel(writer, sheet_name = output_sheet_time_pm, index = False)
    df_time_am.to_excel(writer, sheet_name = output_sheet_time_am, index = False)
