from celery import task
from news_scraper.models import *
from news_scraper.scraper_functions import *

@task()
def scrape_task():
	try:
		ET_scraper()
	except:
		pass
	try:
		BS_scraper()
	except:
		pass
	try:		
		FE_scraper()
	except:
		pass

@task()
def index_scrape_task():
	try:
		index_scrape()
	except:
		pass