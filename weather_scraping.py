#scrape the weather.com website

import requests
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pprint
import selenium

url = requests.get("https://weather.com/weather/today/l/7394a793971a4a7345c791564765f9b3ab107c83a0dfcc6d326b9684cac9c86d")
url.raise_for_status()
bs = soup(url.text, "html.parser")

city = bs.find("h1", {"class": "CurrentConditions--location--kyTeL"})
pprint.pprint(city.get_text())
time_of = bs.find("div", {"class": "CurrentConditions--timestamp--23dfw"})
pprint.pprint(time_of.get_text())
temperature = bs.find("span", {"class": "CurrentConditions--tempValue--3a50n"})
print(temperature.get_text())



