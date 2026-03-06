import os
import matplotlib.pyplot as plt


def plot_efficient_frontier(simulation_results, optimal_portfolio, output_path="outputs/efficient_frontier.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(
        simulation_results["volatility"],
        simulation_results["returns"],
        c=simulation_results["sharpe"],
        cmap="viridis",
        alpha=0.7
    )

    plt.colorbar(scatter, label="Sharpe Ratio")

    plt.scatter(
        optimal_portfolio["volatility"],
        optimal_portfolio["return"],
        marker="*",
        s=300,
        label="Max Sharpe Portfolio"
    )

    plt.xlabel("Portfolio Volatility")
    plt.ylabel("Portfolio Return")
    plt.title("Efficient Frontier")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.show()

    print(f"Efficient Frontier plot saved to: {output_path}")
    
