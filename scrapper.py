from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import numpy as np
#import asyncio

# Start
# Get the website using the Chrome webdriver
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-minimize")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Analyze user input and decide what to return
def get_good_reports(page_num):
    symbols = []
    percents = []
    good_report = []
    bad_report = []
    
    print("Obtaining data...")
    browser.get("https://finance.yahoo.com/calendar/earnings?from=2022-11-06&to=2022-11-12&day=2022-11-07&offset=" + str(page_num) + "00&size=100")
    #Get earnings data
    raw_symbols = browser.find_elements(By.XPATH, "//tr/td[1]")
    if not raw_symbols:
        return "end"
    
    for sym in raw_symbols:
        symbols.append(sym.text)
    raw_percents = browser.find_elements(By.XPATH, "//tr/td[7]")
    
    for pcent in raw_percents:
        percents.append(pcent.text)

    for x in range(len(percents)):
        if "+" in percents[x]:
            good_report.append(symbols[x])
    if not good_report: 
        print("0 positive earnings found")
        return "none"
    else:
        print(str(len(good_report)) + " positive earnings found")         
        return good_report