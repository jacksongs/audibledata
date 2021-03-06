# This scraper collects checks gets the order of best selling audiobooks on the Audible API every day

import requests
import scraperwiki
import simplejson
import datetime

baseurl = "https://api.audible.com.au/1.0/catalog/products?response_groups=product_plans,rating,product_extended_attrs,contributors%2Cproduct_desc,product_attrs&num_results=50&products_sort_by=BestSellers&page="

page = 0
rank = 1
while True:
	results = requests.get(baseurl+str(page)).content
	jsonresults = simplejson.loads(results)
	if len(jsonresults['products']) == 0:
		break
	for product in jsonresults['products']:
		rankdata = {'rank': rank, 'asin':product['asin'],'when':datetime.datetime.now()}
		try:
			rankdata['reviews'] = product['rating']['num_reviews']
			rankdata['orating'] = product['rating']['overall_distribution']['average_rating']
			rankdata['srating'] = product['rating']['story_distribution']['average_rating']
			rankdata['prating'] = product['rating']['performance_distribution']['average_rating']
		except:
			pass
		prod = {
		 		'title': product['title'],
		 		'asin': product['asin']
		}
		try:
			prod['release_date'] = product['release_date']
		except:
			pass		
		try:
			prod['publisher_name'] = product['publisher_name']
		except:
			pass		
		try:
			prod['runtime_length_min'] = product['runtime_length_min']
		except:
			pass
		try:
			prod['issue_date'] = product['issue_date']
		except:
			pass
		try:
			prod['publication_name'] = product['publication_name']
		except:
			pass
		try:
			prod['format_type'] = product['format_type']
		except:
			pass
		try:
			prod['subtitle'] = product['subtitle']
		except:
			pass
		try:
			prod['copyright_en'] = product['copyright']['en']
		except:
			pass
		try:
			authors = []
			for author in product['authors']:
				try:
					authors.append(author['name'])
				except:
					pass
			prod['authors'] = ''.join(authors)
		except:
			pass
		try:
			narrators = []
			for narrator in product['narrators']:
				try:
					narrators.append(narrator['name'])
				except:
					pass
			prod['narrators'] = ''.join(narrators)
		except:
			pass
		rank+=1
		scraperwiki.sqlite.save(unique_keys=["asin"],data=prod,table_name='product')
		scraperwiki.sqlite.save(unique_keys=[],data=rankdata,table_name='rank')
	if rank > 1000:
		break
	page += 1
	
