from re import match
import pandas as pd
from daftlistings import MapVisualization

def match_data(budget, rooms, bathrooms, county, stakeholder):

    # 1. obtain desired county dataset

    # df = pd.read_csv(f'county_data/{county}.csv') 
    df = pd.read_csv(f'county_data/Cork.csv')
    
    # 1.1 adjust POAs
    df.replace(['Price on Application'], [0], inplace=True)

    # 1.2 strip bed and bath from the relevant columns
    df['bedrooms']=df['bedrooms'].str.rstrip(' Bed')
    df['bathrooms']=df['bathrooms'].str.rstrip(' Bath')

    # 1.3 convert columns to int64

    df['monthly_price']=df['monthly_price'].astype('float').astype('Int64')

    df['bedrooms']=df['bedrooms'].str.extract('(\d+)')  
    df['bathrooms']=df['bathrooms'].str.extract('(\d+)')
    
    df['bedrooms']=df['bedrooms'].astype('float').astype('Int64')
    df['bathrooms']=df['bathrooms'].astype('float').astype('Int64')

    
    # 2. perform filtering using given parameters
    
    # 2.1 remove dwellings outisde of budget range
    df = df.loc[df['monthly_price']<=(int(budget))]
    print(df.dtypes)
    
    # 2.2 perform the same filtering for rooms and bathrooms
    df = df.loc[df['bedrooms']<=int(rooms)]
    df = df.loc[df['bathrooms']<=int(bathrooms)]
    
    
    # 2.3 use our predefined stakeholder groups to filter further to provide suitable results pertaining to the given group

    if stakeholder == 'young':

        priority_df=df[df['daft_link'].str.contains('apartment')]
        map_data(priority_df)

    elif stakeholder == 'family':

        priority_df=df[~df['daft_link'].str.contains('apartment')]        
        map_data(priority_df)

    elif stakeholder == 'elderly':
        
        priority_df=df[df['daft_link'].str.contains('apartment') & df['daft_link'].str.contains('bungalow')]
        map_data(priority_df)
        
    
def map_data(df):
    #df=df.drop('Unnamed: 0')
    # df['monthly_price']=df['monthly_price'].astype('float').astype('Int64')
    # for col in df.columns:
    #     print(col)

    # print(type(df))
    print(df)

    try: 
        print('trying to map data')
        property_map = MapVisualization(df)
        property_map.add_markers()
        property_map.add_colorbar()
        property_map.save("templates/property_map.html")
        print("Done, please checkout the html file")
    except Exception:
        pass
    
# match_data(500000, 2,1, 'Cork', 'Family')