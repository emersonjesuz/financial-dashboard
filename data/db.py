import pandas as pd
from sqlalchemy import create_engine
from data.config import DATABASE_URL
from src.logger import logger

def save_to_db(df: pd.DataFrame, table_name: str):
    """
    Função que salva um DataFrame no banco de dados PostgreSQL.
    
    Parâmetros:
        df (pd.DataFrame): O DataFrame a ser salvo.
        table_name (str): O nome da tabela onde os dados serão salvos.
    """
    try:
        engine = create_engine(DATABASE_URL)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info(f"Dados salvos na tabela {table_name}")
    except Exception as e:
        logger.error(f"Erro ao salvar dados no banco de dados: {e}")