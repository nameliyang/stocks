import tushare as ts

df = ts.get_k_data('000970', start='2017-08-05', end='2018-08-05')



#plt.plot(df['date'],df['close'])
#plt.show()
#plt.plot()
#for index, row in df.iterrows():
 #   print(row['date'], row['open'], row['close'], row['high'], row['low'], row['volume'], row['code'])

print(type(df.index))



