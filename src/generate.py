from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import time
crypto=[]
price=[]
ch24=[]
ch7=[]
links=[]
# lst=[name for name in input("enter crypto name:").split(" ")]
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'1000',
    'convert':'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'api_key',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    dataf=json.dumps(data,indent=2)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
data.pop("status")

#print(json.dumps(data["data"][0],indent=2))
#money=json.dumps(data["data"][0]["quote"]["USD"],indent=2)
#print(money)

def generate(name):
    ret=[]
    for i in range(len(data["data"])):
        cname=json.dumps(data["data"][i]["name"],indent=2)
        #print(json.dumps(data["data"][i].pop("name"),indent=2))
        #print(json.dumps(data["data"][i].pop("USD"),indent=2))
        cnamef=cname[1:-1].lower()
        price1=json.dumps(data["data"][i]["quote"]["USD"]["price"],indent=2)
        perc_change24=json.dumps(data["data"][i]["quote"]["USD"]["percent_change_24h"],indent=2)
        perc_change7=json.dumps(data["data"][i]["quote"]["USD"]["percent_change_7d"],indent=2)
        if cnamef.lower() == name:
            ret.append(cnamef)
            ret.append(price1)
            ret.append(perc_change24)
            ret.append(perc_change7)
            break;
                # crypto.append(cnamef)
                # price.append(price1)
                # ch24.append(perc_change24)
                # ch7.append(perc_change7)
    if len(ret)==0:
        ret.append("none")
    return ret
# filec=pd.DataFrame({'name':crypto,'price':price,'pc_24h':ch24,'pc_7d':ch7})
# filec.to_csv(f'crypto{c}.csv',index=True,encoding='utf-8')
# crypto=[]
# price=[]
# ch24=[]
# ch7=[]
# c=c-1
# time.sleep(15)
    
