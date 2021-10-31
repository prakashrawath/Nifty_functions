import requests
import time
from datetime import datetime
from nsetools import Nse
import matplotlib.animation as animation
import matplotlib.pyplot as plt


def adv_dec_print():
 nse = Nse()
 adv_dec = nse.get_advances_declines()
 valid = {'NIFTY 50', 'NIFTY IT', 'NIFTY BANK'}
 for list in adv_dec:
  if list['indice'] in valid:
   print(list)

def weightage():

 baseurl = "https://www1.nseindia.com/"
 url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
 # url = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
 headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
 'like Gecko) '
 'Chrome/80.0.3987.149 Safari/537.36',
 'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
 session = requests.Session()
 request = session.get(baseurl, headers=headers, timeout=5)
 cookies = dict(request.cookies)
 response = session.get(url, headers=headers, timeout=5, cookies=cookies)
 nse_data = response.json()['data']
 nifty50_stocks = [
 {'name': 'RELIANCE', 'weight': '10.66'},
 {'name': 'HDFCBANK', 'weight': '9.13'},
 {'name': 'INFY', 'weight': '8.13'},
 {'name': 'HDFC', 'weight': '6.50'},
 {'name': 'ICICIBANK', 'weight': '6.36'},
 {'name': 'TCS', 'weight': '5.12'},
 {'name': 'KOTAKBANK', 'weight': '3.85'},
 {'name': 'HINDUNILVR', 'weight': '3.16'},
 {'name': 'AXISBANK', 'weight': '2.70'},
 {'name': 'LT', 'weight': '2.69'},
 {'name': 'TITAN', 'weight': '1.12'},
 {'name': 'BAJAJFINSV', 'weight': '1.32'},
 {'name': 'BAJAJ-AUTO', 'weight': '0.65'},
 {'name': 'SBIN', 'weight': '2.30'},
 {'name': 'HEROMOTOCO', 'weight': '0.51'},
 {'name': 'HINDALCO', 'weight': '0.91'},
 {'name': 'NESTLEIND', 'weight': '0.93'},
 {'name': 'TATAMOTORS', 'weight': '0.71'},
 {'name': 'TATASTEEL', 'weight': '1.41'},
 {'name': 'ITC', 'weight': '2.58'},
 {'name': 'EICHERMOT', 'weight': '0.50'},
 {'name': 'INDUSINDBK', 'weight': '0.87'},
 {'name': 'BAJFINANCE', 'weight': '2.66'},
 {'name': 'JSWSTEEL', 'weight': '0.85'},
 {'name': 'HINDUNILVR', 'weight': '3.16'},
 {'name': 'BRITANNIA', 'weight': '0.54'},
 {'name': 'SBILIFE', 'weight': '0.64'},
 {'name': 'WIPRO', 'weight': '1.28'},
 {'name': 'ASIANPAINT', 'weight': '1.91'},
 {'name': 'DIVISLAB', 'weight': '0.83'},
 {'name': 'UPL', 'weight': '0.51'},
 {'name': 'HDFC', 'weight': '9.13'},
 {'name': 'TATACONSUM', 'weight': '0.61'},
 {'name': 'CIPLA', 'weight': '0.65'},
 {'name': 'BPCL', 'weight': '0.69'},
 {'name': 'MARUTI', 'weight': '1.23'},
 {'name': 'NTPC', 'weight': '0.88'},
 {'name': 'POWERGRID', 'weight': '0.88'},
 {'name': 'DRREDDY', 'weight': '0.88'},
 {'name': 'BHARTIARTL', 'weight': '2.13'},
 {'name': 'ADANIPORTS', 'weight': '0.70'},
 {'name': 'SUNPHARMA', 'weight': '1.12'},
 {'name': 'IOC', 'weight': '0.42'},
 {'name': 'GRASIM', 'weight': '0.78'},
 {'name': 'SHREECEM', 'weight': '0.48'},
 {'name': 'ONGC', 'weight': '0.78'},
 {'name': 'M&M', 'weight': '1.01'},
 {'name': 'ULTRACEMCO', 'weight': '1.16'},
 {'name': 'COALINDIA', 'weight': '0.51'},
 {'name': 'HDFCLIFE', 'weight': '0.80'},
 {'name': 'TECHM', 'weight': '1.18'},
 {'name': 'HCLTECH', 'weight': '1.82'},
 ]

 change_from_open = 0
 weightage = 0

 for symbol in nse_data:
  for stock in nifty50_stocks:
   if stock['name'] == symbol['symbol']:
    scrip = symbol['symbol']
    open = symbol['open'].replace(',', '')
    ltp = symbol['ltP'].replace(',', '')
    change = float(ltp) - float(open)
    stock_weightage = float(stock['weight'])
    change_from_open += change
    individual_weightage = float(stock_weightage) * change
    weightage += individual_weightage
    # print(weightage)
    # print(scrip, open , ltp, change, individual_weightage)
 print(datetime.now(), int(change_from_open), int(weightage) / 100)
 return int(weightage) / 100

def animate(i, xs, ys):
 adv_dec_print()
 result = weightage()
 ctime = time.strftime("%H%M%S")

 # Add x and y to lists
 xs.append(ctime)
 ys.append(result)

 # Draw x and y lists
 ax.clear()
 ax.plot(xs, ys)

 # Format plot
 plt.xticks(rotation=45, ha='right')
 plt.subplots_adjust(bottom=0.30)
 plt.title('Weightage graph - updates every 3 minutes')
 plt.ylabel('Weightage')
 plt.xlabel('Time')

# plt.xlabel('Time')
# plt.ylabel('Weightage')
# plt.title('Weightage graph - updates every 3 minutes')

# while True:
# adv_dec_print()
# result = weightage()
# ctime = time.strftime("%H%M%S")
# plt.scatter(ctime, result)
# plt.pause(2)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=150000)
plt.show()