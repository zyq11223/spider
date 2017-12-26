import logging
from bs4 import BeautifulSoup
import requests
import os

def test1():
    url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&Mozilla%2F6.0+%28Macintosh%3B+U%3B+PPC+Mac+OS+X+Mach-O%3B+en-US%3B+rv%3A2.0.0.0%29+Gecko%2F20061028+Firefox%2F3.0=&_nkw=camera&rt=nc&LH_Auction=1"
    response_html = requests.get(url)
    soup = BeautifulSoup(response_html.text, "html.parser")
    internal = "| eBay"
    if internal in soup.title.string:
        print internal, "is in ", soup.title.string
    else:
        print internal, "is not in ", soup.title.string

def test_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(module)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y %b %d %H:%M:%S',
                        filename='app.Log',
                        filemode='w')
    i = 1
    url = "http://ww.bvai.com"
    logging.info("Handle the" + str(i) + "th URL" + url)

if __name__ == '__main__':
    # test1()
    test_logging()