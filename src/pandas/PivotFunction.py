import pandas as pd

# Original DataFrame
data = {
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['Madrid', 'Barcelona', 'Madrid', 'Barcelona'],
    'Temperature': [14, 16, 12, 15],
    'Humidity': [60, 65, 55, 58]
}

load_file = "../../data/pivot_data.csv"

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

# Using pivot to rearrange the DataFrame
df_pivot = df.pivot(index='Date', columns='City', values=['Temperature', 'Humidity'])
print("\nDataFrame reorganizado con pivot:")
print(df_pivot)

# Upload to csv file
df_pivot.columns = df_pivot.columns = ['_'.join(col) for col in df_pivot.columns.values]
df_pivot.to_csv(load_file, index=True)
