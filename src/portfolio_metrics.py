import numpy as np


def portfolio_return(weights, mean_returns):
    """
    Calculate expected portfolio return.
    """
    return np.sum(mean_returns * weights)


def portfolio_volatility(weights, cov_matrix):
    """
    Calculate portfolio volatility (standard deviation).
    """
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))


def sharpe_ratio(portfolio_ret, portfolio_vol, risk_free_rate=0.0):
    """
    Calculate Sharpe Ratio.
    """
    if portfolio_vol == 0:
        return 0
    return (portfolio_ret - risk_free_rate) / portfolio_vol

