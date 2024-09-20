import os
from dotenv import load_dotenv

# Carrega as variáveis do ambiente .env
load_dotenv()

#configuração do banco
DATABASE_URL = os.getenv('DATABASE_URL')
