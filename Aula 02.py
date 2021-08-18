import pandas as pd

'''
# Ex.: 01.
dados = pd.read_csv('athlete_events.csv')
# print(dados)

dados2 = dados.dropna()
# print(dados2)
'''
'''
# Ex.: 02.
dados = pd.read_csv('athlete_events.csv')
enulo = dados.isnull()
# True significa dados faltantes.
print(enulo)
'''

# Ex.: 02.
dados = pd.read_csv('athlete_events.csv')
# Para somar todos os dados faltantes.
faltantes = dados.isnull().sum()
# print(faltantes)
# Para ver a porcentagem.
# faltantes_percentual = (dados.isnull().sum() / len(dados['ID'])) * 100.
# print(faltantes_percentual)
# Para substituir o 'NaN' por 'Nenhuma' e permanecer na mesma linha.
dados['Medal'].fillna('Nenhuma', inplace=True)
# Para substituir a idade, altura e peso faltante pela media de todas as outras.
dados['Age'].fillna(dados['Age'].mean(), inplace=True)
dados['Height'].fillna(dados['Height'].mean(), inplace=True)
dados['Weight'].fillna(dados['Weight'].mean(), inplace=True)
# print(dados)
faltantes_percentual = (dados.isnull().sum() / len(dados['ID'])) * 100
print(faltantes_percentual)
