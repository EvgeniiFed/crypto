from config import api_key, api_secret
from binance.client import client
import requests
import numpy as np
import talib
import time

SYMBOL = 'ALGOUSDT'
INTERVAL = '15m'
LIMIT = '200'
QUANT = 35

client = Client(api_key,api_secret)

def get_data():
    url = 'https://api.binance.com/api/v3/klines?symbol={}&interval={}&limit={}'.format(SYMBOL, INTERVAL, LIMIT)
    res = requests.get(url)
    return_data = []
    for each in res.json():
        return_data.append(float(each[4]))
    return np.array(return_data)

# test = get_data()
# print(test)

def place_order(order_type):
    if(order_type == 'BUY'):
        order = client.create_order(symbol=SYMBOL, side=order_type, type='MARKET', quantity=QUANT)
        print(order, 'Покупка')

    if(order_type == 'SELL'):
        order = client.create_order(symbol=SYMBOL, side=order_type, type='MARKET', quantity=QUANT)
        print(order, 'Продажа')

def main():
    buy = False
    sell = True
    print('Робот ищет сигнал на покупку ...')
    while True:
        closing_data = get_data()
        rsi = talib.RSI(closing_data, 7)[-1]
        print(rsi)

        if(rsi <=30 and not buy):
            place_order('BUY')
            buy = not buy
            sell = not sell

        if(rsi >= 70 and not sell):
            place_order('SELL')
            buy = not buy
            sell = not sell

    time.sleep(1)

if __name__ == '__main__':
    main()
