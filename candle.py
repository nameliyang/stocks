import matplotlib.pyplot as plt
import mpl_finance as mpf
import numpy as np
import talib
from stock import daily

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

data = daily.get_k_data('000970', '2018-05-01', '2018-07-11')
sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)
fig = plt.figure(figsize=(32, 16))
ax = fig.add_subplot(2, 1, 1)
ax.set_xticks(range(0, len(data['date']), 7))
ax.set_xticklabels(data['date'][::7])
ax.plot(sma_10, label='10 日均线')
ax.plot(sma_30, label='30 日均线')
ax.legend(loc='upper left')
mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'], width=0.5, colorup='r',
                      colordown='green', alpha=0.6)


ax1 = fig.add_subplot(2,1, 2)
ax1.set_xticks(range(0, len(data['date']), 7))
ax1.set_xticklabels(data['date'][::7])
data.macd.plot(x=data.date,ax=ax1, kind='bar',color='b', label='Macd', width=0.5, alpha=0.6)
plt.grid()
plt.show()
