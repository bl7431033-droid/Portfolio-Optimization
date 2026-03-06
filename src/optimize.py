import os
import pandas as pd

from download_data import download_price_data
from simulation import simulate_portfolios, get_optimal_portfolio
from visualize import plot_efficient_frontier


def main():
    stocks = ["AAPL", "MSFT", "NVDA", "SPY"]
    start_date = "2018-01-01"
    price_file = "data/prices.csv"
    output_file = "outputs/optimal_portfolio.txt"

    if not os.path.exists(price_file):
        data = download_price_data(stocks, start_date=start_date, output_path=price_file)
    else:
        data = pd.read_csv(price_file, index_col=0, parse_dates=True)
        print(f"Loaded existing data from: {price_file}")

    returns = data.pct_change().dropna()

    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    simulation_results = simulate_portfolios(
        mean_returns=mean_returns,
        cov_matrix=cov_matrix,
        num_portfolios=5000,
        risk_free_rate=0.0
    )

    optimal_portfolio = get_optimal_portfolio(simulation_results)

    print("\nOptimal Portfolio Allocation:")
    for stock, weight in zip(stocks, optimal_portfolio["weights"]):
        print(f"{stock}: {weight:.2%}")

    print(f"\nExpected Return: {optimal_portfolio['return']:.4f}")
    print(f"Volatility: {optimal_portfolio['volatility']:.4f}")
    print(f"Sharpe Ratio: {optimal_portfolio['sharpe']:.4f}")

    os.makedirs("outputs", exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Optimal Portfolio Allocation\n")
        f.write("============================\n")
        for stock, weight in zip(stocks, optimal_portfolio["weights"]):
            f.write(f"{stock}: {weight:.2%}\n")
        f.write("\n")
        f.write(f"Expected Return: {optimal_portfolio['return']:.4f}\n")
        f.write(f"Volatility: {optimal_portfolio['volatility']:.4f}\n")
        f.write(f"Sharpe Ratio: {optimal_portfolio['sharpe']:.4f}\n")

    print(f"\nOptimal portfolio results saved to: {output_file}")

    plot_efficient_frontier(simulation_results, optimal_portfolio)


if __name__ == "__main__":
    main()
    
