import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
    'Age': [28, 25, 32, 21, 29],
    'Gross_Salary': [30000, 35000, 48000, 30000, 32000],
    'Income_tax' : [0.15, 0.15, 0.15, 0.15, 0.15]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Add new column with arithmetic operations
df['Salary'] = df['Gross_Salary'] - df['Gross_Salary'] * df['Income_tax']  # Suponiendo salario mensual, calculamos salario anual
print("\nDataFrame with add column: 'Salary':")
print(df)

# Add new column with logic operation
df['High_salary'] = df['Gross_Salary'] >= 35000
print("\nDataFrame with add column 'High_salary':")
print(df)
