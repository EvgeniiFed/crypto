# python -u main.py
from binance.client import Client
import keys
import pandas as pd
import time

client = Client(keys.api_key, keys.api_secret)


# function for search top gainer coins
def top_coin():
    all_tickers = pd.DataFrame(client.get_ticker())
    usdt = all_tickers[all_tickers.symbol.str.contains('USDT')]
    work = usdt[~((usdt.symbol.str.contains('UP')) | ] (usdt.symbol.str.contains('DOWN')))]
    top_coin = work[work.priceChangePercent == work.priceChangePercent.max()]
    top_coin = top_coin.symbol.values[0]
    return top_coin

# function for show grow up token just now
def last_data(symbol, interval, lookback):
    frame = pd.DataFrame(cient.get_historical_klines(symbol, interval, lookback + 'min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'Hight', 'Low', 'Close', 'Volume']
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

# function for strategy
def strategy(buy_amt, SL=0.97, Target=1.10, open_position=False):
    try:
        asset = top_coin()
        df = last_data(asset, '1m', '120') # берем тикер, полученный из предыдущей функции top_coin, далее создаем переменную, куда кладем этот тикер, с интервалом 1 минута и с историей в 120 минута

    except:
        time.sleep(61)
        asset = top_coin()
        df = last_data(asset, '1m', '120')
# переменная quantity для определения количества позиции
    qty = round(buy_amt/df.Close.iloc[-1], 1)
    if ((df.Close.pct_change() +1).cumprod()).iloc[-1] > 1:
        print(asset)
        print(df.Close.iloc[-1])
        print(qty)
# переменная для выставления ордера на покупку
        order = client.create_order(symbol=asset, side='BUY', type='MARKET', quantity = qty)
        print(order)
        buyprice = float(order['fills'][0]['price']) # цена входа
        open_position = True

        while open_position:
            try:
                df = last_data(asset, '1m', '2') # контролируем позицию каждые 2 минуты с интервалом в 1 минуту
            except:
                print('Restart after 1 min')
                time.sleep(61)
                df = last_data(asset, '1m', '2')

            print(f'Price ' + str(df.Close[-1]))
            print(f'Price ' + str(buyprice * Target)) # показываем цену которую мы ждем, исходя из Target
            print(f'Stop ' + str(buyprice * SL))
            if df.Close[-1] <= buyprice * SL or df.Close[-1] >= buyprice * Target:
                order = client.create_order(symbol=asset, side='SELL', type='MARKET', quantity=qty)
                print(order)
                break

    else:
        print('No find')
        time.sleep(20)
    while True:
        strategy(15) # 15 это объем покупок для стратегии 15 долларов, как пример
