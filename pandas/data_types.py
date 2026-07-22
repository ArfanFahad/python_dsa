# Name      Age     Salary
# Alice      25      50000
# Bob        30      60000
# Charlie    35      70000

import pandas as pd 

sales = pd.Series(
    [230, 440, 100],
    index=["Sun", "Mon", "Tue"]
)

print(sales)

print("---------------------------------")

print("Best Sales amount: ", sales.max())
print("Worst Sales amount: ", sales.min())
print("Average Sales amount: ", sales.mean())

print("Monday sales: ", sales["Mon"])