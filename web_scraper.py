import requests
from bs4 import BeautifulSoup

keyword= 'color pencils'
results = []
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

for i in range(1,11):
    r = requests.get('https://www.ebay.com/sch/i.html?_nkw='+keyword+'&_pgn='+str(i),headers=headers)
    #print('r.stsus_code=',r.status_code)
    soup = BeautifulSoup(r.text,'html.parser')

    #print('r.text=',r.text)
    # extract items from the boxes
    boxes = soup.select('li.s-item > .clearfix.s-item__wrapper')
    for box in boxes:
        #print('---')
        result = {}
        titles = box.select('.s-item__title')
        for title in titles: 
            #print('Name of item=',title.text)
            result['Name of item'] = title.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('Price=',price.text)
            result['Price'] = price.text
        statuses = box.select('.s-item__subtitle')
        for status in statuses: 
            #print('Status=',status.text)
            result['Status'] = status.text
        #print('result=',result)
        results.append(result)
    print('len(results)=',len(results))

import json
j = json.dumps(results)
with open('items.json','w') as f:
    f.write(j)
