# This scraper collects checks gets the order of best selling audiobooks on the Audible API every day

import requests
import scraperwiki
import simplejson

baseurl = "https://api.audible.com.au/1.0/catalog/products?response_groups=product_plans,rating,product_extended_attrs,contributors%2Cproduct_desc,product_attrs&num_results=50&products_sort_by=BestSellers&page="

page = 0
rank = 1
while True:
	results = requests.get(baseurl+str(page)).content
	jsonresults = simplejson.loads(results)
	print jsonresults
	if len(jsonresults['products']) == 0:
		break
	for product in jsonresults['products']:
		prod = {
				'rank': rank,
		 		'title': product['title'],
		 		'asin': product['asin'],
		 		'reviews': product['rating']['num_reviews'],
				'orating': product['rating']['overall_distribution']['average_rating'],
				'srating': product['rating']['story_distribution']['average_rating'],
				'prating': product['rating']['performance_distribution']['average_rating'],
		 		'issue_date': product['issue_date'],
		 		'release_date': product['release_date'],
			 	'copyright': product['copyright'],
		 		'runtime_length_min': product['runtime_length_min'],
			 	'format_type': product['format_type'],
				'publisher_name': product['publisher_name']
		}
		try:
			prod['publication_name'] = product['publication_name']
		except:
			pass
		print prod
		rank+=1
	page += 1
	if page > 10:
		break


#scraperwiki.sqlite.save(unique_keys=["name","club","year"],data=data,table_name='players')