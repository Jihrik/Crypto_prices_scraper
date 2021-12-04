import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.binance.com/cs/markets/coinInfo")
soup = BeautifulSoup(page.content, 'html.parser')

crypto = soup.find(class_='css-1vuj9rf')
crypto_names_div = crypto.find_all(class_='css-1ap5wc6')
crypto_symbols_div = crypto.find_all(class_='css-1wp9rgv')
crypto_prices_div = crypto.find_all(class_='css-ovtrou')
crypto_prices_change_div = crypto.find_all(class_='css-18yakpx')

# Get Crypto name
crypto_names = []
for name in crypto_names_div:
    crypto_names.append(name.get_text())

# get crypto symbols
crypto_symbols = []
for symbol in crypto_symbols_div:
    crypto_symbols.append(symbol.get_text())

# get crypto price
crypto_prices = []
for price in crypto_prices_div:
    crypto_prices.append(price.get_text())

# get crypto price change (24 hour)
crypto_prices_24_h_change = []
for change in crypto_prices_change_div:
    change_text = str(change.get_text())
    if change_text[0] == '+' or change_text[0] == '-':
        crypto_prices_24_h_change.append(change.get_text())

# data frame
datetime_object = datetime.datetime.now().isoformat(timespec='minutes', sep='T').replace("T", " ")
print(datetime_object)


data = {'Symbol': crypto_symbols, "name": crypto_names, "Price": crypto_prices, "Change": crypto_prices_24_h_change,
        "Time": datetime_object}
df = pd.DataFrame(data)
df.to_csv('file.csv')
print(df)
