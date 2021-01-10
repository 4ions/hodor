#!/usr/bin/python3
import requests
import multiprocessing
""" Web scraping: Program that votes 1024 times """


params = {'id': '2158', 'holdthedoor': 'submit'}
url = 'http://158.69.76.135/level0.php'

def post(finish):
    """ send vote to page """
    count = 0
    while count < finish:
        response  = requests.post(url, data = params)
        count += 1
        print(count)

def multi():
    """ Generate the multiprocess """
    finish = 32
    p = multiprocessing.Process(target=post, args=(finish,))
    return(p)

def process():
    """ Start the program """
    inprocess = []
    for i in range(32):
        inprocess.append(multi())
        inprocess[i].start()
    for i in inprocess:
        i.join()
    print("termine")
        

if __name__ == "__main__":
    process()
