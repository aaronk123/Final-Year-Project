import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization
import re
from bs4 import BeautifulSoup
import requests

def daft_scraper():
    daft = Daft()

    #daft.set_location("Cork City")
    daft.set_search_type(SearchType.RESIDENTIAL_SALE)
    daft.set_min_price(1000)
    daft.set_max_price(1000000)

    listings = daft.search()

    # for listing in listings:
    #     print(f'{listing.title}')
    #     print(f'{listing.daft_link}')
    #     print(f'{listing.price}')
    #     # print(f'{listing.distance_to(dublin_castle_coords):.3}km')
    #     print('')

    # cache the listings in the local file
    try:
        with open("result.txt", "w") as fp:
            fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

    except Exception:
        print("error here")
        #print(listing)
        pass

    # read from the local file
    with open("result.txt") as fp:
        lines = fp.readlines()

    properties = []
    for line in lines:
        properties.append(eval(line))

    df = pd.DataFrame(properties)
    print(df)

    df.to_csv('daft properties.csv')
    #property=df.iloc[0]

    # link=property['daft_link']
    # print(link)
    # URL = link
    # header = {'User-Agent': 'Mozilla/5.0'}
    # page = requests.get(URL, headers = header)
    # soup = BeautifulSoup(page.content, 'html.parser')
    # details = soup.find('div', class_='PropertyPage__ContentSection-sc-14jmnho-3 gXMwcB')
    # print(details.text)

#daft_scraper()