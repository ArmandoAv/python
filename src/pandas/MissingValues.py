import pandas as pd
import numpy as np

# Create a DataFrame
data = {
    'A': [1, 2, np.nan, 3],
    'B': [5, np.nan, np.nan, 8],
    'C': ['available', 'available', np.nan, 'available'],
    'D': [10, 5, 7, 16]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Detectar valores faltantes
print("\nDetect missing values:")
print(df.isnull())

# Contar valores faltantes por columna
print("\nCount missing values ​​per column:")
print(df.isnull().sum())

# Drop rows with missing values
df_dropna = df.dropna()
print("\nDataFrame with rows without NaN:")
print(df_dropna)

# Get DataFrame with rows containing NaN values in any column
df_with_nan = df[df.isna().any(axis=1)].reset_index(drop=True)
print("\nDataFrame with rows with NaN:")
print(df_with_nan)

# Fill missing values with specific values
df_fillna = df.fillna(value={'A': df['A'].mean(), 'B': 0, 'C': 'Not available'})
print("\nDataFrame after filling NaN with specific values:")
print(df_fillna)
