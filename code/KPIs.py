def CAGR(df):
    cum_returns = (1+df['Adj Close'].pct_change()).cumprod()
    return cum_returns[-1]**(1/(len(df)/252)) - 1


def CAGR(df):
    return ((df['Adj Close'][-1]/df['Adj Close'][0])**(1/(len(df)/252))-1)*100