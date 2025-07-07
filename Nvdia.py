import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = 'NVDA'
print("Downloading NVIDIA stock data")
data = yf.download(ticker, period="5y")
print(f"\nData(Rows, Columns): {data.shape}")
print(f"Date Range: {data.index[0].strftime('%Y-%m-%d')} to {data.index[-1].strftime('%Y-%m-%d')}")

print(f"\nFirst 5 rows:")
print(data.head())

print(f"\nLast 5 rows:")
print(data.tail())

print(f"\nBasic Statistics:")
print(data.describe())

print(f"\nMissing values:")
print(data.isnull().sum())


plt.figure(figsize=(12, 8))

# plt.subplot(2, 2, 1)
plt.subplot(2,2,1)
plt.plot(data.index, data['Close'], linewidth=1, color='blue')
plt.title('NVDA Closing Price')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True, alpha=0.3)

plt.subplot(2,2,2)
plt.plot(data.index, data['Open'], linewidth=1, color = 'green')
plt.title('NVDA Opening Price')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True, alpha=0.3)


plt.subplot(212)
plt.plot(data.index, data['Volume'], linewidth = 1, color = 'orange')
plt.title('NVDA Volume')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()

plt.subplot(211)
plt.plot(data.index, data['High'], linewidth=1, color='green', label='High')
plt.plot(data.index, data['Low'], linewidth=1, color='red', label='Low')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True, alpha = 0.3)


plt.subplot(212)
daily_range = data['High']-data['Low']
plt.plot(data.index, daily_range, linewidth = 1, color = 'purple')
plt.title('NVDA Daily Range')
plt.xlabel('Date')
plt.ylabel('Price Range ($)')
plt.grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()
