import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from bs4 import BeautifulSoup

my_url = "https://www.nasdaq.com/symbol/aapl/historical"

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "genTable"})

for container in containers:
	rs_container = container.findAll("tbody",)
	for each in rs_container:
		fff = each.findAll("td",)
		status = True
		da_nu = 0
		price_nu = 4
		print ("Date", " | ", "Close/Last")
		while status:
			try:
				print (fff[da_nu].text.strip(), " | ", fff[price_nu].text.strip(), "\n")
			except:
				break;
			da_nu += 6
			price_nu += 6

	# date = rs_container[0].th.text
	# close_price = rs_container[4].tbody.text
	
	# # print (date, close_price)
	# for each in close_price:
	# 	print (each)


	# print (each)
	# for ea in each.table.tbody.tr:
	# 	print (ea, "11111")

# conatin = containers[0]

# container = containers[0]

# # print (container.table.tbody.tr)
# for each in container.table.tbody.tr:
# 	print (each.td)
# # print (container.table.tbody.tr[1])


# def apple(n):
# 	page = requests.get(n)
# 	soup = BeautifulSoup(page.content, 'html.parser')
# 	print(soup.prettify())
# 	import pdb;pdb.set_trace();
# 	return (soup)


# # data = input("Enter website url")
# data = "https://www.nasdaq.com/symbol/aapl/historical"
# apple(data)