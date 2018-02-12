#plot readl time rate for tri amgular arbitrage

# trial 2  btc ==> ltc ==> usd ==> btc
# 2000 cycles
# over the line is the point that you can make profit

public_client = gdax.PublicClient()
fee1 = 0.9975
fee2 = 0.997
profits = []

for i in range(2000):
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


