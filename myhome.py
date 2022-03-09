import re
from bs4 import BeautifulSoup
import requests

URL = 'https://www.myhome.ie/residential/brochure/4-ardcahon-way-coolkellure-lehenaghmore-cork/4543070'
header = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(URL, headers = header)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
details = soup.find('div', class_='PropertyDetails__DescriptionContent')
print(details)