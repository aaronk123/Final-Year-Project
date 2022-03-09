from urllib.request import urlopen
import pandas as pd
import re
from bs4 import BeautifulSoup
import requests
import ssl
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def check_date():
    context = ssl._create_unverified_context()

    res=urlopen('https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPRDownloads?OpenForm', context=context)
    # URL = 'https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPRDownloads?OpenForm'
    # header = {'User-Agent': 'Mozilla/5.0'}
    # page = requests.get(URL, headers = header)
    soup = BeautifulSoup(res, 'html.parser')
    #print(soup)
    date = soup.find('span', id='LastUpdated')
    #print(date.text)

    date=date.text
    date_list=[]
    date_list.append(date)

    df = pd.DataFrame(date_list)
    df.to_csv('ppr date.csv')

def downloader():

    driver = webdriver.Chrome('chromedriver.exe')
    #driver.get('https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPRDownloads?OpenForm')
    #driver.get('https://www.propertypriceregister.ie/website/npsra/pprweb.nsf/PPRDownloads?OpenForm&File=PPR-2022.csv&County=ALL&Year=2022&Month=ALL')

    driver.get('https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-2021.csv/$FILE/PPR-2021.csv')

    actions=ActionChains(driver)
    #time.sleep(3)
    #driver.find_elements_by_class_name('boldbuttons')[0].click()
    # driver.find_element_by_xpath('//input[@value=" CLICK HERE TO DOWNLOAD THE FILE "]').click()
    # time.sleep(2)

downloader()
