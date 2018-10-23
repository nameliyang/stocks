import numpy as np
import talib
import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf

data = ts.get_k_data('002320', '2018-05-01', '2018-10-21')
sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)
fig = plt.figure(figsize=(32, 16))
ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(range(0, len(data['date']), 50))
ax.set_xticklabels(data['date'][::50])
ax.plot(sma_10, label='10 日均线')
ax.plot(sma_30, label='30 日均线')
ax.legend(loc='upper left')
mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'], width=0.5, colorup='r',
                      colordown='green', alpha=0.6)
plt.grid()
plt.show()
