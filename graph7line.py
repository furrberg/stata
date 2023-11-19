import main
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
fig = px.line(main.dflinegrouped2, x='Date', y='Total Sales')
fig.show()#лінійний графік для порівння за датами загального прибутку по усім штатм разом