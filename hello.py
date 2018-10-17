import tushare as ts
import os
import pandas as pd
import numpy as np

stock_file = "stocks.csv"
if os.path.exists(stock_file):
    stocks = pd.read_csv(stock_file, dtype={'code': np.object_})
else:
    stocks = ts.get_stock_basics()
    stocks.to_csv(stock_file)
    stocks.reset_index(level=['code'], inplace=True)

stocks = stocks[~stocks['name'].str.contains('ST')]
stocks = stocks[~stocks['code'].str.startswith('3')]
ts.get_today_all()

def addCurrentData(df):
    ts.get_today_all()
    pass



for index, row in stocks.iterrows():
    ts.get_today_all()
    print(str(index) + '\t' + str(row['code']) + '\t' + row['name'] + '\t' + str(row['pe']))
