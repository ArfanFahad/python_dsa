import pandas as pd 


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_excel('Roster.xlsx', header=1)

print(df.to_markdown())