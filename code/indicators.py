import pandas as pd

def MACD(dataset):
    df = pd.DataFrame(dataset)
    EMA_26 = df['Adj Close'].ewm(span=26, min_periods=26).mean()
    EMA_12 = df['Adj Close'].ewm(span=12, min_periods=12).mean()

    df['MACD'] = EMA_12.subtract(EMA_26)
    df['Signal'] = df['MACD'].ewm(span=9, min_periods=9).mean()

    return df