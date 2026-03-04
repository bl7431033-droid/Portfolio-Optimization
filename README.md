Portfolio Optimization with Modern Portfolio Theory
Overview

This project implements a portfolio optimization framework based on Modern Portfolio Theory (MPT) to determine the optimal asset allocation that maximizes risk-adjusted return.

Using historical market data, the model:

Estimates expected returns and covariance matrix

Simulates thousands of random portfolios via Monte Carlo methods

Computes portfolio volatility and Sharpe Ratio

Identifies the maximum Sharpe portfolio

Visualizes the Efficient Frontier

The objective is to construct an optimal portfolio allocation under a mean-variance framework.

Mathematical Framework

Let:

𝜇
μ = expected return vector

Σ
Σ = covariance matrix

𝑤
w = portfolio weights

Expected Portfolio Return
𝑅
𝑝
=
𝑤
𝑇
𝜇
R
p
	​

=w
T
μ
Portfolio Volatility
𝜎
𝑝
=
𝑤
𝑇
Σ
𝑤
σ
p
	​

=
w
T
Σw
	​

Sharpe Ratio
𝑆
=
𝑅
𝑝
−
𝑅
𝑓
𝜎
𝑝
S=
σ
p
	​

R
p
	​

−R
f
	​

	​


Where:

𝑅
𝑓
R
f
	​

 = risk-free rate (assumed 0 if not specified)

The optimal portfolio is defined as the weight vector 
𝑤
∗
w
∗
 that maximizes the Sharpe Ratio.

Data

Source: Yahoo Finance (via yfinance)

Assets:

AAPL

MSFT

NVDA

SPY

Period: From 2018-01-01 onward

Frequency: Daily adjusted close prices

Daily returns are computed using percentage change.

Methodology
1. Data Collection

Historical adjusted closing prices are downloaded programmatically.

2. Feature Engineering

Daily return calculation

Estimation of mean return vector

Estimation of covariance matrix

3. Monte Carlo Simulation

Randomly generate 5000+ portfolio weight vectors

Normalize weights such that 
∑
𝑤
𝑖
=
1
∑w
i
	​

=1

Compute portfolio return, volatility, and Sharpe Ratio

Store simulation results

4. Optimal Portfolio Selection

The portfolio with the highest Sharpe Ratio is selected as the optimal allocation.

5. Efficient Frontier Visualization

Scatter plot of:

X-axis: Portfolio Volatility

Y-axis: Portfolio Return

The maximum Sharpe portfolio is highlighted.

Example Output

Optimal Portfolio Allocation (example):

AAPL: 35%

MSFT: 25%

NVDA: 20%

SPY: 20%

Maximum Sharpe Ratio:

1.42

An Efficient Frontier plot is generated and saved in the outputs/ directory.

Project Structure
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
Technology Stack

Python

NumPy

Pandas

yfinance

Matplotlib

SciPy (optional for numerical optimization)

How to Run

Install dependencies:

pip install -r requirements.txt

Execute optimization:

python src/optimize.py

Outputs:

Efficient Frontier plot

Optimal portfolio weights

Maximum Sharpe Ratio

Key Concepts Demonstrated

Mean-Variance Optimization

Covariance-based risk modeling

Monte Carlo portfolio simulation

Risk-adjusted performance measurement

Efficient Frontier analysis

Extensions (Future Improvements)

Incorporating non-zero risk-free rate

Annualization of return and volatility

Constrained optimization (no short-selling, weight bounds)

Comparison with equal-weight benchmark

Rolling window backtesting

Use of SciPy optimizer instead of brute-force Monte Carlo

Author

Kelvin Mao
Quantitative Finance / Data-Driven Investment Modeling
