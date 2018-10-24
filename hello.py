import tushare as ts
import os
import pandas as pd
import numpy as np
from stock import daily

stock_file = "stocks.csv"
if os.path.exists(stock_file):
    stocks = pd.read_csv(stock_file, dtype={'code': np.object_})
else:
    stocks = ts.get_stock_basics()
    stocks.to_csv(stock_file)
    stocks.reset_index(level=['code'], inplace=True)

stocks = stocks[~stocks['name'].str.contains('ST')]
stocks = stocks[~stocks['name'].str.contains('S')]
stocks = stocks[~stocks['code'].str.startswith('3')]

for index, row in stocks.iterrows():
    code = str(row['code'])
    pe = row['pe']
    # print(str(index) + '\t' + str(row['code']) + '\t' + row['name'] + '\t' + str(row['pe']))
    if pe > 0 and pe < 100:
        data = daily.get_k_data(code, '2018-01-01', '2018-07-10')
        if (len(data) > 3):
            data = data.iloc[[-3, -2, -1]]
            preMacd = None
            isBuy = True
            for i, r in data.iterrows():
                if not preMacd:
                    preMacd = r['macd']
                else:
                    if r['macd'] >= preMacd and abs(r['macd'] - preMacd) > 0.1:
                        isBuy = True
                        preMacd = r['macd']
                    else:
                        isBuy= False
                        break
            if isBuy:
                print(str(index) + '\t' + str(row['code']) + '\t' + row['name'] + '\t' + str(row['pe']))
