import pandas as pd

# Create a DataFrame
data = {
    'Parcel': ['A', 'B', 'C', 'D'],
    'Lenght': [10, 15, 12, 8],
    'Width': [5, 7, 6, 4]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# Vectorized function to calculated the area
def calcular_area(longitud, ancho):
    return longitud * ancho

# Apply the vectorized function
df['Area'] = calcular_area(df['Lenght'], df['Width'])

print("\nDataFrame with the parcel area:")
print(df)
