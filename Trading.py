import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

stock1 = 'MSFT'
stock = stock1
data = yf.download(stock
                   ,start="2020-01-01"
                  )
data['TP'] = (data['High'] + data['Low'] + data['Close'])/3
data = data['TP']

