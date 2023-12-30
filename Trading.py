# imports
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# pulling from yfinance
stock1 = 'MSFT'
stock = stock1
data = yf.download(stock
                   ,start="2020-01-01"
                  )
data['TP'] = (data['High'] + data['Low'] + data['Close'])/3
data = data['TP']

print(data)

# formatting data
n = 20
m = 2
MA = data.rolling(n).mean()
sig = data.rolling(n).std()
bolu = MA + m * sig
bold = MA - m * sig

plt.figure(figsize = (20,12))
plt.plot(data, label = 'TP = (High + Low + Close) / 3')
plt.plot(MA, label = 'Moving Average')
plt.plot(bolu, label = 'Upper Bollinger Band')
plt.plot(bold, label = 'Lower Bollinger Band')
plt.legend()
plt.title(stock1)
plt.show()
