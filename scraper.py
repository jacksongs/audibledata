# This scraper collects checks gets the order of best selling audiobooks on the Audible API every day

import requests
import scraperwiki
import simplejson

baseurl = "https://api.audible.com.au/1.0/catalog/products?response_groups=product_plans,rating,product_extended_attrs,product_attrs&num_results=5&products_sort_by=BestSellers&page="

page = 0
while True:
	results = requests.get(baseurl+str(page)).content
	jsonresults = simplejson.loads(results)
	print jsonresults
	if len(jsonresults['products']) == 0:
		break
	for product in jsonresults['products']:
		print product['asin']
		print product['rating']
		print product['issue_date']
		print product['release_date']
		print product['copyright']
		print product.keys()
	page += 1
	if page > 10:
		break


#scraperwiki.sqlite.save(unique_keys=["name","club","year"],data=data,table_name='players')