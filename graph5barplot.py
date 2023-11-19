import main
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(main.df2expenses1.loc[:, ['State', 'All Expenses']], x="State", y="All Expenses", width=0.6)
plt.xticks(rotation=90)
plt.show()#порівння за середніми суцільними витратами кожного магазину в штаті

sns.barplot(main.df2expenses2.loc[:, ['State', 'Profitability']], x="State", y="Profitability", width=0.6)
plt.xticks(rotation=90)
plt.show()#порівняння за середньою прибутковістю кожного магазину в штаті

sns.barplot(main.df2expenses3.loc[:, ['State', 'Profitability ratio']], x="State", y="Profitability ratio", width=0.6)
plt.xticks(rotation=90)
plt.show()#порівняння за нормою доодаткової вартості(яку частку продажів склав прибуток) кожного магазину в штаті

sns.barplot(main.product.loc[:, ['Product', 'Sales']], x="Product", y="Sales", width=0.6)
plt.xticks(rotation=90)
plt.show()#порівняння за середніми продажами продуктів у кожному магазині в усіх штатах

sns.barplot(main.df2expenses3.loc[:, ['State', 'Profit']], x="State", y="Profit", width=0.6)
plt.xticks(rotation=90)
plt.show()#порівняння за середнім прибутком кожного магазину в штаті

