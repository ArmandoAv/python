import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
    'Age': [28, 25, 32, 21, 29],
    'City': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Add a column
df['Country'] = ['España', 'España', 'España', 'España', 'España']
print("\nDataFreame with new column: 'Country':")
print(df)

# Add a calculated column
df['Double_Age'] = df['Age'] * 2
print("\nDataFrame with calculated column: 'Double_Age':")
print(df)

# Add a new row
new_row = {'Name': 'Ana', 'Age': 21, 'City': 'Valencia', 'Country' : 'España', 'Double_Age' : 42 }
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("\nDataFrame con una nueva fila añadida:")
print(df)

# Modify values in a row (third row)
df.loc[2, 'Age'] = 29
print("\nDataFrame with modified value in row 3 (Age):")
print(df)

# Axis helps you know if you want to modify a column (axis = 1) or a row (axis = 0)
# Drop a column
df_without_country = df.drop('Country', axis=1)
print("\nDataFrame without column: 'Country':")
print(df_without_country)

# Drop a row
df_without_row = df.drop(3, axis=0)
print("\nDataFrame without third row: 'Name': Ana")
print(df_without_row)
