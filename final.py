import requests
import pandas as pd
from datetime import date
from bs4 import BeautifulSoup
import openpyxl
http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"
data ={'title': [],'change': [],'open':[],'high':[],'low':[], 'close': []}
current_value = {'date':[],'open':[],'high':[],'low':[], 'close': []}
self_data = {'title':[],'open':[],'high':[],'low':[], 'close': [],'quantity':[]}
date_= date.today().strftime("%Y-%m-%d")
proxies = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

url = "https://www.merolagani.com/LatestMarket.aspx"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

def extracter (rows):
    for row in rows:
        values = row.find_all('td',class_="text-right")
        prices=values[0]
        change = values[1]
        open = values[4]
        high= values[2]
        low = values [3]
        for price in prices:
            data["title"].append(row.td.a.string)
            data["open"].append(open.text)
            data["high"].append(high.text)
            data["low"].append(low.text)
            data["close"].append(price)
            data["change"].append(change.text)

def write():
    df = pd.DataFrame.from_dict(self_data)
    cf = pd.DataFrame.from_dict(current_value)

    workbook = openpyxl.load_workbook('data.xlsx')

    sheet1 = workbook['Sheet1']
    sheet2 = workbook['Sheet2']
    sheet1.delete_rows(2, sheet1.max_row)

    for row in df.itertuples(index=False, name=None):
        sheet1.append(row)
    for row in cf.itertuples(index=False, name=None):
        sheet2.append(row)

    workbook.save('data.xlsx')
    workbook.close()

def file_read():
    _df = pd.read_csv('data.csv')
    data = _df.to_dict(orient='list')
    r = len(data['S.N'])
    for i in range( 0,r-1):
        self_data['title'].append(data['Scrip'][i])
        self_data['open'].append(data['Value as of LTP'][i])
        self_data['high'].append(data['Value as of LTP'][i])
        self_data['low'].append(data['Value as of LTP'][i])
        self_data['close'].append(data['Value as of LTP'][i])
        self_data['quantity'].append(float(data['Current Balance'][i]))

    current_value['date'].append(date_)
    current_value['open'].append(data['Value as of LTP'][i+1])
    current_value['high'].append(data['Value as of LTP'][i+1])
    current_value['low'].append(data['Value as of LTP'][i+1])
    current_value['close'].append(data['Value as of LTP'][i+1])
    write()

def portfolio():
    while True:
        choice = input("Enter what stocks you've got? (y/n): ")
        if choice.lower() == 'n':
            break
        key = input('names')
        sn= data['title'].index(key.upper())
        self_data['title'].append(data['title'][sn])
        quantity = input("quantity")
        open_total = float(data['open'][sn].replace(",", ""))
        high_total = float(data['high'][sn].replace(",", ""))
        low_total = float(data['low'][sn].replace(",", ""))
        close_total = float(data['close'][sn].replace(",", ""))
        self_data['quantity'].append(quantity)
        self_data['open'].append(int(quantity)*open_total)
        self_data['high'].append(int(quantity)*high_total)
        self_data['low'].append(int(quantity)*low_total)
        self_data['close'].append(int(quantity)*close_total)
        print("Continuing...")
    write()

incr_row=soup.find_all('tr',class_="increase-row")
dcr_row=soup.find_all('tr',class_="decrease-row")
nochange_row=soup.find_all('tr',class_="nochange-row")
extracter(incr_row)
extracter(dcr_row)
extracter(nochange_row) 
entry = input("Enter what stocks you've got yourself? (y/n) or load using a file?(l): ")
if entry.lower() == 'y':
    portfolio()
if entry.lower() == 'l':
    file_read()
else:
    pass


