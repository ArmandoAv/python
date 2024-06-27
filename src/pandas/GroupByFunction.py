import pandas as pd

# Create a DataFrame
data = {
    'City': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao', 'Madrid', 'Barcelona', 'Madrid', 'Valencia'],
    'Country': ['España', 'España', 'España', 'España', 'España', 'España', 'España', 'España', 'España'],
    'Sales': [1000, 1500, 800, 1200, 900, 1300, 1100, 950, 1150],
    'Price': [20, 25, 18, 22, 21, 23, 24, 21, 20]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Group by City
df_city = df.groupby('City').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Price=('Price', 'mean'),
    Min_Price=('Price', 'min'),
    Max_Price=('Price', 'max')
).reset_index()

print("\nDataFrame grouped by City:")
print(df_city)

# Group by City
df_country = df.groupby('Country').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Price=('Price', 'mean'),
    Min_Price=('Price', 'min'),
    Max_Price=('Price', 'max')
).reset_index()

print("\nDataFrame grouped by Country:")
print(df_country)
