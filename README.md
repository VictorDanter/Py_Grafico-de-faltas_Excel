# Py_Grafico-de-faltas_Excel

Este script em Python usa dados armazenados em um arquivo Excel para mostrar visualmente as presenças e faltas de diferentes pessoas. Aqui está uma explicação simples do que cada parte do script faz:

1. **Leitura dos Dados:**
   - O script começa lendo informações de um arquivo Excel chamado 'dados.xlsx' usando uma ferramenta chamada pandas. As informações são organizadas em uma tabela chamada DataFrame.

2. **Definição de Cores:**
   - São escolhidas cores (vermelho para falta e amarelo para presente) para representar visualmente as situações de falta e presença para cada pessoa.

3. **Filtragem de Dados:**
   - O script remove informações irrelevantes, como 'DISPENSADO' e 'FOLGA', mantendo apenas as situações de 'Falta' e 'Presente' para cada pessoa.

4. **Contagem de Ocorrências:**
   - Para cada pessoa, o script conta quantas vezes ocorreu 'Falta' e 'Presente'.

5. **Visualização com Gráficos de Barras:**
   - O script cria gráficos de barras simples para representar visualmente as contagens. Cada pessoa tem seu próprio gráfico, onde as barras vermelhas e amarelas mostram as faltas e presenças, respectivamente.
   - As anotações nos gráficos indicam o número exato de faltas ou presenças.

6. **Ajustes de Layout e Exibição:**
   - Pequenos ajustes são feitos para garantir que os gráficos sejam exibidos de maneira organizada e legível.
   - Finalmente, os gráficos são mostrados na tela.

Em resumo, este script ajuda a entender, de forma simples e visual, como a presença e a falta variam para diferentes pessoas com base nos dados fornecidos em um arquivo Excel.
