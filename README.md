# Stock Analysis: Banking & Berkshire (2021-2025)

A Python script that compares the performance of Morgan Stanley,
JPMorgan Chase, and Berkshire Hathaway over five years.

## What it does
- Calculates daily percentage returns
- Calculates total return over the period
- Calculates average daily return and volatility (standard deviation)
- Plots closing prices for all three stocks

## Preview
<img width="1920" height="959" alt="Historical_Data" src="https://github.com/user-attachments/assets/d95cdd7f-86c2-4911-ba21-44c9a30b45e6" />

## Tech used
Python, Pandas, NumPy, Matplotlib, YFinance

## How to run
1. Clone this repo:
      ```bash
      git clone https://github.com/araut-atharva/Stock-Market-Project.git
      cd Stock-Market-Project
      ```
2. Install dependencies:
   pip install -r requirements.txt
3. Make sure the CSV files are in a `HistoricalData/` folder.
4. Run the script:
   python Notebooks/stock_analysis.py

## Data
Historical daily prices downloaded from Yahoo Finance (yfinance),
January 2021 to December 2025.

## Findings (Jan 2021 - Dec 2025)

- **Highest return:** Morgan Stanley, up about 205% over the period,
  followed by JPMorgan Chase (about 191%) and Berkshire Hathaway (about 120%).
- **Highest volatility:** Morgan Stanley (1.78% daily standard deviation).
  Berkshire Hathaway was the most stable (1.09%).
- **Risk vs. Reward:** The stock with the highest return was also the
  most volatile, while the most stable stock returned the least.
- **Note:** Returns use closing prices, which may not include dividends,
  so total returns are slightly understated.
