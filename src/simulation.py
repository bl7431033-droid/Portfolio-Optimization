import numpy as np
from portfolio_metrics import portfolio_return, portfolio_volatility, sharpe_ratio


def simulate_portfolios(mean_returns, cov_matrix, num_portfolios=5000, risk_free_rate=0.0):
    num_assets = len(mean_returns)

    results = {
        "returns": [],
        "volatility": [],
        "sharpe": [],
        "weights": []
    }

    for _ in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)

        port_return = portfolio_return(weights, mean_returns)
        port_volatility = portfolio_volatility(weights, cov_matrix)
        port_sharpe = sharpe_ratio(port_return, port_volatility, risk_free_rate)

        results["returns"].append(port_return)
        results["volatility"].append(port_volatility)
        results["sharpe"].append(port_sharpe)
        results["weights"].append(weights)

    return results


def get_optimal_portfolio(simulation_results):
    sharpe_array = np.array(simulation_results["sharpe"])
    max_index = np.argmax(sharpe_array)

    return {
        "return": simulation_results["returns"][max_index],
        "volatility": simulation_results["volatility"][max_index],
        "sharpe": simulation_results["sharpe"][max_index],
        "weights": simulation_results["weights"][max_index]
    }

