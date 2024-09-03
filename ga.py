import pandas as pd

df = pd.read_excel("GA_task.xlsx")

for i in range(len(df)):
    if i == 0 or i % 2 == 0:
        print(df.iloc[i, ::2])