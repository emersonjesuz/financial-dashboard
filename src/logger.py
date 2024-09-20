import logging
import os

# Certifique-se de que a pasta 'Log' existe, caso contrário, crie-a
log_directory = "Log"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Criação do handler e configuração do formato de log
log_file_path = os.path.join(log_directory, 'portfolio_optimization.log')
handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Adiciona o handler ao logger
logger.addHandler(handler)