from selenium import webdriver
import json
import time
from bs4 import BeautifulSoup
from csv import writer 

driver = webdriver.Firefox(executable_path="/home/intel123/geckodriver")
 
samsung = phone("Samsung","https://www.amazon.com/s?k=samsung+phones&rh=n%3A2407748011&ref=nb_sb_noss",'a-size-medium a-color-base a-text-normal')

category = "mobile"
with open('amazon.csv','a') as fd :
	writer_obj = writer(fd)
	entry = [category]
	driver.get(phone.url)
	time.sleep(5)
	source = driver.page_source
	soup = BeautifulSoup(source,'lxml')
	links = soup.find_all('a',{'class':'a-link-normal a-text-normal'})
	product_urls = {}
	for l in links :
		entry = [category]
		prod_name = l.find('span',{'class':phone.prod_span_class}).text.strip()
			prod_url = "https://www.amazon.com"+l.get('href')
			entry.extend([prod_name, prod_url])
			driver.get(prod_url)
			source = driver.page_source
			soup = BeautifulSoup(source,'lxml')
			title = soup.find('span', {'id':'productTitle'}).text.strip()
			if(title != prod_name) :
				print("Mismatch")
			features = {}
			table = soup.find('table',{'class':'a-normal a-spacing-micro'})
			for row in table.find_all('tr') :
				feature, value = row.find_all('td')
				features[feature.text.strip()] = value.text.strip()
			table = soup.find('table',{'id':'productDetails_detailBullets_sections1'})
			for row in table.find_all('tr') :
				feature = row.find('th',{'class':'a-color-secondary a-size-base prodDetSectionEntry'}).text.strip()
				value = row.find('td').text.strip()
				features[feature] = value
			entry.append(features)
			writer_obj.writerow(entry)
	fd.close()

