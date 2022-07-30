#Passo 1: Importar a base de dados;
#Passo 2: Visualizar a base de dados;
#Passo 3: Tratamento de dados (resolver as cagadas da base de dados);
#Passo 4: Análise Inicial dos dados (confirmar se realmente é 26% dos clientes)
#Passo 5: Descobrir motivos do cancelamento
    #Etapas para construir gráficos em py
    #etapa 1: Cria o gráfico
    #etapa 2: Exibe o gráfico

#Passo 1: Importar a base de dados;
import pandas as pd
import plotly.express as px #Gráficos em py

tabela = pd.read_csv('C:/Users/Funari/Documents/GitHub/AnaliseDados/telecom_users.csv')

#Passo 2: Visualizar a base de dados;
#Excluir coluna inutil
#axis = 0 Quando for Linha
#axis = 1 Quando for coluna
tabela = tabela.drop('Unnamed: 0', axis=1 ) #nome da coluna a ser tirada e o eixo da coluna a ser tirado.

#Passo 3: Tratamento de dados (resolver as cagadas da base de dados);
#Informação do tipo correto - ajusar o TotalGasto

#Seleciona uma coluna
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce') #Transforma a coluna TotalGasto em númerico.
#errors='coerce' força o valor a ficar númerico, ou seja, deixa como 0 (ou vazio)

#Informações vazias
#Colunas completamente vazias
tabela = tabela.dropna(how='all',axis=1) #dropna joga fora valores vazios / all=exclui completamente vazias  
#Linhas com valor vazio
tabela = tabela.dropna(how='any',axis=0) #any=exclui se há algum valor vazio exclui a linha toda.

print (tabela.info())#Resumo da base de dado

#Passo 4: Análise Inicial
#Como estão oos cancelamentos dos clientes
#Cancelamentos = a Coluna 'Churn' 'Sim' = Cancelaram 'Não' = Não cancelaram

print (tabela['Churn'].value_counts()) #Contando valores da coluna.

#Normalize = true mostra a porcentagem
print ((tabela['Churn'].value_counts(normalize=True)).map('{:.1%}'.format))#.map formata com 1 casa após a virgula e transform em porcentagem
  
#Passo 5: Descobrir os motivos

for coluna in tabela.columns:#Cria um gráfico para cada coluna na tabela
    #Criar gráfico
    grafico = px.histogram(tabela, x=coluna, color='Churn', text_auto=True)#x igual a coluna, color (valor passado para "comparar")
    grafico.update_layout(bargap=0.2) #Customização da barra  
    
    #Exibe gráfico
    grafico.show()
