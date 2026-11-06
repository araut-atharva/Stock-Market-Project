import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ms = pd.read_csv("HistoricalData/MorganStanley.csv", skiprows=[1, 2])
jpm = pd.read_csv("HistoricalData/JPMorganChase.csv", skiprows=[1, 2])
brk = pd.read_csv("HistoricalData/BerkshireHathawayInc.csv", skiprows=[1, 2])

ms = ms.rename(columns={'Price' : "Date"})
jpm = jpm.rename(columns={'Price' : "Date"})
brk = brk.rename(columns={'Price' : "Date"})

ms["Date"] = pd.to_datetime(ms["Date"])
jpm["Date"] = pd.to_datetime(jpm["Date"])
brk["Date"] = pd.to_datetime(brk["Date"])


#Calculate daily percentage returns of Morgan Stanley
daily_return_ms = ms['Close'].pct_change() * 100
print(f'The Daily Returns of Morgan Stanley (%): {daily_return_ms.head()}')

#Calculate daily percentage returns of JP Morgan Chase & Co.
daily_return_jpm = jpm['Close'].pct_change() * 100
print(f'The Daily Returns of JP Morgan Chase & Co. (%): {daily_return_jpm.head()}')

#Calculate daily percentage returns of Berkshire Hathaway Inc.
daily_return_brk = brk['Close'].pct_change() * 100
print(f'The Daily Returns of Berkshire Hathaway Inc. (%): {daily_return_brk.head()}')

#Calculate total return over the selected period of Morgan Stanley
start_price = ms['Close'].iat[0]
end_price = ms['Close'].iat[-1]

total_return_ms = ((end_price - start_price) / start_price) * 100
print(f'Total return of Morgan Stanley over 5 years: {total_return_ms}')

#Calculate total return over the selected period of JP Morgan Chase & Co.
start_price = jpm['Close'].iat[0]
end_price = jpm['Close'].iat[-1]

total_return_jpm = ((end_price - start_price) / start_price) * 100
print(f'Total return of JP Morgan Chase & Co. over 5 years: {total_return_jpm}')

#Calculate total return over the selected period of Berkshire Hathaway Inc.
start_price = brk['Close'].iat[0]
end_price = brk['Close'].iat[-1]

total_return_brk = ((end_price - start_price) / start_price) * 100
print(f'Total return of Berkshire Hathaway Inc. over 5 years: {total_return_brk}')

#Calculate average daily return of Morgan Stanley
ms["Daily_Return"] = ms["Close"].pct_change() * 100
avg_daily_return = ms["Daily_Return"].mean()
print(f'The Average Daily Return of Morgan Stanley: {avg_daily_return}')

#Calculate average daily return of JP Morgan Chase & Co.
jpm["Daily_Return"] = jpm["Close"].pct_change() * 100
avg_daily_return = jpm["Daily_Return"].mean()
print(f'The Average Daily Return of JP Morgan Chase & Co.: {avg_daily_return}')

#Calculate average daily return of Berkshire Hathaway Inc.
brk["Daily_Return"] = brk["Close"].pct_change() * 100
avg_daily_return = brk["Daily_Return"].mean()
print(f'The Average Daily Return of Berkshire Hathaway Inc.: {avg_daily_return}')

#Calculate daily return volatility using standard deviation of Morgan Stanley
ms["Daily_Return"] = ms["Close"].pct_change() * 100
daily_volatility_ms = ms["Daily_Return"].std()
print(f'The Daily Return Volatility of Morgan Stanley: {daily_volatility_ms}')

#Calculate daily return volatility using standard deviation of JP Morgan Chase & Co.
jpm["Daily_Return"] = jpm["Close"].pct_change() * 100
daily_volatility_jpm = jpm["Daily_Return"].std()
print(f'The Daily Return Volatility of JP Morgan Chase & Co.: {daily_volatility_jpm}')

#Calculate daily return volatility using standard deviation of Berkshire Hathaway Inc.
brk["Daily_Return"] = brk["Close"].pct_change() * 100
daily_volatility_brk = brk["Daily_Return"].std()
print(f'The Daily Return Volatility of Berkshire Hathaway Inc.: {daily_volatility_brk}')



plt.plot(ms['Date'], ms['Close'], label="Morgan Stanley", color="blue")
plt.plot(jpm['Date'], jpm['Close'], label="JP Morgan Chase", color="green")
plt.plot(brk['Date'], brk['Close'], label="Berkshire Hathaway", color="red")
plot_labels = dict(family="Arial",
                   color="black")
plt.xlabel("Date", **plot_labels, fontsize=15)
plt.ylabel("Stock Closing Price (USD)", **plot_labels, fontsize=15)
plt.title("Historical Stock Price Comparison (5 Years)", **plot_labels, fontsize=20, fontweight="bold")
plt.grid(axis="both",
         color="black",
         linewidth=1,
         linestyle="dashed")
plt.legend()
plt.show()



