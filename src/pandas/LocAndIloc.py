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

# Select with loc an iloc
print("\nSelect with loc (row with index 2):")
print(df.loc[2])

print("\nSelect with iloc (second row):")
print(df.iloc[1])

print("\nSelect with loc (rows 0 y 2, columns 'Name' y 'Age'):")
print(df.loc[[0, 2], ['Name', 'Age']])

print("\nSelect with iloc (first two rows, first two columns):")
print(df.iloc[:2, :2])

# Ejemplos de indexación booleana
print("\nfilter with boolean indexing (Age > 25):")
print(df[df['Age'] > 25])

print("\nCombine filter (Age > 25 y City 'Madrid'):")
print(df[(df['Age'] > 25) & (df['City'] == 'Madrid')])
