import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('contrato_item.xlsx')

#print(df.head(5))
#print(df.info())

top_10_fornecedores = df.groupby('NMCONTRATADO')['VLTOTALATUAL'].sum().sort_values(ascending=False).head(10)

top_10_itens = df.groupby('DEDESCRICAO')['VLINFORMADO'].sum().sort_values(ascending=False).head(10)

print(top_10_fornecedores)

print(top_10_itens)



plt.figure(figsize=(12, 8))
top_10_fornecedores.plot(kind='barh')
plt.title('Top 10 Fornecedores por Valor Total em Contratos')
plt.xlabel('Valor Total (R$)')
plt.ylabel('Fornecedor')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('analise_contratos_covid_fornecedores.png')
print("Gráfico salvo com sucesso!")

plt.figure(figsize=(20, 20))
top_10_itens.plot(kind='barh')
plt.title('Top 10 Itens por Valor Total em Contratos')
plt.xlabel('Valor Total (R$)')
plt.ylabel('ITEM')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('analise_contratos_covid_itens.png')
print("Gráfico salvo com sucesso!")
