import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('sales.csv')
print(df.shape)
print(df.tail())
print(df.dtypes)
df2 = df.loc[:, ('State', 'Market', 'Market Size', 'Profit', 'Margin', 'Sales', 'COGS', 'Total Expenses', 'Marketing', 'Inventory', 'Budget Profit', 'Budget COGS', 'Budget Margin', 'Budget Sales', 'Date', 'Product Type', 'Product')]
df2 = df2.rename(columns={'Market': 'Market location'})
df2 = df2.rename(columns={'Marketing': 'Marketing Expenses'})
print(df2.head()) #Видаляємо непотрібні для аналізу стовпці, щоб легше було орієнтуватися (видалиено:'Area Code', 'ProductId','Type') і перейменовуємо стовпеці
df2.describe() #для п'ятого пункту
groups = df2.groupby(by = 'State') #групування даних за штатами
groups.sum(numeric_only = True) #сума значень змінних у різних штатах
df2loc = df2.loc[:, ['Date']]
df2grouped = df2loc.groupby(by = 'Date')
df2grouped.count() #групуємо дати, щоб витягнути з них роки
df2years = df2['Date'].replace(['01/01/10 00:00:00', '01/01/11 00:00:00', '02/01/10 00:00:00', '02/01/11 00:00:00', '03/01/10 00:00:00', '03/01/11 00:00:00', '04/01/10 00:00:00', '04/01/11 00:00:00', '05/01/10 00:00:00', '05/01/11 00:00:00', '06/01/10 00:00:00', '06/01/11 00:00:00', '07/01/10 00:00:00', '07/01/11 00:00:00', '08/01/10 00:00:00', '08/01/11 00:00:00', '09/01/10 00:00:00', '09/01/11 00:00:00', '10/01/10 00:00:00', '10/01/11 00:00:00', '11/01/10 00:00:00', '11/01/11 00:00:00', '12/01/10 00:00:00', '12/01/11 00:00:00'], ['10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11', '10', '11'])
df3 = df2.assign(Date=df2years)
df3 #витагуємо з дат роки
df3years = df3.groupby(by = 'Date')
df3years.sum(numeric_only = True) #сумарні показники у всіх магазинах разом в 2010 та 2011 роках
df2.corr(numeric_only = True)
groups2 = df2.groupby(by = 'Market location')
groups2.sum(numeric_only=True)
groups3 = df2.groupby(by = 'State')
groups3['Profit'].mean()
dataset1 = df2[df2['Market location'] == 'Central']
dataset2 = df2[df2['Market location'] == 'East']
dataset3 = df2[df2['Market location'] == 'South']
dataset4 = df2[df2['Market location'] == 'West']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
datasets = [dataset1, dataset2, dataset3, dataset4]
labels = ['Central', 'East', 'South', 'West']
for i, ax in enumerate(axes.flatten()):
 data = datasets[i]
 ax.scatter(data['Sales'], data['Budget Sales'], label=labels[i])
 ax.set_title(labels[i])
 ax.set_xlabel('Sales')
 ax.set_ylabel('Budget Sales')
 #ax.legend()
plt.tight_layout()
plt.show()
sns.relplot(
    data=df2, kind="line",
    x="Sales", y="Total Expenses", col="Market location",
    hue="Market Size", style="Market Size",
)
sns.barplot(df2.loc[:, ['State', 'Profit']], x="State", y="Profit", width=0.6)
plt.xticks(rotation=90)
plt.show()
sns.barplot(df2.loc[:, ['State', 'Profit']], x="State", y="Profit", width=0.6)
plt.xticks(rotation=90)
plt.show()
df4 = df2.copy(deep=True)
df4.pe = df2['Profit']/df2['Sales']
df4['Profitability ratio'] = df4.pe
df4
df4['Date'] = df4['Date'].astype(str)
df4date = df4.Date.replace({'00:00:00':''}, regex=True)
df4 = df4.assign(Date=df4date)
ddf = df4.Date.replace({'/':'.'}, regex=True)
df4 = df4.assign(Date=ddf)
df4