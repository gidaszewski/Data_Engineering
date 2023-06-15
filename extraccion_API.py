import yfinance as yf
goog = yf.Ticker('GOOG')
goog.info

print(goog.info)

hist = goog.history(period="1y")
hist['Date'] = hist.index
hist = hist.reset_index(drop=True)
hist

print(hist)