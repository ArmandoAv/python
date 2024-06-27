import pandas as pd

# Original DataFrame
data = {
    'Date': ['2023-01-01', '2023-01-02'],
    'Barcelona_Temperature': [16, 15],
    'Barcelona_Humidity': [65, 58],
    'Madrid_Temperature': [14, 12],
    'Madrid_Humidity': [60, 55]
}
load_file = "../../data/melt_data.csv"

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Using melt to rearrange the DataFrame
df_melt = df.melt(id_vars='Date', 
                       var_name='City_Variable', 
                       value_name='Value')
print("\nDataFrame transformado a formato largo con melt:")
print(df_melt)

df_melt.to_csv(load_file, index=False)
