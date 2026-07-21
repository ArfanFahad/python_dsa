# Name      Age     Salary
# Alice      25      50000
# Bob        30      60000
# Charlie    35      70000

import pandas as pd 

df = pd.DataFrame({
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 50],
    "Salary": [50000, 60000, 70000],
    "Designation": ['Sr. Executive ', 'Manager', 'Executive Director'],
    "Bonus": [2000, 4000, 5000]
})

print(df)
print("-------------------")
print(df[df["Age"] < 50])