from termios import VEOL
import numpy as np

'''
The compounded annual growth rate (CAGR) is one of the most accurate ways to calculate and determine returns for anything that can rise or fall in value over time.
It measures a smoothed rate of return.
Investors can compare the CAGR of two or more alternatives to evaluate how well one stock performed against other stocks in a peer group or a market index.
CAGR is thus a good way to evaluate how different investments have performed over time, or against a benchmark.
The CAGR does not, however, reflect investment risk.
'''
def CAGR(df):
    cum_returns = (1+df['Adj Close'].pct_change()).cumprod()
    return cum_returns[-1]**(1/(len(df)/252)) - 1


def CAGR_II(df):
    return ((df['Adj Close'][-1]/df['Adj Close'][0])**(1/(len(df)/252))-1)*100


'''
Volatility represents how large an asset's prices swing around the mean price—it is a statistical measure of its dispersion of returns.
There are several ways to measure volatility, including beta coefficients, option pricing models, and standard deviations of returns.
Volatile assets are often considered riskier than less volatile assets because the price is expected to be less predictable.
Volatility is an important variable for calculating options prices.
'''
def volatility(df, window='daily'):
    lmap = {'daily':252, 'weekly':52, 'monthly':12}
    cum_returns = df['Adj Close'].pct_change()
    return cum_returns.std() * np.sqrt(lmap[window])


def sharpe(df, percent=0.03):
    return (CAGR(df - percent)/volatility(df))


def m_dd(df):
    cum_return = (1+df['Adj Close'].pct_change()).cumprod()
    cum_max_roll = cum_return.cummax()
    return ((cum_max_roll - cum_return)/cum_max_roll).max()

def calmar(df):
    data = df.copy()
    return CAGR_II(data)/m_dd(df)