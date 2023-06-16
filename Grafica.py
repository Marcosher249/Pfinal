import ccxt as c
import pandas as pd
import asyncio






async def tabla(moneda):
    datos = await dataframe(moneda)
    tabla = pd.DataFrame(datos, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    tabla['Date'] = pd.to_datetime(tabla['Date'], unit='ms')
    tabla = tabla.set_index('Date')
    tabla.index = tabla.index.tz_localize('UTC').tz_convert('Europe/Madrid')
    tabla.index = tabla.index.strftime('%Y-%m-%d %H:%M:%S')

    if moneda == "BTC/USDT":
        tabla.to_csv('csv/datos_btc.csv')
    elif moneda == "ETH/USDT":
        tabla.to_csv('csv/datos_eth.csv')
    elif moneda == "BNB/USDT":
        tabla.to_csv('csv/datos_bnb.csv')
    else:
        tabla.to_csv('csv/datos_usdc.csv')

    

async def dataframe(moneda):
        
    try:
        kuco = c.kucoin()
        datos = kuco.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:
        print(f'error en kucoin' + str(e))
    try:
        binan = c.binance()
        datos = binan.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:       
        print('error en binance' + str(e))
    try:
        coin = c.coinbase()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:
        print('error en coinbase' + str(e))
    try:
        coin = c.ace()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:
        print('error en ace' + str(e))
    try:
        coin = c.alpaca()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:
        print('error en alpaca' + str(e))
    try:
        coin = c.ascendex()
        datos = coin.fetch_ohlcv(moneda, timeframe='1m', limit=500)
        return datos
    except Exception as e:
        print('error en ascendex' + str(e))
        return datos
async def datos_graficas():
    while True:
        monedas = ["BTC/USDT","ETH/USDT","BNB/USDT","USDC/USDT"]
        tasks = [tabla(moneda) for moneda in monedas]
        await asyncio.gather(*tasks)
        await asyncio.sleep(30)

    

if __name__ == '__main__':
    asyncio.run(datos_graficas())
    