import yfinance as yf

#Morgan Stanley Historical Data
ms = yf.download("MS", start="2021-01-01", end="2026-01-01")
ms.to_csv("MorganStanley.csv")

#JP Morgan Chase & Co. Historical Data
jpm = yf.download("JPM", start="2021-01-01", end="2026-01-01")
jpm.to_csv("JPMorganChase.csv")

#Berkshire Hathaway Inc. Historical Data
brk = yf.download("BRK-B", start="2021-01-01", end="2026-01-01")
brk.to_csv("BerkshireHathawayInc.csv")