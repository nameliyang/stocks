import tushare as ts
import os
import pandas as pd

stock_file = "stocks.csv"
if os.path.exists(stock_file):
    stocks = pd.read_csv(stock_file)
else:
    stocks = ts.get_stock_basics()
    stocks.to_csv(stock_file, float_format='str')
    stocks.reset_index(level=['code'], inplace=True)

for index, row in stocks.iterrows():
    print(str(index) + '\t' + str(row['code']) + '\t' + row['name'])
