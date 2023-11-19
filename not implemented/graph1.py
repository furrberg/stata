import main
import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset1 = main.df2[main.df2['Market location'] == 'Central']
dataset2 = main.df2[main.df2['Market location'] == 'East']
dataset3 = main.df2[main.df2['Market location'] == 'South']
dataset4 = main.df2[main.df2['Market location'] == 'West']
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