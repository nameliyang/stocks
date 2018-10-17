import tushare as ts

currentPrice = ts.get_today_all()

currentPrice.to_csv('currentPrice.csv')
