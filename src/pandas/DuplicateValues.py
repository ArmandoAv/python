import pandas as pd

# Create a DataFrame
data_duplicates = {
    'A': [1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 10, 10],
    'B': ['q','r','s','s','t','u','v','v','v','w','x','y','z','z']
}

df = pd.DataFrame(data_duplicates)
print("Original DataFrame:")
print(df)

# Detect and display duplicate rows
print("\nDataFrame with duplicate rows:")
df = df[df.duplicated()]
print(df)

# Eliminar filas duplicadas
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame without duplicate rows:")
print(df_no_duplicates)
