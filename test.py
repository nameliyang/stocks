from stock import daily

df = daily.get_k_data('000970', '2018-01-08', '2018-10-17')
df = df[50:]

first_macd = None
second_macd = None
third_macd = None

isBuy = False
match = False

def buyJudge(first_macd, second_macd, third_macd):
    if first_macd < 0 and second_macd > first_macd and third_macd < 0 and third_macd - second_macd > second_macd - first_macd and abs(
            third_macd) > 0.15 and abs(first_macd) > 0.25  and second_macd - first_macd >= 0.05 and abs(first_macd) >= 0.7:
        return True
    return False


pre_macd = None
macd_diff = None
for index, row in df.iterrows():
    date = row['date']
    macd = row['macd']
    open = row['open']
    close = row['close']
    low = row['low']
    high = row['high']
    # print(str(open)+'\t'+str(close)+'\t'+str(low)+'\t'+str(high)+'\t'+str(macd)+'\t'+ date)
    if (date == '2018-06-28'):
        print("--------------debug")
    if isBuy:
        nowdiff = macd - pre_macd
        if macd > pre_macd and abs(nowdiff - macd_diff) > 0.05:
            print("sell " + str(date) + ",price " + str(close))
            pre_macd = None
            macd_diff = None
            first_macd = None
            second_macd = None
            third_macd = None
            isBuy = False
        else:
            macd_diff = macd - pre_macd
            pre_macd = macd
        continue

    if not first_macd and not second_macd and not third_macd:
        first_macd = macd
    elif first_macd and not second_macd and not third_macd:
        second_macd = macd
    elif first_macd and second_macd and not third_macd:
        third_macd = macd

    if first_macd and second_macd and third_macd:
        if buyJudge(first_macd, second_macd, third_macd):
            print('buy date = ' + str(date) + ' close=' + str(close))
            isBuy = True
            macd_diff = third_macd - second_macd
            pre_macd = third_macd
            continue
        else:
            if third_macd < 0 and third_macd > second_macd:
                first_macd = second_macd
                second_macd = third_macd
                third_macd = None
            else:
                first_macd = None
                second_macd = None
                third_macd = None
