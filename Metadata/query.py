import pandas as pd

df = pd.read_csv('ippt_situp.csv')

print(df[df['Rep'] == 60]['1'])