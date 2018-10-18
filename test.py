from stock import daily

df = daily.get_k_data('000970', '2018-01-08', '2018-10-17')
df = df[50:]

first_macd = None
second_macd = None
third_macd = None
isBuy = False
pre_macd = None;

for index, row in df.iterrows():
    date = row['date']
    macd = row['macd']
    open = row['open']
    close = row['close']
    low = row['low']
    high = row['high']
    # print(str(open)+'\t'+str(close)+'\t'+str(low)+'\t'+str(high)+'\t'+str(macd)+'\t'+ date)
    if not first_macd and not second_macd and not third_macd:
        first_macd = macd
    elif first_macd and not second_macd and not third_macd:
        second_macd = macd
    elif first_macd and  second_macd and not third_macd:
        third_macd = macd
