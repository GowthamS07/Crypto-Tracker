# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:20:35 2021

@author: Gowtham S
"""
from selenium import webdriver
from notify_run import Notify
import requests
from bs4 import BeautifulSoup as bs
import time
from urllib.request import urlopen

notify = Notify()

driver_path = r"D:\Projects\Fun project\bitcoin_tracker_with_notification\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

def fetch_price(coin):
	try:
		option = webdriver.ChromeOptions()
		option.binary_location = brave_path
		option.headless = True
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
		driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
		driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"python 3.6.9", "platform":"Windows"})
		url_link = "https://coindcx.com/trade/"+coin+"INR"
		driver.get(url_link)
#driver.get("https://wazirx.com/exchange/DOGE-INR")
		content = driver.page_source
		agent = driver.execute_script("return navigator.userAgent")
		soup = bs(content)
		coin_price = soup.find("span", {"class": "latest-trade-price"}).get_text(strip=True)
		return coin_price
	except:
		notify.send("Error With Fetching prices pls check the app")

def main():
	while True:
		bch_price = fetch_price('BCH')
		doge_price = fetch_price('DOGE')
		notify.send("BCH: "+bch_price+"\nDoge: "+doge_price)
		time.sleep(1800)

main()
