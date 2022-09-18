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
    df = dataset.copy()
    EMA_26 = df['Adj Close'].ewm(span=26, min_periods=26).mean()
    EMA_12 = df['Adj Close'].ewm(span=12, min_periods=12).mean()

    df['MACD'] = EMA_12.subtract(EMA_26)
    df['Signal'] = df['MACD'].ewm(span=9, min_periods=9).mean()

    return df


'''
- The average true range (ATR) is a market volatility indicator used in technical analysis.
- It is typically derived from the 14-day simple moving average of a series of true range indicators.
- The ATR was originally developed for use in commodities markets but has since been applied to all types of securities.
'''
def ATR(dataset, n=14):
    df = dataset.copy()
    df['ATR'] = np.maximum.reduce([
        df['High'] - df['Low'],
        abs(df['High'] - df['Adj Close'].shift(1)),
        abs(df['Low'] - df['Adj Close'].shift(1))
    ])

    return df['ATR'].ewm(com=n, min_periods=n).mean()


def BB(dataset, n=20):
    df = dataset.copy()
    df['Middle Band'] = df["Adj Close"].rolling(window=n).mean()
    std = df["Adj Close"].rolling(window=n).std(ddof=0)

    df['Upper Band'] = df['Middle Band'] + 2*std
    df['Lower Band'] = df['Middle Band'] - 2*std

    return df[['Middle Band', 'Upper Band', 'Lower Band']]


def RSI(dataset, n=14):
    df = dataset.copy()
    change = df['Adj Close'] - df['Adj Close'].shift(1)
    df['Gain'] = np.where(change >= 0, change, 0.0)
    df['Loss'] = np.where(change < 0, -1*change, 0.0)

    avg_gain = df['Gain'].ewm(alpha=1/n, min_periods=n).mean()
    avg_loss = df['Loss'].ewm(alpha=1/n, min_periods=n).mean()
    rs = avg_gain/avg_loss
    df['RSI'] = 100 - (100/(1+rs))

    return df


def ADX(dataset, n=20):
    df = dataset.copy()
    df['ATR'] = ATR(dataset, n)
    up_move = df['High'] - df['High'].shift(1)
    down_move = df['Low'].shift(1) - df['Low']
    pos_DI = 100*(np.where((up_move>down_move) & (up_move > 0), up_move, 0)/df['ATR']).ewm(com=n, min_periods=n).mean()
    neg_DI = 100*(np.where((down_move> up_move) & (down_move> 0), down_move, 0)/df['ATR']).ewm(com=n, min_periods=n).mean()

    df['ADX'] = 100 * abs((pos_DI - neg_DI)/(pos_DI + neg_DI)).ewm(com=n, min_periods=n).mean()
    return df

df = get_single('AMZN')
print(ADX(df).tail(10))