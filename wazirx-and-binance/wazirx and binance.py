import os
try:import xlwings
except ImportError:os.system('python -m pip install xlwings')
try:import pandas
except ImportError:os.system('python -m pip install pandas')
try:import urllib3
except ImportError:os.system('python -m pip install urllib3')
try:import certifi
except ImportError:os.system('python -m pip install certifi')
import xlwings,pandas,urllib3,json,certifi,os
print('running.................')
wb = xlwings.Book('wazirx and binance.xlsx')
wrx = wb.sheets("wazirx")
bnb = wb.sheets('binance')
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
while True:
    data = pandas.read_json('https://api.binance.com/api/v1/ticker/allPrices')
    bnb.range('a1').options(pandas.DataFrame,index=False).value = pandas.DataFrame(data)
    r = http.request('GET', 'https://api.wazirx.com/api/v2/market-status')
    data = json.loads(r.data.decode())
    df1 = pandas.json_normalize(data, 'markets')
    wrx.range('a1').options(pandas.DataFrame,index=False).value = df1

