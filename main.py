#!/usr/bin/python
# -*- coding: iso-8859-15 -*-			# fuer Umlaute

import requests
import time		
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Goodbox-Nickerchen-Werkzeuge-Unbreakable-Dekompression/dp/B07D1NKG5Z/ref=sr_1_2?__mk_de_DE=ÅMÅŽÕÑ&crid=28US32S7GQMO9&keywords=big+enter+button&qid=1563047683&s=gateway&sprefix=big+enter+%2Caps%2C149&sr=8-2'		#amazon link to product
		#Sonderzeichen entfernen

headers = {"User-Agent" : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.70'}

webpage = requests.get(URL, headers = headers)

soup = BeautifulSoup(webpage.content, 'html.parser')

title = soup.find(id = "productTitle").get_text()
title = title.strip()

price = soup.find(id = "priceblock_ourprice").get_text()
price = price[0:5]


print(title)
print(price)
