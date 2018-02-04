from .models import *
from bs4 import BeautifulSoup
from requests import get

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def ET_scraper():
	page = get('http://economictimes.indiatimes.com/markets/stocks/news', headers=hdr)
	soupy_page = BeautifulSoup(page.content, 'html.parser')
	all_meta = soupy_page.find_all("meta")
	for meta in all_meta:
		if(meta.get('itemprop') == 'name'):
			content = meta.get('content')
			if(content.find('Latest Stocks in News') == 0):
				continue
			try:
				Headline.objects.get(text=content)
			except self.model.does:
				HeadlineEntry = Headline()
				HeadlineEntry.publish(content)

def BS_scraper():
	page = get('http://www.business-standard.com/category/markets-news-1060101.htm', headers=hdr)
	soupy_page = BeautifulSoup(page.content, 'html.parser')
	all_divs = soupy_page.find_all("div", class_="listing-txt")
	for div in all_divs:
		for string in div.contents[3].strings:
			try:
				Headline.objects.get(text=string)
			except:
				HeadlineEntry = Headline()
				HeadlineEntry.publish(string)

def FE_scraper():
	page = get('http://www.financialexpress.com/market/', headers=hdr)
	soupy_page = BeautifulSoup(page.content, 'html.parser')
	all_h5s = soupy_page.find_all('h5')
	for h5 in all_h5s[1:]:
		for string in h5.strings:
			try:
				Headline.objects.get(text=string)
			except:
				HeadlineEntry = Headline()
				HeadlineEntry.publish(string)

def index_scrape():
	page = get('https://economictimes.indiatimes.com/indices/nifty_50_companies', headers=hdr)
	soupy_page = BeautifulSoup(page.content, 'html.parser')
	price = soupy_page.find("div", id="")
	for string in price.strings:
		IndexEntry = index_value()
		IndexEntry.publish(float(string))
