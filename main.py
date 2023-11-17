import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('sales.csv')
df2 = df.loc[:, ('State', 'Market', 'Market Size', 'Profit', 'Margin', 'Sales', 'COGS', 'Total Expenses', 'Marketing', 'Inventory', 'Budget Profit', 'Budget COGS', 'Budget Margin', 'Budget Sales', 'Date', 'Product Type', 'Product')]
df2 = df2.rename(columns={'Market': 'Market location'})
df2 = df2.rename(columns={'Marketing': 'Marketing Expenses'})
groups = df2.groupby(by = 'State') #групування даних за штатами
df2loc = df2.loc[:, ['Date']]
df2grouped = df2loc.groupby(by = 'Date')
df2years = df2['Date'].replace(['01/01/10 00:00:00', '01/01/11 00:00:00', '02/01/10 00:00:00', '02/01/11 00:00:00', '03/01/10 00:00:00', '03/01/11 00:00:00', '04/01/10 00:00:00', '04/01/11 00:00:00', '05/01/10 00:00:00', '05/01/11 00:00:00', '06/01/10 00:00:00', '06/01/11 00:00:00', '07/01/10 00:00:00', '07/01/11 00:00:00', '08/01/10 00:00:00', '08/01/11 00:00:00', '09/01/10 00:00:00', '09/01/11 00:00:00', '10/01/10 00:00:00', '10/01/11 00:00:00', '11/01/10 00:00:00', '11/01/11 00:00:00', '12/01/10 00:00:00', '12/01/11 00:00:00'], ['10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11'])
df3 = df2.assign(Date=df2years)
df3years = df3.groupby(by = 'Date')
groups2 = df2.groupby(by = 'Market location')
groups3 = df2.groupby(by = 'State')

df4 = df2.copy(deep=True)
df4.pe = df2['Profit']/df2['Sales']
df4['Profitability ratio'] = df4.pe

df4date = df4.Date.replace({'00:00:00':''}, regex=True)
df4 = df4.assign(Date=df4date)
ddf = df4.Date.replace({'/01/':'.'}, regex=True)
df4 = df4.assign(Date=ddf)
df4['Date'] = df4['Date'].astype(float) #Переводимо дату у формат float

df2expenses1 = df2.loc[:, ['State', 'Sales', 'COGS', 'Total Expenses']]
df2expenses1['All Expenses'] = df2expenses1['COGS'].values + df2expenses1['Total Expenses'].values#суцільні витрати на виробництво і продаж продукту

df2expenses2 = df2.loc[:, ['State', 'Sales', 'COGS', 'Total Expenses']]
df2expenses2['Sales'] = df2['Sales'].copy(deep=True)
df2expenses2['Profitability'] = df2expenses2['Sales'].values/df2expenses1['All Expenses'].values#профітабільність

df2expenses3 = df2.loc[:, ['State', 'Sales', 'COGS', 'Total Expenses', 'Profit']]
df2expenses3['Sales'] = df2['Sales'].copy(deep=True)
df2expenses3['Profitability ratio'] = df2expenses3['Profit'].values/df2expenses3['Sales'].values#для графіку профіт/сейлс(норма додаткової вартості)
