#scrape the weather.com website

from bs4 import BeautifulSoup as soup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#Using Selenium without launching the browser (headless).
chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

search = input("Please enter your City or Zip Code: ")

#Webdriver will navigate to weather.com, click the search bar, and enter the users input.
url = driver.get('https://weather.com/')
time.sleep(2)
driver.find_element_by_id('LocationSearch_input').click()
driver.find_element_by_id('LocationSearch_input').send_keys(search)
time.sleep(2)
driver.find_element_by_id('LocationSearch_input').send_keys(Keys.RETURN)
time.sleep(2)
print("")
print("")

#Access page content with Beautiful soup.
page = driver.page_source
bs = soup(page, "html.parser")

time.sleep(3)

#Soup will scape the page that Selenium navigates too
city = bs.find("h1", {"class": "CurrentConditions--location--kyTeL"})
print(city.text)
tod = bs.find("span", {"class": "CurrentConditions--timestamp--23dfw"})
print(tod.text)
temp = bs.find("span", {"class": "CurrentConditions--tempValue--3a50n"})
print(temp.text)

    
driver.close()
