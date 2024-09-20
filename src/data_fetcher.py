import yfinance as yf
import pandas as pd
from logger import logger

def fetch_stock_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Função que busca os dados históricos de uma ação usando a API do Yahoo Finance.
    
    Parâmetros:
        symbol (str): Código da ação (ex. "AAPL").
        start_date (str): Data inicial no formato "YYYY-MM-DD".
        end_date (str): Data final no formato "YYYY-MM-DD".
    
    Retorna:
        pd.DataFrame: Dados históricos da ação com colunas de preço e volume.
    """
    try:
        data = yf.download(symbol, start=start_date, end=end_date, interval='1d')
        
        if data.empty:
            raise Exception(f"Sem dados disponíveis para a ação {symbol}")

        # Reset index to make 'Date' a column
        data.reset_index(inplace=True)
        
        # Verifique os nomes das colunas disponíveis
        logger.info(f"Colunas disponíveis: {data.columns.tolist()}")
        
        if 'Date' not in data.columns or 'Close' not in data.columns:
            raise Exception("Colunas necessárias não encontradas nos dados")

        # Limpeza e formatação dos dados
        data.rename(columns={'Date': 'timestamp'}, inplace=True)
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        return data
    except Exception as e:
        logger.error(f"Erro ao coletar dados da ação {symbol}: {e}")
        return pd.DataFrame()