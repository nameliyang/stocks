import tushare as ts
import os
import pandas as pd

'''
    code: code
    start:2018-01-01
    end :2018-08-24
'''

'''
def get_k_data(code, start, end):
    if os.path.exists(code + '.csv'):
        df = pd.read_csv(code + '.csv', encoding='GBK')
    else:
         df = ts.get_k_data(code, start=start, end=end)
         df.to_csv(code + '.csv', encoding='GBK', index=False, sep=',')
    return df.to_json(orient='records')
'''


def get_k_data(code, start, end):
    df = ts.get_k_data(code, start=start, end=end)
    df = getMACD(df)
    return df.to_json(orient='records')


def get_EMA(df, N):
    for i in range(len(df)):
        if i == 0:
            df.ix[i, 'ema'] = df.ix[i, 'close']
        if i > 0:
            df.ix[i, 'ema'] = (2 * df.ix[i, 'close'] + (N - 1) * df.ix[i - 1, 'ema']) / (N + 1)
    ema = list(df['ema'])
    return ema


def getMACD(df, short=12, long=26, M=9):
    if len(df) == 0:
        return df
    a = get_EMA(df, short)
    b = get_EMA(df, long)
    df['diff'] = pd.Series(a) - pd.Series(b)
    # print(df['diff'])
    for i in range(len(df)):
        if i == 0:
            df.ix[i, 'dea'] = df.ix[i, 'diff']
        if i > 0:
            df.ix[i, 'dea'] = (2 * df.ix[i, 'diff'] + (M - 1) * df.ix[i - 1, 'dea']) / (M + 1)
    df['macd'] = 2 * (df['diff'] - df['dea'])
    return df


if (__name__ == '__main__'):
    data = get_k_data('000970', '2018-01-01', '2018-09-01')
    print(data)
