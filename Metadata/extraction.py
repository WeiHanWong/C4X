import pandas as pd


df = pd.read_csv('ippt.csv', delimiter=' ')
df.to_csv('ippt_run.csv', index=False)
print(df)