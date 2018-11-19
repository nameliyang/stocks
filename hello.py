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


# def buyJudge(first_macd, second_macd, third_macd):
#     if first_macd < 0 and second_macd > first_macd and third_macd < 0 and third_macd - second_macd > second_macd - first_macd and abs(
#             third_macd) > 0.15 and abs(first_macd) > 0.25 and second_macd - first_macd >= 0.05 and abs(
#         first_macd) >= 0.7:
#         return True
#     return False
def buyJudge(first_macd, second_macd, third_macd):
    if first_macd < 0 and second_macd > first_macd and third_macd>second_macd and third_macd < 0 and third_macd - second_macd >= second_macd - first_macd:
        return True
    return False


for index, row in stocks.iterrows():
    code = str(row['code'])
    pe = row['pe']
    # print(str(index) + '\t' + str(row['code']) + '\t' + row['name'] + '\t' + str(row['pe']))
    if pe > 0 and pe < 100:
        data = daily.get_k_data(code, '2018-01-01', '2018-11-15')
        if (len(data) > 3):
            data = data.iloc[[-3, -2, -1]]
            preMacd = None
            isBuy = True
            firstMacd = data['macd'].iloc[0]
            secondMacd = data['macd'].iloc[1]
            thirdMacd = data['macd'].iloc[2]
            if buyJudge(firstMacd, secondMacd, thirdMacd):
                print('buy ' + code + ' ' + row['name']+' close:'+ str(data['close'].iloc[2]))
