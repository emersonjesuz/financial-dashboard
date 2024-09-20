import numpy as np
import pandas as pd
from scipy.optimize import minimize
from logger import logger

def optimize_portfolio(returns: pd.DataFrame) -> np.ndarray:
    """
    Função que otimiza o portfólio usando a Teoria Moderna de Portfólios.
    
    Parâmetros:
        returns (pd.DataFrame): Retornos históricos dos ativos.
    
    Retorna:
        np.ndarray: Pesos otimizados dos ativos no portfólio.
    """
    try:
        mean_returns = returns.mean()
        cov_matrix = returns.cov()
        num_assets = len(mean_returns)
        
        def objective(weights):
            return -np.dot(weights, mean_returns) / np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for asset in range(num_assets))
        
        result = minimize(objective, num_assets * [1. / num_assets,], method='SLSQP', bounds=bounds, constraints=constraints)
        return result.x
    except Exception as e:
        logger.error(f"Erro na otimização do portfólio: {e}")
        return np.zeros(num_assets)