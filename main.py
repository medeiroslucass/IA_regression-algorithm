import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression

# TRATANDO DADOS
csv = pd.read_csv('dados.csv', sep=";")
# csv = csv.drop(columns=["Número comentários", "Compartilhamento"])

# Convertendo para numero
le = LabelEncoder()
csv["Tipo"] = le.fit_transform(csv["Tipo"])


# Separando dados de entrada e saida
dados = csv.values
entradas = dados[:,0:5]
saida = dados[:,5:]

# Treinamento
modelo = LinearRegression()
modelo.fit(entradas , saida)

#predizao
tipo = int(input('Informe o numero do tipo da postagem: Foto[0] Link[1] Status[2] Video[3] \n'))
mes = int(input('Mes: (1 a 12) \n'))
semana = int(input('Dia da Semana: Dom[1] Seg[2] Ter[3] Qua[4] Qui[5] Sex[6] Sab[7] \n'))
hora = int(input('Hora: \n'))
pago = int(input('Postagem Paga: [1]Sim [0]Nao \n'))



resultado = modelo.predict([[tipo, mes, semana, hora, pago]])

# print(resultado[0][1])
print(f"media de comentarios {int(resultado[0][0])}, media de likes {int(resultado[0][1])}, media de compartilhamento {int(resultado[0][2])}")

