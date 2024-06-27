import pandas as pd

# Create a DataFrame
data = {
    'CIty': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'Celsius': [25, 28, 30, 22, 26]
}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

# Function to convert from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Apply the map function to convert the temperature
df['Fahrenheit'] = df['Celsius'].map(lambda x: celsius_to_fahrenheit(x))

print("\nDataFrame with degrees Fahrenheit:")
print(df)
