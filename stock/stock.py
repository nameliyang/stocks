import stock as stock
from stock import stock
import urllib.request
import time


def code_2_symbol(code):
    return 'sh%s' % code if code[:1] in ['5', '6', '9'] or code[:2] in ['11', '13'] else 'sz%s' % code


def getcurrent_day(code):
    code = stock.code_2_symbol(code)
    url = 'http://hq.sinajs.cn/list=' + code
    current_day = {}
    content = urllib.request.urlopen(url).read().decode('gbk')
    arr = content.split("\"")
    arr = arr[1].split(",")
    current_day['open'] = float(arr[1])
    current_day['close'] = float(arr[3])
    current_day['high'] = float(arr[4])
    current_day['low'] = float(arr[5])
    current_day['date'] = time.strftime("%Y-%m-%d", time.localtime())
    return current_day
