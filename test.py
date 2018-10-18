from stock import daily

df = daily.get_k_data('000970', '2018-01-08', '2018-10-17')
df = df[50:]

first_macd = None
second_macd = None
third_macd = None
isBuy = False
pre_macd = None
match = False
for index, row in df.iterrows():
    date = row['date']
    macd = row['macd']
    open = row['open']
    close = row['close']
    low = row['low']
    high = row['high']
    if date=='2018-06-25':
        print("deug")
    # print(str(open)+'\t'+str(close)+'\t'+str(low)+'\t'+str(high)+'\t'+str(macd)+'\t'+ date)
    if not first_macd and not second_macd and not third_macd:
        first_macd = macd
        match = True
    elif first_macd and not second_macd and not third_macd:
        if macd > first_macd and macd < 0:
            second_macd = macd
        elif macd < 0:
            first_macd = macd
        else:
            first_macd = None
    elif first_macd and second_macd and not third_macd:
        if macd - second_macd > second_macd - first_macd and macd < 0:
            third_macd = macd
        elif macd > second_macd and macd < 0:
            first_macd = second_macd
            second_macd = macd
        else:
            first_macd = macd
            second_macd = None
            third_macd = None

    if first_macd and second_macd and third_macd:
        if abs(third_macd) >= 0.15:
            isBuy = True
            print('date = ' + date + 'buy')
        else:
            first_macd = None
            second_macd = None
            third_macd = None
