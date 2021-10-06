#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python
# 
# ### Desafio:
# 
# Você trabalha em uma empresa de telecom e tem clientes de vários serviços diferentes, entre os principais: internet e telefone.
# 
# O problema é que, analisando o histórico dos clientes dos últimos anos, você percebeu que a empresa está com Churn de mais de 26% dos clientes.
# 
# Isso representa uma perda de milhões para a empresa.
# 
# O que a empresa precisa fazer para resolver isso?
# 
# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing <br>
# Link Original do Kaggle: https://www.kaggle.com/radmirzosimov/telecom-users-dataset

# In[2]:


# Passo 1: Importar base de dados
import pandas as pd

tabela = pd.read_csv('telecom_users.csv')

# Passo 2: Visualizar os dados
# → Entender as informacoes disponíveis
# → Descobrir os problemas da base de dados
tabela = tabela.drop('Unnamed: 0', axis=1) #o que será dropado(apagado) e se o axis é linha(0) ou coluna(1)
display(tabela)


# In[6]:


# Passo 3: Tratamento dos dados

# --→ print(tabela.info())

# → Valores reconhecidos de forma errada
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# → Valores vazios
# 1° deletando as colunas vazias
tabela = tabela.dropna(how='all', axis=1) ##o que será deletado(all → todos | any → algum valor vazio) e se o axis é linha(0) ou coluna(1)

# 2° deletando as linhas vazias
tabela = tabela.dropna(how='any', axis=0)

print(tabela.info())


# In[12]:


# Passo 4: Análise Básica Inicial
# → Como estao os nossos cancelamentos?
display(tabela['Churn'].value_counts()) # números completos da tabela, int
display(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format)) # Porcentagem 


# In[14]:


get_ipython().system('pip install plotly')


# In[21]:


# Passo 5: Análise Completa
# Comparar cada coluna da tabela com a coluna de cancelamento

import plotly.express as px

tabela = tabela.drop('IDCliente', axis=1) # um gráfico sem importancia alguma para analise.
# etapa 1: Criar o gŕafico
for coluna in tabela.columns:
    print(coluna)
    grafico= px.histogram(tabela, x=coluna, color='Churn')
    # etapa 2: Exibir o gráfico
    grafico.show()


# ### Conclusões e Ações

# Escreva aqui suas conclusões:
# 
# - Clientes com contrato mensal tem MUITO mais chance de cancelar:
#     - Podemos fazer promoções para o cliente ir para o contrato anual.
#     
# - Familias maiores tendem a cancelar menos do que famílias menores.
#     - Podemos fazer promoções pra pessoa pegar uma linha adicional de telefone.
#     
# - MesesComoCliente baixos tem MUITO cancelamento. Clientes com pouco tempo como cliente tendem a cancelar muito.
#     - A primeira experiência do cliente na operadora pode ser ruim;
#     - Talvez a captação de clientes está trazendo clientes desqualificados;
#     - Ideia: podemos criar incentivos para ficarem mais tempo como cliente.
#     
# - Quanto mais serviços a pessoa tem, menor a chance de cancelamento.
#     - podemos fazer promoções com mais serviços pro cliente.
#     
# - Tem alguma coisa no nosso serviço de Fibra que está fazendo os clientes cancelarem.
#     - Agir sobre a fibra.
#     
# - Clientes no boleto tem MUITO mais chance de cancelar, então temos que fazer alguma ação para eles irem para as outras formas de pagamento.

# In[ ]:




