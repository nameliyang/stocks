from stock import daily

df = daily.get_k_data('000970', '2018-01-08', '2018-10-17')
df = df[50:]

first_macd = None
second_macd = None
third_macd = None
isBuy = False
pre_macd = None;
for row in df.iterrows():
    date = row['date']
    macd = row['macd']


    if not first_macd and macd < 0:
        first_macd = macd

    if first_macd and not second_macd and macd < 0:
        second_macd = macd
    else:
        first_macd = second_macd
        second_macd = None

    if first_macd and second_macd and (second_macd-first_macd < macd - second_macd):
        isBuy = True
    else:
        first_macd = None
        second_macd = None
        third_macd = None
