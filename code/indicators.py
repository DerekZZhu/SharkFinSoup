import pandas as pd
import numpy as np
from scraper import get_single

'''
- Moving average convergence divergence (MACD) is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA.
- MACD triggers technical signals when it crosses above (to buy) or below (to sell) its signal line.
- The speed of crossovers is also taken as a signal of a market is overbought or oversold.
- MACD helps investors understand whether the bullish or bearish movement in the price is strengthening or weakening.
'''
def MACD(dataset):
    df = pd.DataFrame.copy(dataset)
    EMA_26 = df['Adj Close'].ewm(span=26, min_periods=26).mean()
    EMA_12 = df['Adj Close'].ewm(span=12, min_periods=12).mean()

    df['MACD'] = EMA_12.subtract(EMA_26)
    df['Signal'] = df['MACD'].ewm(span=9, min_periods=9).mean()

    return df


def ATR(dataset, n=14):
    df = pd.DataFrame.copy(dataset)
    df['ATR'] = np.maximum.reduce([
        df['High'] - df['Low'],
        abs(df['High'] - df['Adj Close'].shift(1)),
        abs(df['Low'] - df['Adj Close'].shift(1))
    ])
    
    return df['ATR'].ewm(com=n, min_periods=n).mean()
