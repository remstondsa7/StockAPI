# -*- coding: utf-8 -*-

#pip install alpha_vantage

#pip install mplfinance

def timeSeries(API_key='Z6P4MY41TAIKFAXW', ticker="MSFT"):
  print("########PROCESSING#########")
  from alpha_vantage.timeseries import TimeSeries
  import matplotlib.pyplot as plt
  import mplfinance as mpf
  ts=TimeSeries(key=API_key, output_format='pandas')
  data=ts.get_daily_adjusted(symbol=ticker)[0]
  data.columns = ['Open', 'High', 'Low', 'Close', 'Adjusted_close','Volume','Dividend Amount','Split Coefficient']
  data.index.name = "Date"
  mpf.plot(data,
            type='candle', 
            title=f'Daily Time series for the {ticker} stock',
            mav=(20), 
            volume=True, 
            tight_layout=True,
            style='yahoo')
  return data



def cryptocurrency(API_key='Z6P4MY41TAIKFAXW', currency="BTC"):
  print("########PROCESSING#########")
  from alpha_vantage.cryptocurrencies import CryptoCurrencies
  import matplotlib.pyplot as plt
  import mplfinance as mpf

  cc=CryptoCurrencies(key=API_key,output_format='pandas')
  data=cc.get_digital_currency_daily(symbol=currency, market='INR')[0]

  data.columns = ['Open','_Open','High','_High','Low','_Low','Close','_Close','Volume','Market Cap']
  data.index.name = "Date"
  mpf.plot(data,
          type='candle', 
          title=f'Daily Time series for the {currency} cryptocurrency',
          mav=(20), 
          volume=True, 
          tight_layout=True,
          style='yahoo')
  return data



def forex(API_key='Z6P4MY41TAIKFAXW', fromCurr='INR', toCurr='USD'):
  print("########PROCESSING#########")
  from alpha_vantage.foreignexchange import ForeignExchange
  import matplotlib.pyplot as plt
  import mplfinance as mpf

  fe=ForeignExchange(key=API_key,output_format='pandas')
  data=fe.get_currency_exchange_daily(from_symbol=fromCurr, to_symbol=toCurr)[0]
  data.columns = ['Open', 'High', 'Low', 'Close']
  data.index.name = "Date"
  mpf.plot(data,
          type='candle', 
          title=f'Daily FOREX for the {fromCurr} against {toCurr} currency',
          mav=(20), 
          tight_layout=True,
          style='yahoo')
  return data



def sectorPerformance(API_key='Z6P4MY41TAIKFAXW'):
  print("########PROCESSING#########")
  from alpha_vantage.sectorperformance import SectorPerformances
  import matplotlib.pyplot as plt
  import mplfinance as mpf

  sp=SectorPerformances(key=API_key, output_format='pandas')
  data=sp.get_sector()[0]
  data['Rank A: Real-Time Performance'].plot(kind='bar')
  plt.title('Real Time Performance (%) per sector')
  plt.tight_layout()
  plt.grid()
  plt.show()
  return data



if __name__=='__main__':
  timeSeries(API_key='Z6P4MY41TAIKFAXW', ticker=input('Enter Ticker:\n'))
  
  cryptocurrency(API_key='Z6P4MY41TAIKFAXW', currency=input('Enter Crypto Currency:\n'))

  forex(API_key='Z6P4MY41TAIKFAXW', fromCurr=input('Enter currency for Forex:\n'), toCurr='INR')

  sectorPerformance(API_key='Z6P4MY41TAIKFAXW')
  print("########DONE#########")
  
