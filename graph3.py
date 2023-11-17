import main
import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.lmplot(data=main.df4, x="Date", y="Profitability ratio", col="State", hue="Product")
plt.show()
#print(main.df4.columns)