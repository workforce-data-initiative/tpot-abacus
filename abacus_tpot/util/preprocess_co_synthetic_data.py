#!/usr/bin/env python
import pandas as pd

df = pd.read_csv('UI_synthetic_data.csv')
df = df[['ID', 'Year', 'q1', 'q2', 'q3', 'q4']]
df = df.rename(columns={
               'q1': 'q1_wage',
               'q2': 'q2_wage',
               'q3': 'q3_wage',
               'q4': 'q4_wage',
               'ID': 'id',
               'Year': 'year'})

df.to_csv('colorado_ui_wage.csv', index=False)
