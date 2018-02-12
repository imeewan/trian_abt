#plot readl time rate for tri amgular arbitrage

# 1st trial usd ==> btc ==> eth ==> usd
# run over 2000 cycles
#over line at y=0 is the point you can make profit

import gdax
import matplotlib.pyplot as plt
import time
import numpy as np

public_client = gdax.PublicClient()

fee1 = 0.9995
fee2 = 0.9995

profits = []

for i in range(2000):
    btc_usd = public_client.get_product_order_book('BTC-USD')
    eth_btc = public_client.get_product_order_book('ETH-BTC')
    eth_usd = public_client.get_product_order_book('ETH-USD')
    
    usd2btc = float(btc_usd['asks'][0][0])
    btc2eth = float(eth_btc['asks'][0][0])
    eth2usd = float(eth_usd['bids'][0][0])
    
    profit = (1 / usd2btc * fee1 / btc2eth * fee2 * eth2usd * fee2) - 1
    profits.append(profit)

    print(i, profit)    
    time.sleep(0.3)

y = np.zeros(i)
x = np.array(profits)
plt.plot(x)
plt.plot(y)
plt.show()

# trial 2  btc ==> ltc ==> usd ==> btc

public_client = gdax.PublicClient()
fee1 = 0.9975
fee2 = 0.997
profits = []

for i in range(1000):
    ltc_btc = public_client.get_product_order_book('LTC-BTC')
    ltc_usd = public_client.get_product_order_book('LTC-USD')
    btc_usd = public_client.get_product_order_book('BTC-USD')

    btc2lth = float(ltc_btc['asks'][0][0])    
    ltc2usd = float(ltc_usd['bids'][0][0])
    usd2btc = float(btc_usd['asks'][0][0])
    
    profit = (1 / btc2lth * fee2 * ltc2usd * fee2 / usd2btc * fee1) - 1
    print(i, profit)
    profits.append(profit)
    
    time.sleep(1)
    
y = np.zeros(i)
x = np.array(profits)
plt.plot(x)
plt.plot(y)

plt.show()





from binance.client import BinanceRESTAPI, BinanceWebSocketAPI

prices = rest_client.all_prices()

rest_client.ping()


#web socket
prices = []
j = 0
while True:
    btc_usd = public_client.get_product_order_book('BTC-USD')
    print_time = 100
    btc_usd = public_client.get_product_order_book('BTC-USD')
    usd2btc = float(btc_usd['asks'][0][0])
    prices.append(usd2btc)
    j += 1
    if j % print_time == 0:
        z = np.array(prices)
        plt.plot(z)
        plt.show()
        
    time.sleep(0.3)



























