import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np
import talib
from stock import daily

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9
data = daily.get_k_data('000587', '2018-05-01', '2018-08-02')
print(data[['date','open','close','high','low','macd']].tail(20))
sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)
fig = plt.figure(figsize=(32, 16))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticks(range(0, len(data['date']), 1))
ax.set_xticklabels(data['date'][::1], rotation=90)
ax.plot(sma_10, label='10 日均线')
ax.plot(sma_30, label='30 日均线')
ax.legend(loc='upper left')
ax.tick_params(direction='out', length=6, width=2 ,
               grid_color='r', grid_alpha=0.5)
mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'], width=0.5, colorup='r',
                      colordown='green')

ax1 = fig.add_subplot(2, 1, 2)
ax1.set_xticks(range(0, len(data['date']), 1))
ax1.set_xticklabels(data['date'][::1], rotation=90)
ax1.tick_params(direction='out', length=6, width=2,
               grid_color='r', grid_alpha=0.5)
# data.macd.plot(x=data.date,ax=ax1, kind='bar',color='b', label='Macd', width=0.5, alpha=0.6)
data.loc[0, 'macd']=0.1
ax1.bar(data.date, data['macd'],width=0.25)
plt.grid()
plt.show()
