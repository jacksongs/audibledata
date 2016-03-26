# This scraper collects checks gets the order of best selling audiobooks on the Audible API every day

import requests
import scraperwiki
import simplejson

baseurl = "https://api.audible.com.au/1.0/catalog/products?response_groups=rating,product_extended_attrs&num_results=50&products_sort_by=BestSellers&page="

page = 0
while True:
	results = requests.get(baseurl).content
	jsonresults = simplejson.loads(results)
	if len(jsonresults['products']) == 0:
		break
	for product in jsonresults['products']:
		print product
	page += 1
	if page > 10:
		break


#scraperwiki.sqlite.save(unique_keys=["name","club","year"],data=data,table_name='players')