import main.py as main
dataset1 = main.df2[df2['Market location'] == 'Central']
dataset2 = main.df2[df2['Market location'] == 'East']
dataset3 = main.df2[df2['Market location'] == 'South']
dataset4 = main.df2[df2['Market location'] == 'West']
main.fig, main.axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 10))
datasets = [dataset1, dataset2, dataset3, dataset4]
labels = ['Central', 'East', 'South', 'West']
for i, ax in enumerate(axes.flatten()):
 data = datasets[i]
 ax.scatter(data['Sales'], data['Budget Sales'], label=labels[i])
 ax.set_title(labels[i])
 ax.set_xlabel('Sales')
 ax.set_ylabel('Budget Sales')
 #ax.legend()
main.plt.tight_layout()
main.plt.show()