import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
# Ex.: 01.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x, y)
plt.show()
'''

'''
# Ex.: 02.
x = np.arange(0, 1000, 1)
plt.plot(x, x ** 2)
plt.show()
'''


# Ex.: 03.
dados = pd.read_csv('athlete_events.csv')
# print(dados)
masculino = dados.loc[dados['Sex'] == 'M']
# print(masculino)
a = masculino['Height']
p = masculino['Weight']
plt.scatter(a, p)
plt.show()
