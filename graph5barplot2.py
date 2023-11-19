import main
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x="State", y="Profit", data=main.df2expenses3, estimator=sum)
plt.xticks(rotation=90)
plt.show()#порівння штатів за сумарним прибутком усіх магазинів в штаті 

sns.barplot(x="State", y="All Expenses", data=main.df2expenses1, estimator=sum)
plt.xticks(rotation=90)
plt.show()#порівння штатів за сумарними суцільними витратми усіх магазнів в штаті

sns.barplot(x="State", y="Profitability ratio", data=main.df2expenses3, estimator=sum)
plt.xticks(rotation=90)
plt.show()#порівння штатів за сумарною нормою додаткової вартості(яку частку продажів склав прибуток) усіх магазинів в штаті

sns.barplot(x="Product", y="Sales", data=main.product, estimator=sum)
plt.xticks(rotation=90)
plt.show()#порівння продуктів за їх сумарними продажами в усіх магазинах в усіх штатах

sns.barplot(x="State", y="Sales", data=main.df2expenses3, estimator=sum)
plt.xticks(rotation=90)
plt.show()#порівння штатів за сумарними продажами у всіх магазинах в штаті
