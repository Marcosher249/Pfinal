import sys
import ccxt as c
import pandas as pd
import asyncio


class Grafica:

    def __init__(self, moneda):
        self.moneda = moneda

    async def tabla(self):
        datos = await self.dataframe()
        tabla = pd.DataFrame(datos, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        tabla['Date'] = pd.to_datetime(tabla['Date'], unit='ms')
        tabla = tabla.set_index('Date')
        tabla.index = tabla.index.tz_localize('UTC').tz_convert('Europe/Madrid')
        tabla.index = tabla.index.strftime('%Y-%m-%d %H:%M:%S')
        print(f"se ejecuta"+self.moneda)
        return tabla

    async def dataframe(self):
        
        try:
            kuco = c.kucoin()
            datos = kuco.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:
            print(f'error en kucoin' + str(e))
        try:
            binan = c.binance()
            datos = binan.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:       
            print('error en binance' + str(e))
        try:
            coin = c.coinbase()
            datos = coin.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:
            print('error en coinbase' + str(e))
        try:
            coin = c.ace()
            datos = coin.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:
            print('error en ace' + str(e))
        try:
            coin = c.alpaca()
            datos = coin.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:
            print('error en alpaca' + str(e))
        try:
            coin = c.ascendex()
            datos = coin.fetch_ohlcv(self.moneda, timeframe='1m', limit=500)
            return datos
        except Exception as e:
            print('error en ascendex' + str(e))
        return datos

if __name__ == '__main__':
    tabla = Grafica('BTC/USDT')
    datos = asyncio.run(tabla.tabla())
    print(datos)