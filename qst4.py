import pandas as pd
dr = pd.read_csv('sales_data.csv')
df = pd.DataFrame(dr, index=None)
rows = len(df.axes[0])
cols = len(df.axes[1])
print("DataFrame")
print(df)
print("Number of Rows: ", rows)
print("Number of Columns: ", cols)

print("Sum of Revenue",df['Revenue'].sum())