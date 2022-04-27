import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization
import re
from bs4 import BeautifulSoup
import requests
import os

def daft_scraper():
    
    daft = Daft()

    #daft.set_location("Cork City")
    daft.set_search_type(SearchType.RESIDENTIAL_SALE)
    daft.set_min_price(1000)
    daft.set_max_price(1000000)

    listings = daft.search()

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
    df=df[~df['daft_link'].str.contains('site')]

    df.to_csv('daft properties.csv')
    os.remove('result.txt')
     
    #scrape_counties(daft)

def scrape_counties():

    daft = Daft()
    

    counties = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry', 'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']


    for county in counties:
        print('######################')
        print('County being scraped', county)
        print('####################')
        daft.set_search_type(SearchType.RESIDENTIAL_SALE)
        daft.set_location(county)
        daft.set_min_price(50000)
        daft.set_max_price(1000000)

        listings = daft.search()

        # cache the listings in the local file
        try:
            with open("result.txt", "w") as fp:
                fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

        except Exception:
            print("error here")
            # print(listings)
            # print('dont error')
            pass

        # read from the local file
        with open("result.txt") as fp:
            lines = fp.readlines()

        properties = []
        for line in lines:
            properties.append(eval(line))

        df = pd.DataFrame(properties)
        
        #ensure the dataframe is made up of only the given county
        df=df[df['daft_link'].str.contains(f'co.{county.lower()}')]

        #filter out any sites which make it into the residential section on daft
        df=df[~df['daft_link'].str.contains('site')]
        
        df.to_csv(f'county_data/{county}.csv')
        os.remove('result.txt')
           

# scrape_counties()
#daft_scraper()