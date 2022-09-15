import pandas as pd

'''
- Moving average convergence divergence (MACD) is calculated by subtracting the 26-period exponential moving average (EMA) from the 12-period EMA.
- MACD triggers technical signals when it crosses above (to buy) or below (to sell) its signal line.
- The speed of crossovers is also taken as a signal of a market is overbought or oversold.
- MACD helps investors understand whether the bullish or bearish movement in the price is strengthening or weakening.
'''
def MACD(dataset):
    df = pd.DataFrame(dataset)
    EMA_26 = df['Adj Close'].ewm(span=26, min_periods=26).mean()
    EMA_12 = df['Adj Close'].ewm(span=12, min_periods=12).mean()

    df['MACD'] = EMA_12.subtract(EMA_26)
    df['Signal'] = df['MACD'].ewm(span=9, min_periods=9).mean()

    return df