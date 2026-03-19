# Portfolio Optimization with Modern Portfolio Theory

## Overview

This project implements a portfolio optimization framework based on **Modern Portfolio Theory (MPT)** to determine the optimal asset allocation that maximizes risk-adjusted return.

Using historical market data, the model:

- Estimates expected returns and covariance matrix
- Simulates thousands of random portfolios using Monte Carlo methods
- Computes portfolio volatility and Sharpe Ratio
- Identifies the maximum Sharpe portfolio
- Visualizes the Efficient Frontier

The objective is to construct an optimal portfolio allocation under a mean-variance framework.

---

## Assets

Assets used in this project:

- AAPL
- MSFT
- NVDA
- SPY

Historical price data is downloaded from **Yahoo Finance** using the `yfinance` Python library.

Data period:

2018 – Present

Frequency:

Daily adjusted close prices.

---

## Quantitative Model

Let:

- **μ** = expected return vector
- **Σ** = covariance matrix
- **w** = portfolio weights

### Expected Portfolio Return

Rp = wᵀ μ

### Portfolio Volatility

σp = √(wᵀ Σ w)

### Sharpe Ratio

S = (Rp − Rf) / σp

Where:

- **Rf** = risk-free rate (assumed 0 if not specified)

The optimal portfolio is defined as the weight vector **w*** that maximizes the Sharpe Ratio.

---

## Methodology

### 1. Data Collection

Historical adjusted closing prices are downloaded using `yfinance`.

### 2. Feature Engineering

Daily returns are computed using percentage change.

Key statistics:

- Mean return vector
- Covariance matrix

These metrics form the basis of the mean-variance portfolio model.

### 3. Monte Carlo Portfolio Simulation

To explore possible allocations, the model generates thousands of random portfolios.

For each portfolio:

1. Generate random weights
2. Normalize weights so that the sum equals 1
3. Compute expected return
4. Compute portfolio volatility
5. Compute Sharpe Ratio

More than **5000 portfolios** are simulated.

### 4. Optimal Portfolio Selection

The portfolio with the **maximum Sharpe Ratio** is selected as the optimal allocation.

### 5. Efficient Frontier Visualization

Each simulated portfolio is plotted based on:

- X-axis: Portfolio Volatility
- Y-axis: Portfolio Return

The optimal portfolio is highlighted on the Efficient Frontier.

---

# Results

### Efficient Frontier

![Result](images/result.png)

---

## Example Output

Example optimal portfolio:

AAPL: 35%  
MSFT: 25%  
NVDA: 20%  
SPY: 20%

Maximum Sharpe Ratio:

1.42

---

## Project Structure

```text
portfolio-optimization/

README.md
requirements.txt

data/
    prices.csv

src/
    download_data.py
    portfolio_metrics.py
    simulation.py
    optimize.py
    visualize.py

outputs/
    efficient_frontier.png
    optimal_portfolio.txt
````

---

## Technology Stack

Python

Libraries used:

* pandas
* numpy
* yfinance
* matplotlib
* scipy (optional)

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the optimization script:

```bash
python src/optimize.py
```

Outputs generated:

* Efficient Frontier plot
* Optimal portfolio weights
* Maximum Sharpe Ratio

---

## Key Concepts Demonstrated

* Modern Portfolio Theory
* Mean-Variance Optimization
* Covariance-based risk modeling
* Monte Carlo portfolio simulation
* Risk-adjusted return evaluation
* Efficient Frontier visualization

---

## Future Improvements

Possible extensions:

* Incorporate a non-zero risk-free rate
* Annualize return and volatility
* Add portfolio constraints (no short selling)
* Implement numerical optimization using SciPy
* Perform rolling window backtesting
* Compare against equal-weight benchmark

---

## Author

Brian Lin
Kelvin Mao

Quantitative Finance / Data-Driven Investment Modeling
