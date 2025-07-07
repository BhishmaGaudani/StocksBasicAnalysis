import matplotlib.pyplot as plt
import yfinance as yf

ticker = 'NFLX'
print("Netflix Stock Data")
data = yf.download(ticker,period="5y")
print(f"\nData(Rows, Columns): {data.shape}")
print(f"\n{data.index[0].strftime('%Y-%m-%d')} to {data.index[-1].strftime('%Y-%m-%d')}")

print(f"\nFirst 5 rows:")
print(data.head())

print(f"\nLast 5 rows:")
print(data.tail())

print(f"\nBasic Statistics:")
print(data.describe())

print(f"\nMissing values:")
print(data.isnull().sum)

plt.subplot(2, 2, 1)
plt.plot(data.index, data['Open'], linewidth = 1, color = 'blue')
plt.title('Netflix Opening Price')
plt.xlabel('Dates')
plt.ylabel('Price ($)')
plt.grid(True, alpha = 0.3)


plt.subplot(2, 2, 2)
plt.plot(data.index, data['Close'], linewidth = 1, color = 'Yellow')
plt.title('Netflix Closing Price')
plt.xlabel('Dates')
plt.ylabel('Price ($)')
plt.grid(True, alpha = 0.3)


plt.subplot(212)
plt.plot(data.index, data['Volume'], linewidth = 1, color = 'Orange')
plt.title('Netflix Volume')
plt.xlabel('Dates')
plt.ylabel('Volume')
plt.grid(True, alpha = 0.3)

plt.tight_layout()
plt.show()



plt.subplot(211)
plt.plot(data.index, data['High'], linewidth=1, color='green', label='High')
plt.plot(data.index, data['Low'], linewidth=1, color='red', label='Low')
plt.title('Netflix High vs Low')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.grid(True, alpha=0.3)


plt.subplot(212)
daily_range = data['High'] - data['Low']
plt.plot(data.index, daily_range, linewidth=1, color='purple')
plt.title('Netflix Daily Price Range')
plt.xlabel('Date')
plt.ylabel('Price Range ($)')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


latest_price = float(data['Close'].iloc[-1])
price_5y_high = float(data['Close'].max())
price_5y_low = float(data['Close'].min())
avg_volume = float(data['Volume'].mean())


pct_from_high = ((latest_price / price_5y_high - 1) * 100)
pct_from_low = ((latest_price / price_5y_low - 1) * 100)

print(f"\nKey Metrics:")
print(f"Latest Price: ${latest_price:.2f}")
print(f"5-year High: ${price_5y_high:.2f}")
print(f"5-year Low: ${price_5y_low:.2f}")
print(f"Average Daily Volume: {avg_volume:,.0f}")
print(f"Price vs 5Y High: {pct_from_high:.2f}%")
print(f"Price vs 5Y Low: {pct_from_low:.2f}%")


price_range = price_5y_high - price_5y_low
current_position = (latest_price - price_5y_low) / price_range * 100

print(f"\nAdditional Analysis:")
print(f"5-year Range: ${price_range:.2f}")
print(f"Current Position in Range: {current_position:.1f}%")
print(f"Days of Data: {len(data)} trading days")