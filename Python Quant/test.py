import yfinance as yf
apple= yf.Ticker("aapl")

# show actions (dividends, splits)
apple.actions