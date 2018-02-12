# real time plot BTC-USD

import gdax
import matplotlib.pyplot as plt
import time
import numpy as np

public_client = gdax.PublicClient()

#plot every 100 cycles
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



























