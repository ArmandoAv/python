import pandas as pd

# Create DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Current list of columns
columns = df.columns.tolist()

# New column
new_column = 'D'

# Insert colummn D after column B
position = columns.index('B') + 1
columns.insert(position, new_column)

# Reorder DataFrame with the new column
df = df.reindex(columns=columns)

# Insert values into the new column
df['D'] = [10, 11, 12]

print(df)
