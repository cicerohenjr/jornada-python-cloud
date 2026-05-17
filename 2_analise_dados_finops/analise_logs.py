import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.dropna() 
tabela = tabela[tabela["duracao_contrato"] != "Monthly"] 

grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou")
grafico.show()
