import requests
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from bs4 import BeautifulSoup

my_url = "https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-post-category-touchdowns"

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

# print(page_soup)

containers = page_soup.findAll("div", {"id": "sortableContent"})

for container in containers:
	rs_container = container.findAll("tr",)
	player_num = 3
	team_num = 3
	status = True
	print ("PLAYER", " | ", "POS", " | ", "TEAM", " | ", "TD")
	while status:
		try:
			print (rs_container[player_num].findAll("td")[0].text, " | ", rs_container[player_num].findAll("td")[1].text, " | ", rs_container[player_num].findAll("td")[2].text, " | ", rs_container[player_num].findAll("td")[6].text)
			player_num += 1
		except:
			status = False
			break;