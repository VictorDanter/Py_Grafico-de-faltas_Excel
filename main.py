import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

url = 'dados.xlsx'
df = pd.read_excel(url)
print(df.head(50))


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregue os dados do arquivo 'dados.xlsx'
df = pd.read_excel('dados.xlsx')

# Defina as cores para 'Falta' e 'Presente' (vermelho e amarelo)
cores_ray = {'Falta': 'red', 'Presente': 'yellow'}
cores_amilton = {'Falta': 'red', 'Presente': 'yellow'}
cores_matheus = {'Falta': 'red', 'Presente': 'yellow'}
cores_wderlan = {'Falta': 'red', 'Presente': 'yellow'}
cores_edmilson = {'Falta': 'red', 'Presente': 'yellow'}

# Remova 'DISPENSADO' e 'FOLGA' do DataFrame para cada pessoa
df_ray = df[df['L'].isin(['Falta', 'Presente'])]
df_amilton = df[df['V'].isin(['Falta', 'Presente'])]
df_matheus = df[df['Lin'].isin(['Falta', 'Presente'])]
df_wderlan = df[df['T'].isin(['Falta', 'Presente'])]
df_edmilson = df[df['IS'].isin(['Falta', 'Presente'])]

# Calcular as ocorrências de 'Falta' e 'Presente' para cada pessoa
contagem_ray = df_ray['L'].value_counts()
contagem_amilton = df_amilton['V'].value_counts()
contagem_matheus = df_matheus['Lin'].value_counts()
contagem_wderlan = df_wderlan['T'].value_counts()
contagem_edmilson = df_edmilson['IS'].value_counts()

# Criar gráficos de barras para cada pessoa
plt.figure(figsize=(30, 6))

plt.subplot(1, 5, 1)  # Gráfico para L
ax_ray = sns.barplot(x=contagem_ray.index, y=contagem_ray, palette=cores_ray)
for p in ax_ray.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax_ray.annotate(f"{int(height)}", (x + width/2, height), ha='center', fontsize=12, color='black')

plt.subplot(1, 5, 2)  # Gráfico para V
ax_amilton = sns.barplot(x=contagem_amilton.index, y=contagem_amilton, palette=cores_amilton, order=['Presente', 'Falta'])
for p in ax_amilton.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax_amilton.annotate(f"{int(height)}", (x + width/2, height), ha='center', fontsize=12, color='black')

plt.subplot(1, 5, 3)  # Gráfico para Lin
ax_matheus = sns.barplot(x=contagem_matheus.index, y=contagem_matheus, palette=cores_matheus, order=['Presente', 'Falta'])
for p in ax_matheus.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax_matheus.annotate(f"{int(height)}", (x + width/2, height), ha='center', fontsize=12, color='black')

plt.subplot(1, 5, 4)  # Gráfico para T
ax_wderlan = sns.barplot(x=contagem_wderlan.index, y=contagem_wderlan, palette=cores_wderlan, order=['Presente', 'Falta'])
for p in ax_wderlan.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax_wderlan.annotate(f"{int(height)}", (x + width/2, height), ha='center', fontsize=12, color='black')

plt.subplot(1, 5, 5)  # Gráfico para IS
ax_edmilson = sns.barplot(x=contagem_edmilson.index, y=contagem_edmilson, palette=cores_edmilson, order=['Presente', 'Falta'])
for p in ax_edmilson.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    ax_edmilson.annotate(f"{int(height)}", (x + width/2, height), ha='center', fontsize=12, color='black')

plt.tight_layout()
plt.show()
