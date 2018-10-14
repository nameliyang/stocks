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
    return df.to_json(orient='records')


if(__name__=='__main__'):
    data = get_k_data('000970','2018-01-01','2018-09-01')
    print(data)
