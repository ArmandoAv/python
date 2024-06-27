import pandas as pd

input_file = '../../data/uber_data.json'
output_file = '../../data/uber_data.csv'

with open(input_file) as f:
    data = pd.read_json(f, lines = True)

data.to_csv(output_file, index = False)
df = pd.DataFrame(data)

print("The file has been converted from json to csv")

# Print the first rows of the DataFrame
print(df.head)

# Print info of the DataFrame
print(df.info())

# Print the columns of the DataFrame
print(df.columns)
