import main as main
import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.relplot(
    data=main.df2, kind="line",
    x="Sales", y="Total Expenses", col="Market location",
    hue="Market Size", style="Market Size",
)
sns.barplot(main.df2.loc[:, ['State', 'Profit']], x="State", y="Profit", width=0.6)
plt.xticks(rotation=90)
plt.show()