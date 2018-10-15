import tushare as ts
import matplotlib.pyplot as plt

df = ts.get_k_data('002230', '2018-10-08', '2018-10-15')
stock_data = df.sort_index()
f1,ax = plt.subplots(figsize=(10, 5))
ax.plot(stock_data.date, stock_data['close'], 'black', label='Price')
plt.bar(stock_data.date,stock_data['volume']/100000, 'black', label='valume')
plt.show()
print(stock_data)
