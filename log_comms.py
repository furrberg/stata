import main
import time as t #для маніпуляцій з датами
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(main.df.shape)
print(main.df.tail())
print(main.df.dtypes)

print(main.df2.head()) #Видаляємо непотрібні для аналізу стовпці, щоб легше було орієнтуватися (видалиено:'Area Code', 'ProductId','Type') і перейменовуємо стовпеці
main.df2.describe() #для п'ятого пункту
main.groups.sum(numeric_only = True) #сума значень змінних у різних штатах
main.df2grouped.count() #групуємо дати, щоб витягнути з них роки

print(main.df3) #витагуємо з дат роки

main.df3years.sum(numeric_only = True) #сумарні показники у всіх магазинах разом в 2010 та 2011 роках
main.df2.corr(numeric_only = True)

main.groups2.sum(numeric_only=True)

main.groups3['Profit'].mean()

print(main.df4)
