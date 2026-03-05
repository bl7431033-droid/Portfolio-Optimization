# Portfolio Optimization with Modern Portfolio Theory

## Overview

This project implements a portfolio optimization framework based on **Modern Portfolio Theory (MPT)** to determine the optimal asset allocation that maximizes risk-adjusted return.

Using historical market data, the model:

* Estimates expected returns and covariance matrix
* Simulates thousands of random portfolios via Monte Carlo methods
* Computes portfolio volatility and Sharpe Ratio
* Identifies the maximum Sharpe portfolio
* Visualizes the Efficient Frontier

The objective is to construct an optimal portfolio allocation under a mean-variance framework.

---

## Mathematical Framework

Let:

* ( \mu ) = expected return vector
* ( \Sigma ) = covariance matrix
* ( w ) = portfolio weights

### Expected Portfolio Return

[
R_p = w^T \mu
]

### Portfolio Volatility

[
\sigma_p = \sqrt{w^T \Sigma w}
]

### Sharpe Ratio

[
S = \frac{R_p - R_f}{\sigma_p}
]

Where:

* ( R_f ) = risk-free rate (assumed 0 if not specified)

The optimal portfolio is defined as the weight vector ( w^* ) that maximizes the Sharpe Ratio.

---

## Data

* Source: Yahoo Finance (via `yfinance`)
* Assets:

  * AAPL
  * MSFT
  * NVDA
  * SPY
* Period: From 2018-01-01 onward
* Frequency: Daily adjusted close prices

Daily returns are computed using percentage change.

---

## Methodology

### 1. Data Collection

Historical adjusted closing prices are downloaded programmatically.

### 2. Feature Engineering

* Daily return calculation
* Estimation of mean return vector
* Estimation of covariance matrix

### 3. Monte Carlo Simulation

* Randomly generate 5000+ portfolio weight vectors
* Normalize weights such that ( \sum w_i = 1 )
* Compute portfolio return, volatility, and Sharpe Ratio
* Store simulation results

### 4. Optimal Portfolio Selection

The portfolio with the highest Sharpe Ratio is selected as the optimal allocation.

### 5. Efficient Frontier Visualization

Scatter plot of:

* X-axis: Portfolio Volatility
* Y-axis: Portfolio Return

The maximum Sharpe portfolio is highlighted.

---

## Example Output

Optimal Portfolio Allocation (example):

* AAPL: 35%
* MSFT: 25%
* NVDA: 20%
* SPY: 20%

Maximum Sharpe Ratio:

1.42

An Efficient Frontier plot is generated and saved in the `outputs/` directory.

---

## Project Structure

```
portfolio-optimization/

README.md
requirements.txt

data/
    prices.csv

notebooks/
    exploration.ipynb

src/
    download_data.py
    portfolio_metrics.py
    simulation.py
    optimize.py
    visualize.py

outputs/
    efficient_frontier.png
    optimal_portfolio.txt
```

---

## Technology Stack

* Python
* NumPy
* Pandas
* yfinance
* Matplotlib
* SciPy (optional for numerical optimization)

---

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Execute optimization:

```
python src/optimize.py
```

Outputs:

* Efficient Frontier plot
* Optimal portfolio weights
* Maximum Sharpe Ratio

---

## Key Concepts Demonstrated

* Mean-Variance Optimization
* Covariance-based risk modeling
* Monte Carlo portfolio simulation
* Risk-adjusted performance measurement
* Efficient Frontier analysis

---

## Extensions (Future Improvements)

* Incorporating non-zero risk-free rate
* Annualization of return and volatility
* Constrained optimization (no short-selling, weight bounds)
* Comparison with equal-weight benchmark
* Rolling window backtesting
* Use of SciPy optimizer instead of brute-force Monte Carlo

---

## Author

Brian Lin / Kelvin Mao
Quantitative Finance / Data-Driven Investment Modeling
