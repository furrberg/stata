import main
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.heatmap(main.df2.corr(numeric_only = True), cmap="YlGnBu", annot=True)#візуалізація кореляції
plt.xticks(rotation=90)
plt.show()