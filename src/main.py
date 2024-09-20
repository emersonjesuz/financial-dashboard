import pandas as pd
from data_fetcher import fetch_stock_data
import sys
import os
from optimization import optimize_portfolio
from visualizations import plot_portfolio_returns
from logger import logger
# Adiciona o diretório do projeto ao caminho de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.db import save_to_db

def main():
    """
    Função principal que executa o fluxo do projeto: coleta de dados, otimização e visualização.
    """
    try:
        # Entrada do usuário
        tickers_input = input("Digite as ações separados por vírgula (ex. AAPL, MSFT, GOOGL): ")
        tickers = [ticker.strip() for ticker in tickers_input.split(',')]
        start_date = input("Digite a data inicial no formato YYYY-MM-DD: ")
        end_date = input("Digite a data final no formato YYYY-MM-DD: ")
        
        data = {}

        # Coleta de dados
        for ticker in tickers:
            logger.info(f"Coletando dados da ação {ticker}")
            df = fetch_stock_data(ticker, start_date, end_date)
            if df.empty:
                logger.warning(f"Sem dados para a ação {ticker}")
                continue
            data[ticker] = df
        
        # Salvando dados no banco de dados
        for ticker, df in data.items():
            if not df.empty:
                logger.info(f"Salvando dados da ação {ticker} no banco de dados")
                save_to_db(df, table_name=f"{ticker}_data")
        
        # Otimização de portfólio
        returns = pd.concat([df.set_index('timestamp')['Close'] for df in data.values()], axis=1)
        returns.columns = tickers
        returns = returns.pct_change().dropna()
        
        logger.info("Otimizando portfólio")
        weights = optimize_portfolio(returns)
        print(f"Pesos Otimizados: {weights}")
        
        # Visualização dos retornos
        logger.info("Gerando visualização dos retornos")
        plot_portfolio_returns(returns, tickers, start_date, end_date)
    
    except Exception as e:
        logger.error(f"Erro na execução do projeto: {e}")

if __name__ == "__main__":
    main()