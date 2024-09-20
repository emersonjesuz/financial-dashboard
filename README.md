# Projeto de Otimização de Portfólio de Investimentos

Este projeto realiza a otimização de portfólio de ações utilizando dados históricos do Yahoo Finance. Ele coleta os dados, armazena-os em um banco de dados PostgreSQL, calcula os pesos ótimos para maximizar o retorno ajustado ao risco e gera visualizações gráficas do desempenho do portfólio.

## Objetivo

O objetivo deste projeto é fornecer uma ferramenta que auxilie investidores a otimizar a alocação de ativos no portfólio, maximizando o retorno e minimizando o risco, com base em dados históricos de preços de ações.

---

## Funcionalidades

1. **Coleta de Dados de Ações**: Usa a biblioteca `yfinance` para baixar os dados históricos de ações específicas.
2. **Armazenamento no Banco de Dados**: Salva os dados coletados em um banco de dados PostgreSQL.
3. **Otimização de Portfólio**: Calcula a melhor distribuição de pesos para maximizar o retorno ajustado ao risco.
4. **Visualização de Retornos**: Gera gráficos de desempenho do portfólio.

## Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Bibliotecas**:
  - `yfinance`: Coleta de dados de ações.
  - `SQLAlchemy`: Conexão com o banco de dados PostgreSQL.
  - `NumPy` e `SciPy`: Para cálculos de otimização.
  - `Pandas`: Manipulação de dados.
  - `Matplotlib`: Visualização de gráficos.
  - `Logging`: Para rastrear a execução e erros.

---

## Exemplo de Uso

### Entrada do usuário

Ao executar o script, o usuário será solicitado a inserir os tickers das ações e o intervalo de datas:

1.Digite os tickers das ações separados por vírgula (ex. AAPL, MSFT, GOOGL): AAPL, MSFT, GOOGL

2.Digite a data inicial no formato YYYY-MM-DD: 2023-01-01

3.Digite a data final no formato YYYY-MM-DD: 2023-12-31

## Saída Esperada

1.Pesos Otimizados para o Portfólio:

Pesos Otimizados: {'AAPL': 0.22207971, 'MSFT': 0.21523553, 'GOOGL': 0.56268475}

2.Visualização de Retornos (Gráfico):

O gráfico abaixo mostra os retornos cumulativos do portfólio com os pesos otimizados:

![image](https://github.com/user-attachments/assets/6f1e6ce3-de04-43b9-8901-38602ea6622f)

---

## Estrutura do Banco de Dados

Os dados coletados para cada ação serão salvos em tabelas separadas no banco de dados PostgreSQL. A estrutura das tabelas segue o padrão abaixo:

Exemplo de Tabela AAPL_data:

![image](https://github.com/user-attachments/assets/11aa76d0-ec44-42b1-82f7-cf08a88021ad)
