import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_portfolio_returns(returns: pd.DataFrame, tickers: list, start_date: str, end_date: str):
    """
    Função para plotar os retornos do portfólio e salvar a imagem na pasta 'img'.
    
    Parâmetros:
        returns (pd.DataFrame): DataFrame com os retornos dos ativos.
        tickers (list): Lista de tickers das ações.
        start_date (str): Data inicial no formato "YYYY-MM-DD".
        end_date (str): Data final no formato "YYYY-MM-DD".
    """
    try:
        plt.figure(figsize=(12, 6))
        for ticker in tickers:
            if ticker in returns.columns:
                plt.plot(returns.index, returns[ticker], label=ticker)
        
        plt.title(f'Retorno do Portfólio de Ações ({start_date} a {end_date})')
        plt.xlabel('Data')
        plt.ylabel('Retorno Diário')
        plt.legend()
        plt.grid(True)

        # Criando o nome do arquivo com base nas ações e datas
        filename = f'portfolio_returns_{"_".join(tickers)}_{start_date}_to_{end_date}.png'
        
        # Verificando se a pasta 'img' existe, senão cria
        if not os.path.exists('img'):
            os.mkdir('img')
        
        # Salvando o arquivo na pasta 'img'
        filepath = os.path.join('img', filename)
        plt.savefig(filepath)

        # Mostrar o gráfico na tela
        plt.show()
    

        

        print(f"Gráfico salvo como {filepath}")
    except Exception as e:
        print(f"Erro ao gerar gráfico: {e}")