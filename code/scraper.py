import yfinance as yf
import datetime as dt

def get_ohlcv(tickers=['AMZN', 'META', 'GOOG', 'AAPL', 'MSFT', 'NFLX'], start=(dt.datetime.today() - dt.timedelta(365)), end=(dt.datetime.today())):
    ohlcv_data = {}

    for ticker in tickers:
        ticker_data = yf.download(ticker, start, end)
        ticker_data.fillna(method='bfill', axis=0, inplace=True)
        ohlcv_data[ticker] = ticker_data


